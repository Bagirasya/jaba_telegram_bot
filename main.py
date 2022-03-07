import req
import requests
from config import API_link


if __name__ == '__main__':
    updates = requests.get(API_link + "/getUpdates?offset=-1").json()
    print(updates)

    message = updates['result'][0]['message']
    chat_id = message['from']['id']
    text = message['text']