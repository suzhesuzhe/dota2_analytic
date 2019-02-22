class FieldsToTrack:
    fieldsToTrack = {
        'Position': False,
        'HealthPercent': False,
        'HeroDamage': False,
        'HeroHealing': False,
        'CreepDamage': False,
        'LastHits': False,
        'XP': False,
        'CurrentTime': False
    }
    
    def track_all(self):
        for key in self.fieldsToTrack.keys():
            self.fieldsToTrack[key] = True
        return self

    def track_position(self):
        self.fieldsToTrack.Position = True
        return self

    def track_health_percent(self):
        self.fieldsToTrack.HealthPercent = True
        return self

    def track_hero_damage(self):
        self.fieldsToTrack.HeroDamage = True
        return self

    def track_hero_healing(self):
        self.fieldsToTrack.HeroHealing = True
        return self

    def track_creep_damage(self):
        self.fieldsToTrack.CreepDamage = True
        return self

    def track_last_hits(self):
        self.fieldsToTrack.LastHits = True
        return self

    def track_XP(self):
        self.fieldsToTrack.XP = True
        return self

    def track_current_time(self):
        self.fieldsToTrack.CurrentTime = True
        return self

    def get_dictionary(self):
        return self.fieldsToTrack