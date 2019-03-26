#from AbilityPriorityGradients import AbilityPriorityGradients


class Player:
    keys = [
        'xPosition',
        'yPosition',
        'HealthPercent',
        'HeroDamage',
        'HeroHealing',
        'CreepDamage',
        'LastHits',
        'XP',
        'CurrentTime'
    ]

    playerId = 0

    def __init__(self, timestep, id):
        self.values = {
            'xPosition': 0,
            'yPosition': 0,
            'HealthPercent': 0,
            'HeroDamage': 0,
            'HeroHealing': 0,
            'CreepDamage': 0,
            'LastHits': 0,
            'XP': 0,
            'CurrentTime': 0
        }
        self.timeseriess = {
            'xPosition': [],
            'yPosition': [],
            'HealthPercent': [],
            'HeroDamage': [],
            'HeroHealing': [],
            'CreepDamage': [],
            'LastHits': [],
            'XP': [],
            'CurrentTime': []
        }
        self.isRadiant = False
        self.timestep = timestep
        self.saved_values = 0
        self.id = id
        self.hero_name = ""
        self.ability_priority = None

    def set_hero_name(self, hero_name):
        self.hero_name = hero_name
        #self.ability_priority = AbilityPriorityGradients(hero_name)

    def set_is_radiant(self, is_radiant):
        self.isRadiant = is_radiant

    def save_current_values(self):
        for key in self.keys:
            self.timeseriess[key].append(self.values[key])
        self.saved_values += 1

    def update_value(self, name, value):
        if name in self.values:
            self.values[name] = value
        elif name == "Team":
            self.isRadiant = value == "team2"
        elif name == "Position":
            splitValue = value.split(',')
            self.values['xPosition'] = splitValue[0]
            self.values['yPosition'] = splitValue[1]

    def update_ability(self, ability_name):
        if self.ability_priority is not None:
            self.ability_priority.add_ability_point(ability_name)

    def get_value_difference(self, key, index):
        timeSeries = self.timeseriess[key]

        return int(timeSeries[index + 1]) - int(timeSeries[index])


    def print_self(self):
        for key in self.keys:
            timeseries = self.timeseriess[key]
            i = 0
            for value in timeseries:
                print('player - {} field name - {}, value - {} at -  {}s'.format(self.playerId, key, value, i))
                i += self.timestep
