import os
import json
import logging
from agents.scraping_agent import ScrapingAgent

if __name__ == '__main__':
    input_topic = os.environ['TIE_SCRAPING_INPUT_TOPIC']
    output_topic = os.environ['TIE_SCRAPING_OUTPUT_TOPIC']
    producer_settings = os.environ['TIE_KAFKA_PRODUCER_SETTINGS']
    consumer_settings = os.environ['TIE_KAFKA_CONSUMER_SETTINGS']
    producer_settings = json.loads(producer_settings)
    consumer_settings = json.loads(consumer_settings)

    logging.basicConfig(level=logging.DEBUG)

    agent = ScrapingAgent(producer_settings, consumer_settings, input_topic, output_topic)
    agent.behaviour()
