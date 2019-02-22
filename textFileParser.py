from fieldsToTrack import FieldsToTrack


class TextFileParser:
    previousTickTime = 0

    def __init__(self, timestep=30, fields_to_track=None, track_timeseriess=False, track_abilities=False):
        self.timestep = timestep
        self.track_timeseriess = track_timeseriess
        self.fields_to_track = \
            fields_to_track.get_dictionary() if fields_to_track is not None else FieldsToTrack().track_all().get_dictionary()
        self.track_abilities = track_abilities

    def parse_player_line(self, player, line):
        is_hero = False
        if line.startswith("hero"):
            line = line.lstrip("hero")
            is_hero = True
        line = line[1:]
        name_value_pair = line.split('\t')
        name = name_value_pair[0]
        value = name_value_pair[1]
        value = value.split('\n')[0]
        if is_hero and name == "Name":
            player.set_hero_name(value)
        elif self.fields_to_track.keys().__contains__(name) and self.fields_to_track[name] is True:
            player.update_value(name, value)

    def parse_players_line(self, players, line):
        if line.startswith("UPDATE\tplayer"):
            line = line.lstrip("UPDATE\tplayer")
            player_number = int(line[0])
            line = line[1:]
            self.parse_player_line(players[player_number], line)

    def parse_tick_line(self, players, line):
        tick_time = float(line)
        if self.timestep > 0:
            tick_time_difference = (tick_time - self.previousTickTime) % self.timestep
            if tick_time_difference > self.timestep - 1 and tick_time > 0:
                for player in players:
                    player.update_value("CurrentTime", tick_time)
                    player.save_current_values()
                self.previousTickTime = tick_time
        else:
            for player in players:
                player.update_value("CurrentTime", tick_time)
                player.save_current_values()

    def parse_ability_line(self, players, line):
        line = line.lstrip("UPDATE\t")
        player_index = int(line[-2])
        ability_name = line.split("\t")[0]
        players[player_index].update_ability(ability_name)

    def parse_line(self, players, line):
        if line.startswith("UPDATE\tplayer") and self.track_timeseriess:
            self.parse_players_line(players, line)
        elif line.startswith("TICK\t") and self.track_timeseriess:
            tick_time_string = line.lstrip("TICK\t")
            self.parse_tick_line(players, tick_time_string)
        elif line.startswith("UPDATE") and "AbilityLevel" in line and self.track_abilities:
            self.parse_ability_line(players, line)
        elif line.startswith("UPDATE\tplayer") and "hero" in line and 'Name' in line:
            self.parse_players_line(players, line)

    def parse_file(self):
        print("soon")
