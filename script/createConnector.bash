
export KAFKA_TOPIC=tie_analysis_output
export MONGO_URI="mongodb://admin:TIETODOSSDDTFG@backend.novatrends.me:27017"
export MONGO_DB=tie
export MONGO_COLLECTION=news


# install connector plugin
#sudo apt update
#sudo apt install curl -y
#sudo confluent-hub install mongodb/kafka-connect-mongodb:latest

curl -X PUT http://localhost:8083/connectors/sink-mongodb-users/config -H "Content-Type: application/json" -d "{
      \"connector.class\":\"com.mongodb.kafka.connect.MongoSinkConnector\",
      \"tasks.max\":\"1\",
      \"topics\":\"$KAFKA_TOPIC\",
      \"connection.uri\":\"$MONGO_URI\",
      \"database\":\"$MONGO_DB\",
      \"collection\":\"$MONGO_COLLECTION\",
      \"key.converter\":\"org.apache.kafka.connect.json.JsonConverter\",
      \"key.converter.schemas.enable\":false,
      \"value.converter\":\"org.apache.kafka.connect.json.JsonConverter\",
      \"value.converter.schemas.enable\":false 
}"