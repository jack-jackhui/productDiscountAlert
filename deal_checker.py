import feedparser

class DealChecker:
    def __init__(self, rss_url):
        self.rss_url = rss_url

    def check_deals(self, product_name):
        feed = feedparser.parse(self.rss_url)
        for entry in feed.entries:
            # Check for expired tag in the entry
            if 'expired' not in str(entry).lower():  # Check for non-expired entries
                if product_name.lower() in entry.title.lower():
                    return entry.title, entry.link
        return None
