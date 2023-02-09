import requests
from send_email import send_email


link = "https://newsapi.org/v2/everything?"
api_key = "apiKey=239e97455d7e4c8a9f956349d2f46e13"
topic = "q=tesla"
d = f"&from=2023-01-09&sortBy=publishedAt&"
lang = "&language=en"
url = f"{link}{topic}{d}{api_key}{lang}"

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" "\n" + \
            body + article["title"] + "\n" + \
            article["description"] + "\n" + \
            article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
