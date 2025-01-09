# utils/web_scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_page_content(url, headers=None):
    """
    获取网页内容。
    参数:
        url: 网页链接
        headers: 可选的请求头
    返回:
        网页 HTML 内容
    """
    headers = headers or {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 如果请求失败则抛出异常
    return response.text

def extract_elements(html, css_selector):
    """
    使用 CSS 选择器提取网页中的元素。
    参数:
        html: 网页 HTML 内容
        css_selector: CSS 选择器字符串
    返回:
        提取的元素列表
    """
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.select(css_selector)
    return elements

def scrape_articles(url, article_selector, title_selector, summary_selector):
    """
    通用新闻爬取函数。
    参数:
        url: 新闻主页链接
        article_selector: 文章容器的 CSS 选择器
        title_selector: 标题的 CSS 选择器
        summary_selector: 摘要的 CSS 选择器
    返回:
        包含标题和摘要的文章列表
    """
    html = fetch_page_content(url)
    articles = []
    for article in extract_elements(html, article_selector):
        title_elem = article.select_one(title_selector)
        summary_elem = article.select_one(summary_selector)
        if title_elem and summary_elem:
            articles.append({
                "title": title_elem.get_text(strip=True),
                "summary": summary_elem.get_text(strip=True),
            })
    return articles
