import feedparser

class DealChecker:
    def __init__(self, rss_url, keywords):
        self.rss_url = rss_url
        self.keywords = [k.strip().lower() for k in keywords.split(',')]

    def is_expired(self, entry):
        # print("\nEntry keys:", entry.keys())
        # Check 'expired' in title (legacy)
        if 'expired' in entry.title.lower():
            # print(f"Expired via title: {entry.title}")
            return True
        # Check for ozb:title-msg type="expired"
        # feedparser converts : to _ in tags, so it's ozb_title_msg
        ozb_title_msg = entry.get('ozb_title-msg')
        # print(f"ozb_title_msg structure: {ozb_title_msg}")  # Debug line

        if ozb_title_msg:
            # Sometimes it's a dict, sometimes a list of dicts
            if isinstance(ozb_title_msg, dict):
                # print(f"Dict keys: {ozb_title_msg.keys()}")  # Debug line
                if ozb_title_msg.get('type') == 'expired':
                    # print(f"Expired via ozb_title_msg (dict): {ozb_title_msg}")
                    return True
            elif isinstance(ozb_title_msg, list):
                for msg in ozb_title_msg:
                    if msg.get('type') == 'expired':
                        # print(f"Expired via ozb_title_msg (list): {msg}")
                        return True
            # Sometimes it's just a string (rare)
            elif isinstance(ozb_title_msg, str):
                if 'expired' in ozb_title_msg.lower():
                    # print(f"Expired via ozb_title_msg (string): {ozb_title_msg}")
                    return True
        return False

    def check_deals(self):
        deals_found = []
        try:
            feed = feedparser.parse(self.rss_url)
            for entry in feed.entries:
                if self.is_expired(entry):
                    continue
                title = entry.title.lower()
                link = entry.link
                # At least two keywords in the title
                if sum(word in title for word in self.keywords) >= 2:
                    deals_found.append((entry.title, link))
            return deals_found if deals_found else None
        except Exception as e:
            print(f"An error occurred while fetching the RSS feed: {e}")
            return None
