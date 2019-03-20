import os

from game import Game
from gameAnalyser import GameAnalyser
from textFileParser import TextFileParser
import pandas as pd

textFileDirectory = 'D:\\BigDota\\Txts\\720\\fewer-games\\'
textFileParser = TextFileParser(0.66, track_timeseriess=True)
games = []

fileNames = os.listdir(textFileDirectory)
results = []
for fileName in fileNames:
    newGame = Game(fileName, 0)
    if len(games) > 5:
        break
    try:
        games.append(newGame)
        data_file = open(textFileDirectory + '\\' + fileName, encoding="utf-8-sig")
        for line in data_file:
            textFileParser.parse_line(newGame.players, line)
    except FileNotFoundError:
        print("no txt found for match id - {}".format(str(fileName)))

timeseriess = []
farm_priorities = []
match_ids = []
for game in games:
    game_analyser = GameAnalyser()
    timeseriess.extend(game_analyser.get_positional_timeseriess(game))
    farm_priorities.append(game_analyser.get_farm_priorities(game))
    match_ids.extend([game.id] * len(game.players))

df = pd.DataFrame(timeseriess)
df.insert(loc=0, column='matchID', value=match_ids)
for i in range(10):
    index = i * 50
    timeseries = timeseriess[i]
    datapoint = timeseries[index]
    print("time - {} position - {} {}".format(datapoint['time'], datapoint['xPosition'], datapoint['yPosition']))

for i in range(5):
    farm_priority = farm_priorities[i]
    for player in farm_priority:
        print("xp prio - {}  last hit prio - {}  isRadiant - {}".format(player[0], player[1], player[2]))
