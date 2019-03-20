import pickle


class AbilityPriorityGradients:
    def __init__(self, hero_name):
        self.ability_gradients = {}
        self.talent_selection = {}
        with open('abilityAndTalentList.pickle', 'rb') as handle:
            abilityList = pickle.load(handle)
        self.my_abilities = list(filter(lambda name: not name.startswith('special_bonus'), abilityList[hero_name]))
        self.my_talents = list(filter(lambda name: name.startswith('special_bonus'), abilityList[hero_name]))
        for ability in self.my_abilities:
            self.ability_gradients.update({ability: []})
        for talent in self.my_talents:
            self.talent_selection.update({talent: 0})
        self.current_level = 0

    def add_ability_point(self, ability_name):
        if ability_name in self.my_abilities:
            self.current_level += 1
            this_ability_gradients = self.ability_gradients[ability_name]
            points_so_far = len(this_ability_gradients) + 1
            this_ability_gradients.append(points_so_far / self.current_level)
        elif ability_name in self.my_talents:
            self.talent_selection[ability_name] = 1

    def pad_ability_gradients(self, ability_name):
        this_ability_gradients = self.ability_gradients[ability_name]
        while len(this_ability_gradients) < 4:
            this_ability_gradients.append(this_ability_gradients[-1])

    def get_ability_priority(self):
        for ability in self.my_abilities:
            points_in_ability = len(self.ability_gradients[ability])
            if points_in_ability == 0:
                self.ability_gradients[ability] = [0] * 4
            elif points_in_ability < 4:
                self.pad_ability_gradients(ability)

        return {
            'ability_gradients': self.ability_gradients,
            'talent_selection': self.talent_selection
        }
