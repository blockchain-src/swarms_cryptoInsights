# utils/plot_tools.py
import matplotlib.pyplot as plt
from datetime import datetime

def plot_news_trend(dates, counts, output_path):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, counts, marker='o', linestyle='-', color='b')
    plt.title("News Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of News Articles")
    plt.grid(True)
    plt.savefig(output_path)
    plt.close()

def plot_sentiment_distribution(sentiments, output_path):
    labels = ["Positive", "Neutral", "Negative"]
    sizes = [sentiments.get("positive", 0), sentiments.get("neutral", 0), sentiments.get("negative", 0)]
    colors = ["green", "gray", "red"]
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
    plt.title("Social Media Sentiment Distribution")
    plt.savefig(output_path)
    plt.close()

def plot_chain_activity(chain_name, data, output_path):
    plt.figure(figsize=(10, 6))
    labels = list(data.keys())
    values = list(data.values())

    plt.bar(labels, values, color="blue")
    plt.title(f"{chain_name} On-Chain Activity")
    plt.xlabel("Metrics")
    plt.ylabel("Values")
    plt.grid(axis="y")
    plt.savefig(output_path)
    plt.close()
