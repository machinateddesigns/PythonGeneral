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
    print('''-------------------------------------''')
    for game in games:
        homeTeam = game['homeTeam']
        awayTeam = game['awayTeam']
        homeScore = homeTeam['score']
        awayScore = awayTeam['score']
        period = game['period']
        if period == 0:
            homeScore = ""
            awayScore = ""
        clock = game['gameClock']
        if clock == "":
            clock = 0
        status = game['gameStatusText']
        leaders = game['gameLeaders']
        hLeaders = leaders['homeLeaders']
        aLeaders = leaders['awayLeaders']
        print(f'''{homeTeam['teamCity']} {homeTeam['teamName']} {homeScore} 
VS 
{awayTeam['teamCity']} {awayTeam['teamName']} {awayScore}''')
        print(f"{status}")
        if status == "Final":
            print(f'''Game Leaders: 
Home: {hLeaders['jerseyNum']} {hLeaders['name']} 
Away: {aLeaders['jerseyNum']} {aLeaders['name']}''')
        print('''-------------------------------------''')
        #break
getGames()