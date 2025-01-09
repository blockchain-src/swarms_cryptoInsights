from agents.news_agent import NewsAgent
from agents.social_media_agent import SocialMediaAgent
from agents.onchain_agent import OnChainAnalyticsAgent
from agents.report_agent import ReportGenerator
from utils.plot_tools import plot_news_trend, plot_sentiment_distribution, plot_onchain_activity
from datetime import datetime
from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

if __name__ == "__main__":
    # 从环境变量获取 Twitter API 密钥
    twitter_api_key = os.getenv("TWITTER_API_KEY")
    if not twitter_api_key:
        raise EnvironmentError("Twitter API Key 未配置，请在 .env 文件中设置 TWITTER_API_KEY")

    # 初始化代理
    news_agent = NewsAgent()
    social_media_agent = SocialMediaAgent(api_key=twitter_api_key)
    onchain_agent = OnChainAnalyticsAgent()
    report_generator = ReportGenerator()

    # 收集数据
    news = news_agent.scrape_news()
    sentiments = social_media_agent.analyze_sentiments("Bitcoin")

    # 定义多链支持
    chains = ["BTC", "Ethereum", "Solana", "Base"]
    chain_reports = []
    chain_charts = []

    for chain in chains:
        # 获取链上数据
        onchain_data = onchain_agent.analyze_chain(chain)
        
        # 动态生成链上图表
        chart_path = f"{chain.lower()}_activity.png"
        plot_onchain_activity(
            ["2025-01-05", "2025-01-06", "2025-01-07"],  # 示例日期
            [onchain_data.get("large_transactions", 0), 
             onchain_data.get("active_addresses", 0), 
             onchain_data.get("whale_activity", 0)], 
            chart_path
        )
        chain_charts.append((chain, chart_path))
        
        # 添加链报告
        chain_report = f"=== {chain} 链上数据分析 ===\n"
        for key, value in onchain_data.items():
            chain_report += f"{key}: {value}\n"
        chain_reports.append(chain_report)

    # 数据准备
    # 示例新闻趋势数据（按日期分组）
    news_dates = ["2025-01-05", "2025-01-06", "2025-01-07"]
    news_counts = [15, 20, 10]

    # 示例情绪分析结果
    sentiment_summary = {"positive": 50, "neutral": 30, "negative": 20}

    # 生成新闻和情绪图表
    plot_news_trend(news_dates, news_counts, "news_trend.png")
    plot_sentiment_distribution(sentiment_summary, "sentiment_distribution.png")

    # 整合链上报告
    onchain_report = "\n".join(chain_reports)

    # 生成完整报告
    report = report_generator.generate_report(news, sentiments, onchain_report)

    # 将图表嵌入报告中
    report_with_charts = f"""
    {report}

    以下是生成的市场趋势图：
    1. 新闻趋势图：见文件 news_trend.png
    2. 社交媒体情绪分布图：见文件 sentiment_distribution.png

    链上活动图表：
    """
    for chain, chart_path in chain_charts:
        report_with_charts += f"{chain} 链活动图：见文件 {chart_path}\n"

    # 保存报告
    with open("market_insights_report.txt", "w") as f:
        f.write(report_with_charts)

    print("市场洞察报告和趋势图生成成功！")
