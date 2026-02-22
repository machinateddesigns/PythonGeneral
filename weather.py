from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.weather.gov/"


printer = PrettyPrinter()

data = get(BASE_URL)