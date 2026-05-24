from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Bhai amar bot jinda ache! 🔥"

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    msg = request.form.get('Body', '').lower()
    
    if 'hello' in msg or 'hi' in msg:
        reply = "Hello bhai! Ami tor mini AI bot ❤️ Ki khobor?"
    elif 'kemon' in msg:
        reply = "Bindas achi bhai. Tui bol 😎"
    elif 'naam' in msg:
        reply = "Amar naam Mini AI Bot. Tor jonno banano."
    else:
        reply = "Bhai ami notun. Sudhu hello, kemon acho, naam ki bolte pari 🤖"
    
    return f'<Response><Message>{reply}</Message></Response>'

if __name__ == '__main__':
    app.run()
