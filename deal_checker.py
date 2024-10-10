import feedparser
import requests
import xml.etree.ElementTree as ET
class DealChecker:
    def __init__(self, rss_url, product_name):
        self.rss_url = rss_url
        self.product_name = product_name

    def check_deals(self):
        deals_found = []
        try:
            response = requests.get(self.rss_url)
            response.raise_for_status()
            xml_content = response.content

            # Parse the XML content
            root = ET.fromstring(xml_content)

            # Define namespaces
            namespaces = {
                'atom': 'http://www.w3.org/2005/Atom',
                'dc': 'http://purl.org/dc/elements/1.1/',
                'media': 'http://search.yahoo.com/mrss/',
                'ozb': 'https://www.ozbargain.com.au',
            }

            # Iterate over each item in the feed
            for item in root.findall('.//item'):
                title = item.find('title').text or ''
                link = item.find('link').text or ''

                # Check for the 'ozb:title-msg' tag to determine if the deal is expired
                title_msg = item.find('ozb:title-msg', namespaces)
                if title_msg is not None and title_msg.get('type') == 'expired':
                    continue  # Skip expired deals

                # Fallback: Check if 'expired' is in the title
                if 'expired' in title.lower():
                    continue

                # Check if the product name is in the title
                if self.product_name.lower() in title.lower():
                    deals_found.append((title, link))
            return deals_found if deals_found else None
        except Exception as e:
            print(f"An error occurred while fetching the RSS feed: {e}")
            return None
