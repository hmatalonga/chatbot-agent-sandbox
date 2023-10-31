import os
from flask import Flask, jsonify, request
from litellm import completion_with_retries
from dotenv import load_dotenv

_ = load_dotenv()

app = Flask(__name__)


# Example route
@app.route("/", methods=["GET"])
def hello():
    return jsonify(message="Hello, Flask!")


@app.route("/chat/completions", methods=["POST"])
def api_completion():
    data = request.json
    data["api_base"] = os.environ["OLLAMA_SERVER_URL"]
    data["model"] = os.environ["OLLAMA_SERVER_MODEL"]
    try:
        response = completion_with_retries(**data)
    except Exception as e:
        print(e)

    return response
