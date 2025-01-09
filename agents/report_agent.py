from swarms import Agent

REPORT_GENERATOR_PROMPT = """
你是一个报告生成专家，负责整合新闻、社交媒体情绪和链上数据，生成市场洞察报告。
任务：
1. 整合所有数据，生成每日市场总结。
2. 以清晰的格式输出，包括数据图表和关键信息。
"""

class ReportGenerator:
    def __init__(self):
        self.agent = Agent(agent_name="ReportGenerator", system_prompt=REPORT_GENERATOR_PROMPT, max_loops=1)

    def generate_report(self, news, sentiments, onchain_data):
        report_input = f"新闻: {news}\n情绪: {sentiments}\n链上数据: {onchain_data}"
        return self.agent.run(report_input)
