import os
import json
from flask import Flask, request
from flask_cors import CORS
from flask_restplus import Api, Resource, reqparse
from flask_request_id_header.middleware import RequestID


import utils.kafka_utils as kafka

API_PORT = int(os.environ['API_PORT'])
KAFKA_OUTPUT_TOPIC = os.environ['TIE_API_OUTPUT_TOPIC']
KAFKA_PRODUCER_SETTINGS = json.loads(os.environ['TIE_KAFKA_PRODUCER_SETTINGS'])

app = Flask('tie')
api = Api(app)
service = api.namespace('etl')

CORS(app)

app.config['REQUEST_ID_UNIQUE_VALUE_PREFIX'] = 'TIE-ETL-'
RequestID(app)


args_parser = reqparse.RequestParser()
args_parser.add_argument('q', required=True, type=str, location='form', help='a string with keywords to serach')

@service.route("/kafka")
class Search(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = args_parser
        self._producer = kafka.build_producer(KAFKA_PRODUCER_SETTINGS)

    @api.doc('Starts a search of news over the internet')
    @api.expect(args_parser)
    @api.response(200, 'Success')
    def post(self):
        # get query
        q = self._get_args()
        # build kafka message
        message = {
            "request": {
                "id": request.environ.get("HTTP_X_REQUEST_ID"),
                "keywords": q
            }
        }
        message = json.dumps(message)
        # send to kafka
        kafka.write(self._producer, KAFKA_OUTPUT_TOPIC, message)
        return {
            "status": "ok",
            "keywords": q,
            "id": request.environ.get("HTTP_X_REQUEST_ID")
        }

    def _get_args(self):
        args = self.parser.parse_args()
        q = args['q']
        return q


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=API_PORT)
