from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def count_text(text):
    words = text.split()
    paragraphs = text.strip().split("\n")
    characters = len(text)

    return {
        "words": len(words),
        "paragraphs": len([p for p in paragraphs if p.strip()]),
        "characters": characters
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/count", methods=["POST"])
def count():
    text = request.form.get("text", "")
    result = count_text(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
