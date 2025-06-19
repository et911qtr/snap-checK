import requests
import time
import os

BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']
USERNAME = os.environ['USERNAME']
DELAY = int(os.environ.get('DELAY', 600))

def is_username_available(username):
    url = f'https://signup.snapchat.com/accounts/check_username_v2?requested_username={username}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data.get('status_code') == 'USERNAME_AVAILABLE'
    except Exception as e:
        print(f'Error checking username: {e}')
        return False

def send_telegram_message(message):
    telegram_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}
    try:
        requests.post(telegram_url, data=payload)
    except Exception as e:
        print(f'Error sending Telegram message: {e}')

while True:
    print(f'Checking username: {USERNAME}')
    if is_username_available(USERNAME):
        send_telegram_message(f'🔥 اليوزر متاح الآن: {USERNAME} 🔥 احجزه بسرعة!')
        break
    else:
        print(f'{USERNAME} not available yet. Retrying in {DELAY} seconds...')
    time.sleep(DELAY)
