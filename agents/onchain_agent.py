from swarms import Agent

ONCHAIN_ANALYTICS_AGENT_PROMPT = """
你是一个链上数据分析专家，专注于监控加密货币链上活动。
任务：
1. 跟踪大额转账（如超过1000 BTC的交易）。
2. 监控鲸鱼地址的活动。
3. 提供链上数据的每日总结，包括转账量、活跃地址数和Gas费。
"""

class OnChainAnalyticsAgent:
    def __init__(self):
        self.agent = Agent(agent_name="OnChainAnalyticsAgent", system_prompt=ONCHAIN_ANALYTICS_AGENT_PROMPT, max_loops=1)

    def analyze_onchain_data(self, chain_name):
        # 示例逻辑：假设使用链上分析 API 提供数据
        onchain_data = {"whale_activity": "High", "large_transactions": 15}
        return self.agent.run(str(onchain_data))
