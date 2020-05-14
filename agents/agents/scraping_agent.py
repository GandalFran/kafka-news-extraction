import json
import requests
from typing import List
from agents.agent import Agent
from lxml.html import fromstring
from lxml.html.clean import clean_html


class ScrapingAgent(Agent):

    def task(self, message: str) -> List[str]:
        # get list of articles
        article = json.loads(message)
        # request the web
        response = requests.get(article['url'], headers={
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                          '60.0.3112.113 Safari/537.36',
            "X-Requested-With": "XMLHttpRequest"
        })
        # parse the web
        text = ''
        try:
            html = clean_html(response.text)
            dom = fromstring(html)
            p_elements = dom.cssselect('p')
            for p in p_elements:
                text = text + p.text_content().encode().decode('utf-8')
        except:
            text = ''
        article['text'] = text
        response = json.dumps(article)
        return [response]