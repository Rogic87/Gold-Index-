from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def ussd():
    text = request.values.get('text', '')

    if text == '':
        response = "CON GOLD INDEX\n"
        response += "Intl: ZMW 3500/g\n"
        response += "------------------\n"
        response += "1. Lusaka    ZMW 2800\n"
        response += "2. Kitwe     ZMW 2700\n"
        response += "3. Solwezi   ZMW 2500\n"
        response += "4. Mpika     ZMW 2100\n"
        response += "5. Mufumbwe  ZMW 2200\n"
        response += "6. Kasempa   ZMW 1800\n"
        response += "7. Mumbwa    ZMW 1700\n"
        response += "\n"
        response += "0. Exit"

    elif text == '0':
        response = "END Thank you.\nKnow your worth.\nGold Index"

    else:
        response = "END Invalid option.\nDial again."

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
