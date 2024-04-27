# Product Discount Monitor

Product Discount Monitor is a Python application designed to track product discounts on OzBargain and notify users via Telegram when discounts are found. 
This project utilizes the RSS feed provided by OzBargain to check for new deals and integrates with Telegram for real-time notifications.

## Features

- **Product Monitoring**: Monitors specific products for discounts on OzBargain via their RSS feed.
- **Telegram Notifications**: Sends alerts through a Telegram bot when a new discount on a monitored product is detected.
- **Customizable Monitoring**: Users can customize which products to monitor through a configuration file.
- **Error Handling**: Robust error handling to manage common issues like network failures, RSS parsing errors, and Telegram API limits.
- **Logging**: Detailed logging of operations, errors, and notifications for troubleshooting and monitoring app performance.

## Installation

To get started with Product Discount Monitor, follow these steps:

### Prerequisites

- Python 3.8 or higher
- pip for installing dependencies

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/jack-jackhui/productDiscountAlert.git
   cd [project-folder]

2. Install the required Python libraries:
   pip install -r requirements.txt

### Configuration
To configure the application, edit the config.ini file with your Telegram bot token and chat ID:

[Telegram]

bot_token = your_telegram_bot_token

chat_id = your_chat_id

## Usage
To run the application, use the following command:
python main.py

## License
Distributed under the MIT License. See LICENSE for more information.

