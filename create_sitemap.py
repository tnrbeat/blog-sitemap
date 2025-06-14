import feedparser
from datetime import datetime

RSS_URL = "https://flashsoudannavi.blogspot.com/feeds/posts/default?alt=rss&max-results=100"
SITEMAP_FILE = "sitemap.xml"

def create_sitemap():
    feed = feedparser.parse(RSS_URL)
    urls = []
    for entry in feed.entries:
        urls.append(entry.link)

    header = '<?xml version="1.0" encoding="UTF-8"?>\n'
    header += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    footer = '</urlset>'

    body = ""
    for url in urls:
        body += "  <url>\n"
        body += f"    <loc>{url}</loc>\n"
        body += f"    <lastmod>{datetime.now().date()}</lastmod>\n"
        body += "  </url>\n"

    sitemap = header + body + footer

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(sitemap)

if __name__ == "__main__":
    create_sitemap()
