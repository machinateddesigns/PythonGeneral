'''
Note: This project is heavily modified because data.nba.net
no longer exists, so I had to find a similar dataset at
https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json
'''
from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"

printer = PrettyPrinter()

data = get(BASE_URL).json()

scoreboard = data["scoreboard"]

games = scoreboard["games"]

def getGames():
    print(scoreboard['gameDate'])
    for game in games:
        homeTeam = game['homeTeam']
        awayTeam = game['awayTeam']
        period = game['period']
        clock = game['gameClock']
        if clock == "":
            clock = 0
        status = game['gameStatusText']
        leaders = game['gameLeaders']
        hLeaders = leaders['homeLeaders']
        aLeaders = leaders['awayLeaders']
        print(f"{homeTeam['teamCity']} {homeTeam['teamName']} {homeTeam['score']} VS {awayTeam['teamCity']} {awayTeam['teamName']} {awayTeam['score']} | Time Left: {clock} | Periods: {period} | Status: {status}\nGame Leaders: Home: {hLeaders['jerseyNum']} {hLeaders['name']} Away: {aLeaders['jerseyNum']} {aLeaders['name']}\n----------------------")
        #break
getGames()