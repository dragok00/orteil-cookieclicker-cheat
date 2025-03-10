# orteil-cookieclicker-cheat

# Automated Cookie Clicker Bot

This is an automated bot that plays [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) using Selenium. The bot continuously clicks the cookie and purchases available upgrades and power-ups to maximize efficiency.

## Features
- Automatically clicks the main cookie to generate cookies.
- Buys available upgrades to boost cookie production.
- Purchases power-ups when they become available.
- Runs continuously, managing cookie generation and optimizations.

## Requirements
- Python installed (preferably Python 3.x)
- Google Chrome installed
- Chrome WebDriver matching the installed Chrome version
- Required Python packages: `selenium` and `schedule`

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/dragok00/cookie-clicker-bot.git
   cd cookie-clicker-bot
   ```
2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```
3. Download Chrome WebDriver from [here](https://sites.google.com/chromium.org/driver/) and place it in a known directory.
4. Update the script with the correct path to your `chromedriver.exe` file.

## Usage
1. The bot will:
   - Accept the cookie policy.
   - Select the English language.
   - Start clicking the main cookie.
   - Every 5 seconds, attempt to buy an upgrade or power-up if available.

## Disclaimer
This bot is for educational purposes only. Use it responsibly and be aware that automated scripts might violate the game's terms of service.

