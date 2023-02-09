import requests
from send_email import send_email


link = "https://newsapi.org/v2/"
api_key = "apiKey=239e97455d7e4c8a9f956349d2f46e13"
d = "everything?q=tesla&from=2023-01-09&sortBy=publishedAt&"
url = f"{link}{d}{api_key}"

request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + \
            article["description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
