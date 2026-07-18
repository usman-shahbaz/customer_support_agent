from flask import Flask, jsonify, request
from flask_cors import CORS

from agent_v2.agent import CustomerSupportAgentV2
from agent_v2.session import SessionManager

app = Flask(__name__)
CORS(app)

agent = CustomerSupportAgentV2()
session_manager = SessionManager()


@app.get("/")
def home():

    return {
        "status": "ok",
        "agent": "v2"
    }


@app.post("/chat")
def chat():

    body = request.get_json()

    question = body["question"]

    session_id = body.get(
        "session_id",
        "default",
    )

    session = session_manager.get(
        session_id
    )

    answer = agent.chat(
        question,
        session,
    )

    return jsonify(
        {
            "answer": answer
        }
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True,
    )
