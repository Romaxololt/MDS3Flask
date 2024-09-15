from flask import Flask, request, jsonify

app = Flask(__name__)

# Liste des messages
messages = []

# Route pour envoyer un message
@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message')
    if message:
        messages.append(message)
        return jsonify({"status": "Message received", "message": message}), 200
    return jsonify({"error": "No message found"}), 400

# Route pour recevoir des messages
@app.route('/receive', methods=['GET'])
def receive_message():
    if messages:
        return jsonify({"messages": messages}), 200
    return jsonify({"message": "No new messages"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
