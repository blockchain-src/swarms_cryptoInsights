from swarms import Agent
import requests
from bs4 import BeautifulSoup

NEWS_AGENT_PROMPT = """
你是一个专业的新闻采集代理，负责实时收集加密货币领域的新闻。
任务：
1. 爬取多个来源的最新新闻，包括 CoinDesk 和 CoinTelegraph。
2. 提取每篇新闻的标题、发布时间和关键内容。
3. 过滤掉与加密货币无关的新闻。
"""

class NewsAgent:
    def __init__(self):
        self.agent = Agent(agent_name="NewsAgent", system_prompt=NEWS_AGENT_PROMPT, max_loops=1)

    def scrape_coindesk(self):
        """爬取 CoinDesk 的新闻"""
        url = "https://www.coindesk.com"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article')
        news = []
        for article in articles:
            title = article.find('h2')
            summary = article.find('p')
            if title and summary:
                news.append({
                    "source": "CoinDesk",
                    "title": title.text.strip(),
                    "summary": summary.text.strip()
                })
        return news

    def scrape_cointelegraph(self):
        """爬取 CoinTelegraph 的新闻"""
        url = "https://cointelegraph.com"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article')
        news = []
        for article in articles:
            title = article.find('a', class_='post-card-inline__title-link')
            summary = article.find('p', class_='post-card-inline__text')
            if title and summary:
                news.append({
                    "source": "CoinTelegraph",
                    "title": title.text.strip(),
                    "summary": summary.text.strip()
                })
        return news

    def scrape_news(self):
        """整合多个来源的新闻"""
        coindesk_news = self.scrape_coindesk()
        cointelegraph_news = self.scrape_cointelegraph()
        return coindesk_news + cointelegraph_news
