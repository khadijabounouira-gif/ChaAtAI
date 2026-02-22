from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# المفتاح ديالك خاصك تحطيه في Render → Secrets
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            max_tokens=500
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = "عذرًا، وقع خطأ: " + str(e)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
