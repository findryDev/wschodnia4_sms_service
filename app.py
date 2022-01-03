from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from models import db
from models import TemperatureModelSensor1
from models import TemperatureModelSensor2
from models import TemperatureModelSensor3
from requestDomoticz import getTempForDomoticzAPI
from queriesFromDB import sensorQueries
from generate_message import get_domoticz_information, get_CO_information



app = Flask(__name__)

app.config.from_object('config.DevConfig')

db.init_app(app)



@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'syp' in incoming_msg:
        msg.body(get_domoticz_information()['sypialnia'])
        # return a beadroom condition
        responded = True

    if 'kuch' in incoming_msg:
        msg.body(get_domoticz_information()['kuchnia'])
        # return a kitchen condition
        responded = True
    if 'kot' in incoming_msg:
        msg.body(get_domoticz_information()['kotlownia'])
        # return a boiler room condition
        responded = True
    if 'laz' in incoming_msg:
        msg.body(get_domoticz_information()['lazienka'])
        # return a boiler room condition
        responded = True
    if 'wej' in incoming_msg:
        msg.body(get_domoticz_information()['wejscie'])
        # return a boiler room condition
        responded = True
    if 'piec' in incoming_msg:
        msg.body(get_CO_information())
        responded = True

    if not responded:
        msg.body('sorry!')
    return str(resp)


@app.route('/api/dom', methods=['GET'])
def api():
    return get_domoticz_information()

@app.route('/api/piec', methods=['GET'])
def piec():
    return get_CO_information()

if __name__ == '__main__':
    app.run(host='localhost')