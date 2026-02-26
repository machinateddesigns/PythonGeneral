'''
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.
==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.
'''

#Imports for requests, webbrowser and (formerly) JSON. 
#Turns out it was doing nothing since the json comes in as a string/dictionary so we commented it out as the parser was complaining.
import requests
import webbrowser
#import json

#a painstakingly constructed list, grabbed from the API and converted from JSON to what you see here.
curCodes = ["USD", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SLL", "SOS", "SRD", "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "UYU", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"]
API_KEY = "9956274efae582820753793c" #Your API Key Here
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

#Input the currency code to convert from
def getConvertFrom():
    while True:
        convertFrom = input("Enter the ISO 4217 Currency Code you are converting from: ").upper().strip()
        if convertFrom in curCodes:
            return convertFrom
        else:
            print("❌ Invalid currency code. Please enter a valid 3-letter ISO 4217 currency code.")
            listCurrencyCodes()

#Input the currency code to convert to
def getConvertTo():
    while True:
        convertTo = input("Enter the ISO 4217 Currency Code you are converting to: ").upper().strip()
        if convertTo in curCodes:
            return convertTo
        else:
            print("❌ Invalid currency code. Please enter a valid 3-letter ISO 4217 currency code.")
            listCurrencyCodes()

#Maybe the user isn't familiar with the ISO 4217 3 letter currency codes! Perhaps we can help them by providing them with our list, 
#and opening the page to what those codes mean in wikipedia for them.
def listCurrencyCodes():
    yN = input("Would you like a list of available Currency Codes? This will open your web browser. Y/N: ").upper().strip()
    if yN == "Y" or yN == "YES":
        webbrowser.open('https://en.wikipedia.org/wiki/ISO_4217#List_of_ISO_4217_currency_codes')
        print("Available Codes: ")
        print(*curCodes, sep =', ')
        print(" ")
        return
    else:
        return

# function to get the currency conversion API
def runConversion():
#base = "USD"
    base = getConvertFrom()
#selection = "EUR"
    selection = getConvertTo()
#Have the user input the amount they want to convert from base to the selection
    amountFrom = posFloat(f"Enter the amount of {base} you wish to convert into {selection}: ")
#Here's where we set the API data including the dynamic base
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base}"
#This calls the RESTful API utilizing the requests module we imported
    response = requests.get(url)
#if the status code is 200, meaning it was successful, 
    if response.status_code == 200:
#then the program continues and collects the data from the API, 
#translating it into a JSON format which is read by python like a dictionary.
        data = response.json()
        conversion = data["conversion_rates"][f"{selection}"]
#Now we take that data we obtained using the selection as the key, and multiply the amount the user wants to convert by that number, obtaining the result
        convertedAmount = conversion * amountFrom
#We then print the result for the user, and exit this function, and the whole program.
        print(f"The current conversion rate for {base} to {selection} is {conversion}{selection} to 1{base}. Your {amountFrom} {base} is now {convertedAmount} {selection}.")
        return
#Unless something went wrong, in which case, we just have the program end. There's not much I can do if their API isn't working at this point, or I've run out of free uses for the month.
    else:
        print("An error has occured connecting to the API. Please try again later.")
        return None
#This just prints the title and runs the primary function.
if __name__ == "__main__":
    print("        💰 CURRENCY CONVERTER 💰")
    print("💴💵 Utilizing the ExchangeRate-API 💶💷")
    runConversion()
