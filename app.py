from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the sentiment analysis model
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_model = pipeline("sentiment-analysis", model=model_name)

@app.route("/", methods=["GET", "POST"])
def sentiment_analysis():
    if request.method == "POST":
        text = request.form.get("text")

        # Perform sentiment analysis on the input text
        result = sentiment_model(text)

        # Extract the sentiment label and score
        label = result[0]["label"]
        score = result[0]["score"]

        return render_template("index.html", text=text, label=label, score=score)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
