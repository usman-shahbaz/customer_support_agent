from flask import Flask, request, jsonify
from bedrock import get_response

app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    prompt = data["message"]

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "text": prompt
                }
            ]
        }
    ]

    answer = get_response(messages)

    return jsonify({
        "response": answer
    })


@app.route("/health")
def health():
    return {
        "status": "ok"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  
