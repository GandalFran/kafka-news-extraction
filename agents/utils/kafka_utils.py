from confluent_kafka import Consumer, Producer


def build_producer(settings: dict) -> Producer:
    producer = Producer(settings)
    return producer


def build_consumer(settings: dict, input_topic: str) -> Consumer:
    consumer = Consumer(settings)
    consumer.subscribe([input_topic])
    return consumer


def read(consumer: Consumer) -> str or None:
    msg = consumer.poll()
    if msg is not None and not msg.error():
        msg = msg.value().decode('utf-8')
        return msg
    else:
        return None


def write(producer: Producer, topic: str, message: str):
    producer.produce(topic, value=message)
    producer.flush()
