from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from models import db
from models import TemperatureModelSensor1
from models import TemperatureModelSensor2
from models import TemperatureModelSensor3
from requestDomoticz import getTempForDomoticzAPI



SENSOR_ID = {'sypialnia': 3,
             'kuchnia': 6,
             'lazienka': 7,
             'kotlownia' : 8,
             'wejscie': 36}

syp = getTempForDomoticzAPI(3)
        jad = getTempForDomoticzAPI(6)
        laz = getTempForDomoticzAPI(7)
        kot = getTempForDomoticzAPI(8)
        wej = getTempForDomoticzAPI(36)




app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'sypialnia' in incoming_msg:
        # return a beadroom condition
        responded = True
    if 'kuchnia' in incoming_msg:
        # return a kitchen condition
        responded = True
    if 'kotlownia' or 'kotłownia' in incoming_msg:
        # return a boiler room condition
        responded = True
    if 'sypialnia' in incoming_msg:
        # return a beadroom condition
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()