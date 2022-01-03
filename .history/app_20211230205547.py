from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from models import db
from models import TemperatureModelSensor1
from models import TemperatureModelSensor2
from models import TemperatureModelSensor3
from requestDomoticz import getTempForDomoticzAPI


SENSOR_ID = {'sypialnia': 3,
             'kuchnia': 6,
             'lazienka': 7,
             'kotlownia': 8,
             'wejscie': 36}


app = Flask(__name__)




@app.route('/bot', methods=['POST'])
def bot():
    '''
    "temperature": ,
    "humidity":,
    "lastUpdate":,
    "batteryLevel"
    '''

    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'sypialnia' in incoming_msg:
        dom = getTempForDomoticzAPI(SENSOR_ID['sypialnia'])
        domoticz_message = f'''
        Sypialnia
        Temperatura: {dom["temperature"]}
        Wilgotnosc: {dom["humidity"]}
        Ostatni pomiar: {dom['lastUpdate']}
        Poziom baterii: {dom['batteryLevel']}
        '''
        msg.body(domoticz_message)
        # return a beadroom condition
        responded = True
    if 'kuchnia' in incoming_msg:
        dom = getTempForDomoticzAPI(SENSOR_ID['kuchnia'])
        domoticz_message = f'''
        Kuchnia
        Temperatura: {dom["temperature"]}
        Wilgotnosc: {dom["humidity"]}
        Ostatni pomiar: {dom['lastUpdate']}
        Poziom baterii: {dom['batteryLevel']}
        '''
        msg.body(domoticz_message)
        # return a kitchen condition
        responded = True
    if 'kotlownia' or 'kotłownia' in incoming_msg:
        dom = getTempForDomoticzAPI(SENSOR_ID['kotlownia'])
        domoticz_message = f'''
        Kotłownia
        Temperatura: {dom["temperature"]}
        Wilgotnosc: {dom["humidity"]}
        Ostatni pomiar: {dom['lastUpdate']}
        Poziom baterii: {dom['batteryLevel']}
        '''
        msg.body(domoticz_message)
        # return a boiler room condition
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


@app.route('/api', methods=['GET'])
def api():
    '''
    "temperature": ,
    "humidity":,
    "lastUpdate":,
    "batteryLevel"
    '''

    domoticz_message = ''
    dom = getTempForDomoticzAPI(SENSOR_ID['sypialnia'])
    domoticz_message = domoticz_message + f'''
    Sypialnia
    Temperatura: {dom["temperature"]}
    Wilgotnosc: {dom["humidity"]}
    Ostatni pomiar: {dom['lastUpdate']}
    Poziom baterii: {dom['batteryLevel']}
    '''
    dom = getTempForDomoticzAPI(SENSOR_ID['kuchnia'])
    domoticz_message = domoticz_message +  f'''
    Kuchnia
    Temperatura: {dom["temperature"]}
    Wilgotnosc: {dom["humidity"]}
    Ostatni pomiar: {dom['lastUpdate']}
    Poziom baterii: {dom['batteryLevel']}
    '''
    dom = getTempForDomoticzAPI(SENSOR_ID['kotlownia'])
    domoticz_message = domoticz_message + f'''
    Kotłownia
    Temperatura: {dom["temperature"]}
    Wilgotnosc: {dom["humidity"]}
    Ostatni pomiar: {dom['lastUpdate']}
    Poziom baterii: {dom['batteryLevel']}
    '''
    dom = getTempForDomoticzAPI(SENSOR_ID['sypialnia'])
    domoticz_message = domoticz_message + f'''
    Sypialnia
    Temperatura: {dom["temperature"]}
    Wilgotnosc: {dom["humidity"]}
    Ostatni pomiar: {dom['lastUpdate']}
    Poziom baterii: {dom['batteryLevel']}
    '''
    return domoticz_message





if __name__ == '__main__':
    app.run(host='localhost')