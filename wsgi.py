from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route('/shuffle', methods=['POST'])
def shuffle():
    command = request.form.get('command')
    text = request.form.get('text')

    items = []
    for item in text.split(','):
        if item.strip() != "":
            items.append(item.strip())

    random.shuffle(items)

    if command == '/shuffle' and len(items) > 0:
        return jsonify({
            "response_type": "in_channel",
            "text": "The order is...",
            "attachments": [
                {
                    "text": ', '.join(items)
                }
            ]
        })
    else:
        return jsonify({
            "response_type": "ephemeral",
            "text": "Sorry, that didn't work. Please try again."
        })

if __name__ == "__main__":
    application.run()
