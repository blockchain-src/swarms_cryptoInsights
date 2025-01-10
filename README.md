# 加密货币市场洞察项目

## **概述**

加密货币市场洞察项目是一个综合框架，用于监控和分析加密货币市场。本项目从多个来源（如新闻网站、社交媒体平台和区块链网络）收集和分析数据，以生成可操作的市场洞察和可视化报告。

## **功能**

1. **新闻聚合**

   - 从多个来源（例如 CoinDesk、CoinTelegraph）收集与加密货币相关的新闻。
   - 提取标题和摘要以便快速浏览。

2. **社交媒体情绪分析**

   - 分析社交媒体平台（例如 Twitter）上的情绪（正面、中立、负面）。
   - 总结关键加密货币的市场情绪。

3. **区块链数据分析**

   - 支持多条链，包括比特币（BTC）、以太坊（ETH）、Solana（SOL）和 Base。
   - 跟踪关键指标，如大额交易、鲸鱼活动、活跃地址和网络性能。

4. **可视化和报告**

   - 生成新闻频率、社交媒体情绪分布和区块链活动的趋势图。
   - 以文本格式生成综合市场洞察报告。

## **安装**

### 前置条件

- Python 3.10 或更高版本
- 虚拟环境（可选但推荐）

### 安装步骤

1. 克隆代码仓库：

   ```bash
   git clone https://github.com/blockchain-src/swarms_cryptoInsights.git && cd swarms_cryptoInsights
   ```

2. 创建并激活虚拟环境：

   ```bash
   sudo apt install python3.12-venv -y && python3 -m venv swarms_env && source swarms_env/bin/activate
   ```

3. 一键安装依赖：

   ```bash
   chmod +x install.sh && ./install.sh
   ```

4. 配置环境变量：

   ```bash
   echo 'TWITTER_API_KEY=your_twitter_api_key' >> .env
   ```

## **使用方法**

### 运行主程序

执行主脚本以收集数据、进行分析并生成报告：

```bash
python3 main.py
```

### 输出

- **市场洞察报告：** 一个文本文件，摘要了新闻、社交媒体情绪和区块链活动（例如 `market_insights_report.txt`）。
- **图表：** 可视化趋势图的 PNG 文件（例如 `news_trend.png`，`sentiment_distribution.png`，`btc_activity.png`）。

## **项目结构**

```
crypto-market-insights/
├── agents/
│   ├── news_agent.py           # 聚合多个来源的新闻
│   ├── social_media_agent.py   # 分析社交媒体情绪
│   ├── onchain_agent.py        # 区块链数据分析
│   ├── report_agent.py         # 生成综合报告
├── utils/
│   ├── sentiment_analysis.py   # 提供情绪分析功能
│   ├── web_scraper.py          # 通用网页爬取工具
│   ├── plot_tools.py           # 生成可视化图表
├── main.py                     # 主程序
├── requirements.txt            # 项目依赖
├── README.md                   # 项目文档
```

## **自定义**

- **添加更多新闻来源：** 扩展 `NewsAgent` 类，添加新的网站爬取逻辑。
- **支持更多区块链：** 修改 `OnChainAnalyticsAgent` 类，集成额外的区块链 API。
- **增强情绪分析：** 替换 `TextBlob` 为更高级的 NLP 库（例如 Hugging Face Transformers）。

## **参与贡献**

欢迎提交拉取请求！对于重大更改，请先打开 issue 讨论您的建议。

## **许可证**

本项目基于 MIT 许可证。详见 `LICENSE` 文件。

