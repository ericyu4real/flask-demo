from flask import Flask
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})  # This allows all origins; you can specify specific origins instead

@app.route('/')

def home():
    return "flask heroku app"

@app.route("/api/query_bot", methods=["POST"])
def query_chat_bot():
    query =  request.form.get("question", "")
    if(query):
        try:
            # result = qa({"question": query})
            return jsonify({"response" : 'you can eat this d'+query}), 200
        except Exception:
            return jsonify({"error": "An error occurred. Please try again!"}), 500
    return jsonify({"error": "Invalid request. Please provide 'question' in JSON format."}), 400

if __name__ == '__main__':
    app.run()