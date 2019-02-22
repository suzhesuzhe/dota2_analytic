import math


class TimestepDataPoint:
    keys = [
        'initXPosition',
        'initYPosition',
        'finalXPosition',
        'finalYPosition',
        'distanceTraveled',
        'HealthPercent',
        'HeroDamage',
        'HeroHealing',
        'CreepDamage',
        'LastHits',
        'CurrentTime',
        'ally_proximity_1',
        'ally_proximity_2',
        'ally_proximity_3',
        'ally_proximity_4',
        'enemy_proximity_1',
        'enemy_proximity_2',
        'enemy_proximity_3',
        'enemy_proximity_4',
        'enemy_proximity_5'
    ]

    def __init__(self, is_radiant, timestep):
        self.data = {
            'initXPosition': 0,
            'initYPosition': 0,
            'finalXPosition': 0,
            'finalYPosition': 0,
            'distanceTraveled': 0,
            'HealthPercent': 0,
            'HeroDamage': 0,
            'HeroHealing': 0,
            'CreepDamage': 0,
            'LastHits': 0,
            'CurrentTime': 0,
            'ally_proximity_1': 0,
            'ally_proximity_2': 0,
            'ally_proximity_3': 0,
            'ally_proximity_4': 0,
            'enemy_proximity_1': 0,
            'enemy_proximity_2': 0,
            'enemy_proximity_3': 0,
            'enemy_proximity_4': 0,
            'enemy_proximity_5': 0,
            'timeStep': timestep,
            'isRadiant': is_radiant
        }

    def set_value(self, key, value):
        timestep = self.data['timeStep']
        if key in self.data:
            self.data[key] = float(value) / timestep

    def set_timestep(self, timestep):
        self.data['timeStep'] = timestep

    def set_position(self, init_x_position, init_y_position, final_x_position, final_y_position):
        self.data['initXPosition'] = init_x_position
        self.data['initYPosition'] = init_y_position
        self.data['finalXPosition'] = final_x_position
        self.data['finalYPosition'] = final_y_position

    def set_proximities(self, proximities):
        self.data['ally_proximity_1'] = proximities[0]
        self.data['ally_proximity_2'] = proximities[1]
        self.data['ally_proximity_3'] = proximities[2]
        self.data['ally_proximity_4'] = proximities[3]
        self.data['enemy_proximity_1'] = proximities[4]
        self.data['enemy_proximity_2'] = proximities[5]
        self.data['enemy_proximity_3'] = proximities[6]
        self.data['enemy_proximity_4'] = proximities[7]
        self.data['enemy_proximity_5'] = proximities[8]

    def set_distance_traveled(self):
        x_distance = int(self.data['finalXPosition']) - int(self.data['initXPosition'])
        y_distance = int(self.data['finalYPosition']) - int(self.data['initYPosition'])
        timestep = self.data['timeStep']
        self.data['distanceTraveled'] = math.sqrt(x_distance * x_distance + y_distance * y_distance) / timestep

    def print_self(self):
        print("datapoint print start")
        for key in self.keys:
            print("attribute  - {}, value - {}".format(key, self.data[key]))
        print("datapoint print end")

    def is_radiant(self):
        return self.data['isRadiant']

    def data_point_to_matrix(self):
        result = []
        for key in self.keys:
            result.append(self.data[key])

        return result
