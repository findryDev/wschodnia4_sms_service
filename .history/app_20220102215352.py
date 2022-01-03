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
        domoticz_message = ''
        responded = True
    if 'kot' in incoming_msg:
        msg.body(get_domoticz_information()['kotlownia'])
        # return a boiler room condition
        domoticz_message = ''
        responded = True
    if 'laz' in incoming_msg:
        msg.body(get_domoticz_information()['lazienka'])
        # return a boiler room condition
        domoticz_message = ''
        responded = True
    if 'wej' in incoming_msg:
        msg.body(get_domoticz_information()['wej'])
        # return a boiler room condition
        domoticz_message = ''
        responded = True
    if 'piec' in incoming_msg:
        out_CO = sensorQueries(TemperatureModelSensor1)
        in_CO = sensorQueries(TemperatureModelSensor2)
        return_CO = sensorQueries(TemperatureModelSensor3)
        piec_message = f'''
        Wyjscie: {out_CO['temperature']}->{out_CO['date']}
        Piec: {in_CO['temperature']}->{in_CO['date']}
        Powrot: {return_CO['temperature']}->{return_CO['date']}
        '''
        msg.body(piec_message)
        responded = True


    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


@app.route('/api/dom', methods=['GET'])
def api():
    return get_domoticz_information()

@app.route('/api/piec', methods=['GET'])
def piec():
    return get_CO_information()





if __name__ == '__main__':
    app.run(host='localhost')