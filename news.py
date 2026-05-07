from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = "your_api_key_here"

@app.route("/")
def home():
    return "News API Project"

@app.route("/news/<topic>")
def get_news(topic):

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch news"}

    data = response.json()

    articles = []

    for item in data["articles"][:5]:
        articles.append({
            "title": item["title"],
            "source": item["source"]["name"]
        })

    return jsonify(articles)

app.run(debug=True)