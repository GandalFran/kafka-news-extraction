import json
from typing import List
from agents.agent import Agent
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class AnalysisAgent(Agent):

    def __init__(self, producer_settings, consumer_settings, input_topic, output_topic):
        super().__init__(producer_settings, consumer_settings, input_topic, output_topic)
        self._analyzer = SentimentIntensityAnalyzer()

    def task(self, message: str) -> List[str]:
        # get list of articles
        article = json.loads(message)

        # analyze
        article['sentiment'] = self._analyzer.polarity_scores(article['content'])

        # build kafka message
        response = json.dumps(article)
        return [response]
