import json
import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}'

@app.route('/api/bot', methods=['POST'])
def bot():
    body = request.get_json()
    message = body.get('message', {})
    chat_id = message.get('chat', {}).get('id')
    text = message.get('text')

    if text == '/start':
        send_message(chat_id, 'Bot is working')

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Received'})
    }

def send_message(chat_id, text):
    url = f'{TELEGRAM_API_URL}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run()
