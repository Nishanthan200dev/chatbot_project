from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Expanded chatbot responses
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! What do you need?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a simple chatbot, built to assist you!",
    "bye": "Goodbye! Have a great day!",
    "who created you": "I was created by a budding Python developer!",
    "what can you do": "I can answer basic questions. Try asking me something!",
    "thanks": "You're welcome!",
    "default": "I'm not sure how to respond to that. Can you rephrase?"
}
@app.route("/")
def home():
    return render_template("index.html")
# Chatbot API Route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()  # Get JSON input from user
    user_message = data.get("message", "").lower()  # Convert message to lowercase

    # Get response based on user input, or return default response
    bot_response = responses.get(user_message, responses["default"])

    return jsonify({"response": bot_response})  # Return JSON response

# Run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
