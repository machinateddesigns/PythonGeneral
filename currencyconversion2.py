from requests import get
from pprint import PrettyPrinter

BASE_URL = "http://free.currconv.com/"
APP_URL = "https://api.freecurrencyapi.com/"
API_KEY = "fca_live_SC7wBxB9NXUR22eWfOClVDXtNXdYz3bVLqIyzIZi"

printer = PrettyPrinter()

def getCurrencies():
    endPoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endPoint
    data = get(url).json()
    printer.pprint(data)
    #return data['results']

def getCurrencyApp():
    appPoint = f"v1/latest?apikey={API_KEY}"
    app = APP_URL + appPoint
    appData = get(app).json()
    printer.pprint(appData)

getCurrencies()
#getCurrencyApp()

