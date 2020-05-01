import json
import logging
from typing import List
import utils.kafka_utils as kafka


class Agent:
    LOG = logging.getLogger('kafka')

    def __init__(self, producer_settings, consumer_settings, input_topic, output_topic):
        self._output_topic = output_topic
        self._producer = kafka.build_producer(producer_settings)
        self._consumer = kafka.build_consumer(consumer_settings, input_topic)

    def behaviour(self):
        while True:
            try:
                message = kafka.read(self._consumer)
                Agent.LOG.debug(f"received new message {json.loads(message)['request']['id']}")
                if message is not None:
                    results = self.task(message)
                    if results is not None:
                        for result in results:
                            Agent.LOG.debug(f"responded to message {json.loads(message)['request']['id']}")
                            kafka.write(self._producer, self._output_topic, result)
            except:
                pass

    def task(self, message: str) -> List[str]:
        return [message]
