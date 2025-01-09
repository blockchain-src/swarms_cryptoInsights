# agents/onchain_agent.py
from swarms import Agent

ONCHAIN_ANALYTICS_AGENT_PROMPT = """
你是一个链上数据分析专家，支持多条链（BTC、Ethereum、Solana、Base）的数据分析。
任务：
1. 动态分析指定链上的关键指标。
2. 提供每条链的每日总结，包括转账量、活跃地址数和特定链指标。
3. 高亮链上异常（如大额交易或网络拥堵）。
"""

class OnChainAnalyticsAgent:
    def __init__(self):
        self.agent = Agent(agent_name="OnChainAnalyticsAgent", system_prompt=ONCHAIN_ANALYTICS_AGENT_PROMPT, max_loops=1)

    def analyze_btc(self):
        # 示例逻辑：返回 BTC 的链上数据
        return {
            "large_transactions": 12,
            "whale_activity": "High",
            "active_addresses": 150000,
        }

    def analyze_eth(self):
        # 示例逻辑：返回 Ethereum 的链上数据
        return {
            "gas_fees": 25,  # 单位：Gwei
            "large_transactions": 8,
            "active_addresses": 500000,
        }

    def analyze_solana(self):
        # 示例逻辑：返回 Solana 的链上数据
        return {
            "tps": 2000,  # 每秒交易数
            "transaction_count": 3000000,
            "active_stake_accounts": 120000,
        }

    def analyze_base(self):
        # 示例逻辑：返回 Base 的链上数据
        return {
            "tvl": 80000000,  # 锁仓量
            "active_users": 20000,
            "transactions": 500000,
        }

    def analyze_chain(self, chain_name):
        if chain_name.lower() == "btc":
            return self.analyze_btc()
        elif chain_name.lower() == "ethereum" or chain_name.lower() == "eth":
            return self.analyze_eth()
        elif chain_name.lower() == "solana" or chain_name.lower() == "sol":
            return self.analyze_solana()
        elif chain_name.lower() == "base":
            return self.analyze_base()
        else:
            return {"error": "Unsupported chain"}
