import asyncio
import configparser
from telegram_bot import TelegramBot
from deal_checker import DealChecker

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

async def main():
    config = load_config()
    bot_token = config['Telegram']['bot_token']
    chat_id = config['Telegram']['chat_id']
    rss_url = config['Ozbargain']['rss_url']
    product_name = config['Ozbargain']['product_name']

    bot = TelegramBot(bot_token, chat_id)
    checker = DealChecker(rss_url, product_name)

    result = checker.check_deals()
    if result:
        title, link = result
        await bot.send_message(f"Discount found for {product_name}: {title} - {link}")
    else:
        await bot.send_message(f"No discounts found for {product_name}.")

if __name__ == '__main__':
    asyncio.run(main())
