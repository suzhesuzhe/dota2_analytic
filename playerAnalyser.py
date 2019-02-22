import math

from timestepDataPoint import TimestepDataPoint


class PlayerAnalyser:
    def set_datapoint_position(self, player, datapoint, index):
        x_position_series = player.timeseriess['xPosition']
        y_position_series = player.timeseriess['yPosition']
        datapoint.set_position(x_position_series[index], y_position_series[index], x_position_series[index + 1],
                               y_position_series[index + 1])

    def get_player_proximity(self, player, index, other_player):
        this_x_positions = player.timeseriess['xPosition']
        this_y_positions = player.timeseriess['yPosition']
        that_x_positions = other_player.timeseriess['xPosition']
        that_y_positions = other_player.timeseriess['yPosition']
        x_distance = int(this_x_positions[index]) - int(that_x_positions[index])
        y_distance = int(this_y_positions[index]) - int(that_y_positions[index])
        x_distance_squared = x_distance * x_distance
        y_distance_squared = y_distance * y_distance
        return math.sqrt(x_distance_squared + y_distance_squared)

    def get_player_proximities(self, player, index, other_players):
        ally_proximities = []
        enemy_proximities = []
        for other_player in other_players:
            if not player.id == other_player.id:
                proximity = player.get_player_proximity(player, index, other_player)
                if player.isRadiant == other_player.isRadiant:
                    ally_proximities.append(proximity)
                else:
                    enemy_proximities.append(proximity)
        ally_proximities.sort()
        enemy_proximities.sort()
        ally_proximities.extend(enemy_proximities)
        return ally_proximities

    def get_timestep_data_point(self, player, index, players):
        datapoint = TimestepDataPoint(player.isRadiant, player.timestep)
        for key in player.keys:
            datapoint.set_value(key, player.get_value_difference(key, index))
        timeMidPoint = int(player.timeseriess['CurrentTime'][index]) + (player.timestep / 2)
        datapoint.set_value('CurrentTime', timeMidPoint)
        self.set_datapoint_position(player, datapoint, index)

        datapoint.set_proximities(self.get_player_proximities(player, index, players))
        datapoint.set_distance_traveled()
        return datapoint

    def get_timestep_data_points(self, player, players):
        timestep_datapoints = []
        for i in range(player.saved_values - 1):
            timestep_datapoints.append(self.get_timestep_data_point(player, i, players))
        return timestep_datapoints

    def get_positional_data_point(self, player, index):
        return {
            'xPosition': player.timeseriess['xPosition'][index],
            'yPosition': player.timeseriess['yPosition'][index],
            'time': player.timeseriess['CurrentTime'][index]
        }

    def get_positional_timeseries(self, player):
        timeseries = []
        for i in range(player.saved_values):
            timeseries.append(self.get_positional_data_point(player, i))
        return timeseries

    def get_ability_priorities(self, player):
        return None if player.ability_priority is None else player.ability_priority.get_ability_priority()

    def get_value_at(self, player, value, time):
        if value not in player.keys:
            return None
        else:
            current_time = player.timeseriess['CurrentTime']
            index = 0
            while current_time[index] < time:
                index += 1

            return player.timeseriess[value][index]

    def get_farm_priority(self, player, other_players, time):
        my_XP = int(self.get_value_at(player, 'XP', time))
        my_last_hits = int(self.get_value_at(player, 'LastHits', time))
        total_XP = my_XP
        total_last_hits = my_last_hits
        for other_player in other_players:
            if player.isRadiant == other_player.isRadiant and player.id != other_player.id:
                total_XP += int(self.get_value_at(other_player, 'XP', time))
                total_last_hits += int(self.get_value_at(other_player, 'LastHits', time))
        percentage_XP = my_XP / total_XP
        percentage_last_hits = my_last_hits / total_last_hits
        return [percentage_XP, percentage_last_hits, player.isRadiant]
