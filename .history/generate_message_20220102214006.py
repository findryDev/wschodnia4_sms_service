from models import TemperatureModelSensor1
from models import TemperatureModelSensor2
from models import TemperatureModelSensor3
from requestDomoticz import getTempForDomoticzAPI
from queriesFromDB import sensorQueries

SENSOR_ID = {'sypialnia': 3,
             'kuchnia': 6,
             'lazienka': 7,
             'kotlownia': 8,
             'wejscie': 36}

def get_domoticz_information():
    sensors = SENSOR_ID
    dom = {}
    message = {}
    for s in sensors:
        dom[s] = getTempForDomoticzAPI(sensors[s])
    for key in dom.keys():
        message[key] = f"""
        {key.title()}
        Temperatura: {dom[key]["temperature"]}
        Wilgotnosc: {dom[key]["humidity"]}
        Ostatni pomiar: {dom[key]['lastUpdate']}
        Poziom baterii: {dom[key]['batteryLevel']}
        """
    return message




def get_CO_information():
    out_CO = sensorQueries(TemperatureModelSensor1)
    in_CO = sensorQueries(TemperatureModelSensor2)
    return_CO = sensorQueries(TemperatureModelSensor3)
    boiler_message = f'''
    Wyjscie: {out_CO['temperature']} - {out_CO['date']}
    Piec: {in_CO['temperature']} - {in_CO['date']}
    Powrot: {return_CO['temperature']} - {return_CO['date']}
    '''
    return boiler_message
