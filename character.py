class character:
    def __init__(self, name, level, status_point, experience, strength, dexterity, luck, intelligence, damage, meso, weapon_attack, weapon_strength, dr_killer, kills, bob_the_builder, branch, john_the_butcher, pig_meat, playing, status, hunting, quest, store, sword1, blade1, axe1):
        self.name = name
        self.level = level
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
    def experience_loss_by_death(self):
        if self.experience < 10:
            print("You lost "+str(self.experience)+" exp.")
            self.experience = 0
        if self.experience >= 10:
            print("You lost "+str(self.experience)+" exp.")
            self.experience -= 10
        else:
            return experience
    def death(self):
        print("you died...")
        print("")
        experience_loss_by_death(self)
    def increase_experience(self, experience_gained):
        self.experience += experience_gained
    def increase_meso(self, meso_earned):
        self.meso +=meso_earned
    def check_level(self, hunting):
        while self.experience > (self.level**2 + 2 * self.level):
            self.experience -= (self.level**2 + 2 * self.level)
            self.level += 1
            self.status_point += 5
            if hunting:
                print("You leveled up!!!")
                print("Now you're LV "+str(self.level)+"!")
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
        self.damage = self.strength + self.weapon_strength + self.weapon_strength + (self.dexterity-(self.dexterity%2))/2 + self.level
    def total_experience(self):
        return (self.level**2 + 2 * self.level)
    def add_weapon_stat(self):
        if self.sword1 = True:
            self.weapon_attack = 3
        if self.blade1 = True:
            self.weapon_attack = 6
            self.weapon_strength = 2
        if self.axe1 = True:
            self.weapon_attack = 10
            self.weapon_strength = 5
