class Character(object):
    def __init__(self, level, health_point, mana_point, status_point, experience, strength, dexterity, luck, intelligence, damage, meso, weapon_attack, weapon_strength, dr_killer, kills, bob_the_builder, branch, john_the_butcher, pig_meat, sword1, blade1, axe1, red_potion):
        self.level = level
        self.health_point = health_point
        self.mana_point = mana_point
        self.status_point = status_point
        self.experience = experience
        self.strength = strength
        self.dexterity = dexterity
        self.luck = luck
        self.intelligence = intelligence
        self.damage = damage
        self.meso = meso
        self.weapon_attack = weapon_attack
        self.weapon_strength = weapon_strength
        self.dr_killer = dr_killer
        self.kills = kills
        self.bob_the_builder = bob_the_builder
        self.branch = branch
        self.john_the_butcher =john_the_butcher
        self.pig_meat = pig_meat
        self.sword1 = sword1
        self.blade1 = blade1
        self.axe1 = axe1
        self.red_potion = red_potion
    def experience_loss_by_death(self):
        if self.experience < 10:
            print("You lost "+str(self.experience)+" exp.")
            self.experience = 0
        elif self.experience >= 10:
            print("You lost "+str(self.experience)+" exp.")
            self.experience -= 10
    def death(self):
        print("you died...")
        self.health_point = 50
        self.mana_point = 50
        self.experience_loss_by_death()
    def health_point_max(self):
        return (50 + (self.level - 1) * 20)
    def mana_point_max(self):
        return(50 + (self.level - 1) * 20)
    def check_level(self, hunting):
        while self.experience >= (self.level**2 + 2 * self.level):
            self.experience -= (self.level**2 + 2 * self.level)
            self.level += 1
            self.status_point += 2
            self.health_point = self.health_point_max()
            self.mana_point = self.mana_point_max()
            if hunting:
                print("You leveled up!!! Now you're LV "+str(self.level)+"!")
    def increase_strength(self, point):
        self.strength += point
        self.status_point -= point
    def increase_dexterity(self, point):
        self.dexterity += point
        self.status_point -= point
    def increase_luck(self, point):
        self.luck += point
        self.status_point -= point
    def increase_intelligence(self, point):
        self.intelligence += point
        self.status_point -= point
    def calculate_damage(self):
        dexterity_temp = self.dexterity
        if self.dexterity%2 == 1:
            dexterity_temp -=1
        dexterity_temp = int(dexterity_temp/2)
        self.damage = self.strength + self.weapon_attack + self.weapon_strength + dexterity_temp + self.level
    def total_experience(self):
        return (self.level**2 + 2 * self.level)
    def add_weapon_stat(self):
        if self.sword1:
            self.weapon_attack = 3
        if self.blade1:
            self.weapon_attack = 5
            self.weapon_strength = 2
        if self.axe1:
            self.weapon_attack = 8
            self.weapon_strength = 4
    def check_health_point(self):
        if self.health_point < 0:
            self.death()
