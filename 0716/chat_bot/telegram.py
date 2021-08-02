import requests
from decouple import config

TOKEN = config('telegram_token')
CHAT_ID = config('telegram_chat_id')

# url = f'https://api.telegram.org/bot{TOKEN}/{METHOD_NAME}'

def getMe():
    url = f'https://api.telegram.org/bot{TOKEN}/getMe'
    response = requests.get(url).json()
    return response

def getUpdates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url).json()
    return response

def sendMessage(msg):
    METHOD_NAME = f'sendMessage?chat_id={CHAT_ID}&text={msg}'
    url = f'https://api.telegram.org/bot{TOKEN}/{METHOD_NAME}'
    response = requests.get(url).json()
    return response

