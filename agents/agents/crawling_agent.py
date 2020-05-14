import json
from typing import List
from agents.agent import Agent
from newsapi import NewsApiClient


class CrawlingAgent(Agent):

    def __init__(self, api_key: str, producer_settings, consumer_settings, input_topic, output_topic):
        super().__init__(producer_settings, consumer_settings, input_topic, output_topic)
        self._client = NewsApiClient(api_key=api_key)

    def task(self, message: str) -> List[str]:
        message = json.loads(message)
        keywords = message['request']['keywords']
        crawled = self._client.get_everything(q=keywords, language='en')
        return [json.dumps({
                'request': message['request'],
                'url': article['url'],
                'title': article['title'],
                'date': article['publishedAt'],
                'author': article['author'],
                'source': article['source']['name']
            }) for article in crawled['articles']]
