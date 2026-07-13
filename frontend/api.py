import requests

API_URL = "http://localhost:5000/chat"


def ask_llm(prompt):

    response = requests.post(
        API_URL,
        json={
            "message": prompt
        }
    )

    return response.json()["response"]
  
