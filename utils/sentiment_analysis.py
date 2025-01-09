# utils/sentiment_analysis.py
from textblob import TextBlob

def analyze_sentiment(text):
    """
    分析单条文本的情绪。
    返回情绪类别：'positive', 'neutral', 或 'negative'。
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  # 情感极性分数：[-1.0, 1.0]
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

def analyze_sentiment_batch(texts):
    """
    分析多条文本的情绪。
    返回正面、中立和负面的统计结果。
    """
    sentiment_summary = {"positive": 0, "neutral": 0, "negative": 0}
    for text in texts:
        sentiment = analyze_sentiment(text)
        sentiment_summary[sentiment] += 1
    return sentiment_summary
