from swarms import Agent
import requests

SOCIAL_MEDIA_AGENT_PROMPT = """
你是一个社交媒体情绪分析专家，专注于分析加密货币相关推文和帖子。
任务：
1. 收集与特定加密货币相关的推文和帖子。
2. 使用情绪分析工具判断市场情绪（正面、中立或负面）。
3. 生成每小时的情绪比例统计数据。
"""

class SocialMediaAgent:
    def __init__(self, api_key):
        self.agent = Agent(agent_name="SocialMediaAgent", system_prompt=SOCIAL_MEDIA_AGENT_PROMPT, max_loops=1)
        self.api_key = api_key

    def analyze_sentiments(self, keyword):
        # 假设这是一个调用 Twitter API 的方法
        response = requests.get(f"https://api.twitter.com/2/tweets/search/recent?query={keyword}", headers={
            "Authorization": f"Bearer {self.api_key}"
        })
        tweets = response.json()
        sentiments = [self.agent.run(tweet['text']) for tweet in tweets]
        return sentiments
