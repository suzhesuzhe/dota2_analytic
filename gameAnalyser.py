from playerAnalyser import PlayerAnalyser


class GameAnalyser:
    def __init__(self):
        self.playerAnalyser = PlayerAnalyser()

    def check_hero_name(self, hero_name, player):
        return hero_name is None or player.hero_name == hero_name

    def get_filtered_players(self, game, hero_name):
        return game.players if hero_name is None else filter(lambda x: self.check_hero_name(hero_name, x),game.players)

    def get_timestep_data_point(self, game, hero_name=None):
        datapoints = []

        filtered_players = self.get_filtered_players(game, hero_name)

        map(lambda x: datapoints.extend(self.playerAnalyser.get_timestep_data_points(x, game.players)), filtered_players)
        return datapoints

    def get_positional_timeseriess(self, game, hero_name=None):
        timeseriess = []

        filtered_players = self.get_filtered_players(game, hero_name)

        map(lambda x: timeseriess.append(self.playerAnalyser.get_positional_timeseries(x)), filtered_players)
        return timeseriess

    def get_ability_priorities(self, game, hero_name=None):
        ability_priorities = []

        filtered_players = self.get_filtered_players(game, hero_name)
        for player in filtered_players:
            ability_priority = self.playerAnalyser.get_ability_priorities(player)
            if ability_priority is not None:
                ability_priorities.append({'hero': player.hero_name, 'priority': ability_priority})

        return ability_priorities

    def get_farm_priorities(self, game, hero_name=None):
        farm_priorities = []

        filtered_players = self.get_filtered_players(game, hero_name)
        for player in filtered_players:
                farm_priorities.append(self.playerAnalyser.get_farm_priority(player, game.players, 600))
        return farm_priorities
