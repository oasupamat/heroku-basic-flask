import json
import requests
from flask import Flask, request, abort

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_channel_access_token = 'TioJy3Z69p9xCmG2RXgW1WNTDPQ0EEIbz2fM2786d8uMvl6WSIx+wWqobq8OEu3x0TzUxFUMo8Wi28uJUyxaoHlI7y1D3QO+UmXI0QDMmO5M/GFHe255Zh/zEk4VJcFqh1wYaObBthd4lhOiBsWD4gdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(line_channel_access_token)
handler = WebhookHandler('96363b03e615241b7d68c6ef2ba8dcf2')
Authorization = "Bearer {}".format(line_channel_access_token)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    body = json.loads(body)
    print (body)

    reply_token = body['events'][0]["replyToken"]
    print("reply_token: {}".format(reply_token))

    event_type = body['events'][0]['type']
    print("event_type: {}".format(event_type))

    if event_type == "message":
        message_type = body['events'][0]['message']['type']
        # print("message_type: {}".format(message_type))
        if message_type == "text":
            text = body['events'][0]['message']['text']
            print("text: {}".format(text))
            if "home" in text or "Home" in text:
                print("replying text:{}".format(text))
                reply_menu3(reply_token)
            elif text == "weather":
                line_bot_api.reply_message(reply_token, TextSendMessage(text='ตอนนี้อุณหภูมิ ที่บ้าน 30 C '))
            elif text == "energy":
                line_bot_api.reply_message(reply_token, TextSendMessage(text='การใช้ไไฟ้าที่บ้านวันนี้ 3.4 หน่วย คิดเป็นเงิน 12 บาท'))

    return '',200



def reply_menu(reply_token):
    print('from reply menu')
    print("Authorization:{}".format(Authorization))
    print("reply_token:{}".format((reply_token)))

    # line_bot_api.reply_message(reply_token, TextSendMessage(text='Hello World222!'))

    response = requests.post(
        url="https://api.line.me/v2/bot/message/reply",
        headers={
            "Content-Type": "application/json",
            "Authorization": Authorization,
        },
        data=json.dumps({
            "replyToken": str(reply_token),
            "messages": [
                {
                    "type": "text",
                    "text": "เชิญเลือกเมนูได้เลยครับ",
                    "quickReply": {
                        "items": [
                            {
                                "type": "action",
                                "imageUrl": 'https://drive.google.com/uc?export=download&id=1Hsd2w0YF1ThUIQEiXXm-6s67fmV7azh2',
                                "action": {
                                    "type": "message",
                                    "label": "home",
                                    "text": "Home"
                                }
                            },
                            {
                                "type": "action",
                                "imageUrl": 'https://drive.google.com/uc?export=download&id=1Hsd2w0YF1ThUIQEiXXm-6s67fmV7azh2',
                                "action": {
                                    "type": "message",
                                    "label": "weather",
                                    "text": "weather"
                                }
                            },
                            {
                                "type": "action",
                                "imageUrl": 'https://drive.google.com/uc?export=download&id=1Hsd2w0YF1ThUIQEiXXm-6s67fmV7azh2',
                                "action": {
                                    "type": "message",
                                    "label": "energy",
                                    "text": "energy"
                                }
                            }
                        ]
                    }
                }
            ]
        })
    )
    print('Response HTTP Status Code: {status_code}'.format(
        status_code=response.status_code))
    print('Response HTTP Response Body: {content}'.format(
        content=response.content))


def reply_menu2(reply_token):
    print('from reply menu')
    print("Authorization:{}".format(Authorization))
    print("reply_token:{}".format((reply_token)))

    # line_bot_api.reply_message(reply_token, TextSendMessage(text='Hello World222!'))

    response = requests.post(
        url="https://api.line.me/v2/bot/message/reply",
        headers={
            "Content-Type": "application/json",
            "Authorization": Authorization,
        },
        data=json.dumps({
            "replyToken": str(reply_token),
            "messages": [{
  "type": "template",
  "altText": "this is a carousel template",
  "template": {
    "type": "carousel",
    "actions": [],
    "columns": [
      {
        "thumbnailImageUrl": "https://d3n8a8pro7vhmx.cloudfront.net/edonsw/pages/995/attachments/original/1386210667/green_energy_320.jpg",
        "text": "Energy",
        "actions": [
          {
            "type": "message",
            "label": "click",
            "text": "energy"
          }
        ]
      },
      {
        "thumbnailImageUrl": "https://d3n8a8pro7vhmx.cloudfront.net/edonsw/pages/995/attachments/original/1386210667/green_energy_320.jpg",
        "text": "Weather",
        "actions": [
          {
            "type": "message",
            "label": "click",
            "text": "weather"
          }
        ]
      }
    ]
  }
}]
        })
    )


def reply_menu3(reply_token):
    response = requests.post(
        url="https://api.line.me/v2/bot/message/reply",
        headers={
            "Content-Type": "application/json",
            "Authorization": Authorization,
        },
        data=json.dumps({
            "replyToken": str(reply_token),
            "messages": [{
  "type": "template",
  "altText": "this is a carousel template",
  "template": {
    "type": "carousel",
    "actions": [],
    "columns": [
      {
        "thumbnailImageUrl": "https://sv1.picz.in.th/images/2019/06/27/1CCpqZ.th.jpg",
        "text": "weather",
        "actions": [
          {
            "type": "message",
            "label": "weather",
            "text": "weather"
          }
        ]
      },
      {
        "thumbnailImageUrl": "https://d3n8a8pro7vhmx.cloudfront.net/edonsw/pages/995/attachments/original/1386210667/green_energy_320.jpg",
        "text": "energy",
        "actions": [
          {
            "type": "message",
            "label": "energy",
            "text": "energy"
          }
        ]
      }
    ]
  }
}]
        })
    )




def reply_menu4(reply_token):
    response = requests.post(
        url="https://api.line.me/v2/bot/message/reply",
        headers={
            "Content-Type": "application/json",
            "Authorization": Authorization,
        },
        data=json.dumps({
            "replyToken": str(reply_token),
            "messages": []
        })
    )


def reply_menu5(reply_token):
    response = requests.post(
        url="https://api.line.me/v2/bot/message/reply",
        headers={
            "Content-Type": "application/json",
            "Authorization": Authorization,
        },
        data=json.dumps({
            "replyToken": str(reply_token),
            "messages": []
        })
    )


def reply_menu6(reply_token):
    response = requests.post(
        url="https://api.line.me/v2/bot/message/reply",
        headers={
            "Content-Type": "application/json",
            "Authorization": Authorization,
        },
        data=json.dumps({
            "replyToken": str(reply_token),
            "messages": []
        })
    )

if __name__ == "__main__":
    app.run()
