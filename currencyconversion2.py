import json #not sure if I still need this
import webbrowser
from requests import get
from pprint import PrettyPrinter

'''
This site from the tutorial no longer works, as there is 
no way to get an API key for it for free.
BASE_URL = "http://free.currconv.com/"
API_KEY = ""
'''
#New site. Pulled JSON files from them for local testing. Only 100 calls available.
BASE_URL = "https://api.exchangerate.host/"
API_KEY = "12ad37bc18248058f735f5ce1078ed31"

#Old site from my earlier project. 1500 calls available.
APP_URL = "https://api.freecurrencyapi.com/"
APP_API_KEY = "fca_live_SC7wBxB9NXUR22eWfOClVDXtNXdYz3bVLqIyzIZi"

printer = PrettyPrinter()

'''
paths for local currency data. Updated the file of currencies2 
#to include currency symbols. May keep this in the version that 
#accesses the exchange data so I'm not running extra calls.
'''
path1 = "currencies2.json"
path2 = "currexch2.json"

#Local JSON Currency Codes, Names & Symbols, scraped from exchangerate.host

def getCurrJson():
    try:
        with open(path1, 'r', encoding="utf-8") as f:
            data = json.load(f)['currencies']
            
    except FileNotFoundError:
        print(f"Error: The file '{path1}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{path1}'. Check if the JSON is valid.")
    data = list(data.items())
    data.sort()
    return data

#sorted exchange in a list
def getCurrExchJSON():
    try:
        with open(path2, 'r', encoding="utf-8") as f:
            data = json.load(f)['quotes']
    except FileNotFoundError:
        print(f"Error: The file '{path2}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{path2}'. Check if the JSON is valid.")
    
    data = list(data.items())
    data.sort()
    return data

#unsorted exchange
def getExchJSON():
    try:
        with open(path2, 'r', encoding="utf-8") as f:
            data = json.load(f)['quotes']
    except FileNotFoundError:
        print(f"Error: The file '{path2}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{path2}'. Check if the JSON is valid.")

    return data

#This is using api.exchangerate.host
def getCurrencies():
    endPoint = f"list?access_key={API_KEY}"
    url = BASE_URL + endPoint
    data = get(url).json()['currencies']
    data = list(data.items())
    data.sort()
    return data

#This is using api.freecurrencyapi.com
def getCurrencyApp():
    appPoint = f"v1/latest?apikey={APP_API_KEY}"
    app = APP_URL + appPoint
    appData = get(app).json()
    printer.pprint(appData)

#sets local json copy of api.exchangerate.host/list as currencies
currencies = getCurrJson()
#make a list of currency codes
curr = []
for c in currencies:
    curr.append(c[0])
print("        💰 CURRENCY CONVERTER 💰")
print("💴💵 Utilizing the api.exchangerate.host JSON pulled 2/25/2026 💶💷")    
print(*curr, sep =', ')
#prints whatever data is in currencies
def print_currencies(currencies):
    for currency in currencies:
        code = currency[0]
        name = currency[1][0]
        symbol = currency[1][1]
        print(f"{code} - {name} - {symbol}1")

exchange = getCurrExchJSON()

def print_exchange(exchange):
    USDUSD = ("USDUSD",float(1))
    print(f"{USDUSD[0][3:6]} - {USDUSD[1]}")
    for ex in exchange:
        code = ex[0]
        rate = ex[1]
        #print(f"{code} - {rate}")
        print(f"{code[3:6]} - {rate}")

#getCurrencies()
#getCurrencyApp()

#Maybe the user isn't familiar with the ISO 4217 3 letter currency codes! Perhaps we can help them by providing them with our list, 
#and opening the page to what those codes mean in wikipedia for them.
def listCurrencyCodes(curr):
    yN = input("Would you like a list of available Currency Codes? This will open your web browser. Y/N: ").upper().strip()
    if yN == "Y" or yN == "YES":
        webbrowser.open('https://en.wikipedia.org/wiki/ISO_4217#List_of_ISO_4217_currency_codes')
        print("Available Codes: ")
        print(*curr, sep =', ')
        print(" ")
        return
    else:
        return

def getConvertFrom(curr):
    
    while True:
        convertFrom = input("Enter the ISO 4217 Currency Code you are converting from: ").upper().strip()
        if convertFrom in curr:
            return convertFrom
        else:
            print("❌ Invalid currency code. Please enter a valid 3-letter ISO 4217 currency code.")
            listCurrencyCodes()

#Input the currency code to convert to
def getConvertTo(curr):
    while True:
        convertTo = input("Enter the ISO 4217 Currency Code you are converting to: ").upper().strip()
        if convertTo in curr:
            return convertTo
        else:
            print("❌ Invalid currency code. Please enter a valid 3-letter ISO 4217 currency code.")
            listCurrencyCodes()

def exchangeRate(curr):
    currFrom = getConvertFrom(curr)
    currTo = getConvertTo(curr)
    fromVal = getExchJSON()[f"USD{currFrom}"]
    toVal = getExchJSON()[f"USD{currTo}"]
    exchangeRate = toVal / fromVal
    return exchangeRate

#Grabbing my posFloat function from other programs to make sure they input a positive number.
def posFloat(y):
    while True:
        try:
            x = float(input(y))
            if x <= 0:
                print ("❌ That wasn't a positive amount greater than zero! Please try again.")
            else:
                return x
        except ValueError:
            print("❌ Invalid input! Please enter an amount greater than zero.")


amountFrom = posFloat(f"Enter the amount of X you wish to convert into Y: ")
print(amountFrom*exchangeRate(curr))

#print_currencies(currencies)
#print_exchange(exchange)