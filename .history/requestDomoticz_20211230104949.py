import requests

username = 'ZmlsaXA='
password = 'Rm42OTYxMjk2MDc='


def getTempForDomoticzAPI(id):
    results = {}
    endpoint = (("http://213.227.70.24:8080/json.htm?") +
                (f"username={username}") +
                (f"&password={password}&type=devices&rid={id}"))
    r = requests.get(endpoint)
    if r.status_code == 200:
        data = r.json()
        results = {"temperature": data['result'][0]['Temp'],
                   "humidity": data['result'][0]['Humidity'],
                   "lastUpdate": data['result'][0]['LastUpdate'],
                   "batteryLevel": data['result'][0]['BatteryLevel']}

        return results
    else:
        return ('NONE', r.status_code)
