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
        content = ''
        try:
            # obtain the dom
            html = clean_html(response.text)
            dom = fromstring(html)
            # obtain all p elements and join
            p_elements = dom.cssselect('p')
            for p in p_elements:
                content = content + p.text_content()
        except:
            content = ''

        # encode the text
        content = content.encode().decode('utf-8')

        # store content in the article
        article['content'] = content

        # build response message
        response = json.dumps(article)

        return [response]