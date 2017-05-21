#maplestorybeta
import os
import random
from character import Character
from display import Display
os.system("clear")
display = Display
display.opening()
choice = raw_input("Press enter ")
character = Character( 1, 50, 50, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, False, 0, False, 0, False, 0, False, False, False, 0)
os.system("clear")
playing = True
while playing:
    display.maple_island()
    choice = raw_input("Select: ")
    if choice == "7":
        print("Are you sure? Your progress will not be saved.")
        choice = raw_input("type 1 to quit ")
        if choice == "1":
            os.system("clear")
            print("Thank you for playing.")
            break
        os.system("clear")
    if choice == "1":
        status = True
        os.system("clear")
        while status:
            extra_space1 = ""
            extra_space2 = ""
            extra_space3 = ""
            extra_space4 = ""
            character.check_level(False)
            character.calculate_damage()
            level_str = str(character.level)
            health_point_str = str(character.health_point)
            mana_point_str = str(character.mana_point)
            health_point_max_str = str(character.health_point_max())
            mana_point_max_str = str(character.mana_point_max())
            damage_str = str(character.damage)
            experience_str = str(character.experience)
            total_experience_str = str(character.total_experience())
            strength_str = str(character.strength)
            weapon_strength_str = str(character.weapon_strength)
            dexterity_str = str(character.dexterity)
            luck_str = str(character.luck)
            intelligence_str = str(character.intelligence)
            status_point_str = str(character.status_point)
            if character.level < 10:
                level_str += "-"
            if character.status_point < 100:
                status_point_str += "-"
            if character.status_point < 10:
                status_point_str += "-"
            if character.damage < 10000000:
                damage_str += "-"
            if character.damage < 1000000:
                damage_str += "-"
            if character.damage < 100000:
                damage_str += "-"
            if character.damage < 10000:
                damage_str += "-"
            if character.damage < 1000:
                damage_str += "-"
            if character.damage < 100:
                damage_str += "-"
            if character.damage < 10:
                damage_str += "-"
            if character.strength < 10:
                extra_space4 += "-"
            if character.weapon_strength == 0:
                weapon_strength_str = "----"
            if character.weapon_strength > 0:
                weapon_strength_str = "(+" + weapon_strength_str + ")"
            if character.weapon_strength < 10:
                weapon_strength_str += "-"
            if character.dexterity < 10:
                dexterity_str += "-"
            if character.luck < 10:
                luck_str += "-"
            if character.intelligence < 10:
                intelligence_str += "-"
            if character.health_point < 1000:
                extra_space1 += "-"
            if character.health_point < 100:
                extra_space1 += "-"
            if character.health_point < 10:
                extra_space1 += "-"
            if character.mana_point < 1000:
                extra_space1 += "-"
            if character.mana_point < 100:
                extra_space1 += "-"
            if character.mana_point < 10:
                extra_space1 += "-"
            if character.experience < 1000000000:
                extra_space3 += "-"
            if character.experience < 100000000:
                extra_space3 += "-"
            if character.experience < 10000000:
                extra_space3 += "-"
            if character.experience < 1000000:
                extra_space3 += "-"
            if character.experience < 100000:
                extra_space3 += "-"
            if character.experience < 10000:
                extra_space3 += "-"
            if character.experience < 1000:
                extra_space3 += "-"
            if character.experience < 100:
                extra_space3 += "-"
            if character.experience < 10:
                extra_space3 += "-"
            percentage = str(round(character.experience/(character.total_experience()),2))
            if character.total_experience() < 1000000000:
                total_experience_str += "-"
            if character.total_experience() < 100000000:
                total_experience_str += "-"
            if character.total_experience() < 10000000:
                total_experience_str += "-"
            if character.total_experience() < 1000000:
                total_experience_str += "-"
            if character.total_experience() < 100000:
                total_experience_str += "-"
            if character.total_experience() < 10000:
                total_experience_str += "-"
            if character.total_experience() < 1000:
                total_experience_str += "-"
            if character.total_experience() < 100:
                total_experience_str += "-"
            if character.total_experience() < 10:
                total_experience_str += "-"
            print("-----------------------------------------------------")
            print("-----------------------STATUS------------------------")
            print("-----------------------------------------------------")
            print("level:" + level_str + "------------" + percentage + "%-----------------------------")
            print("EXP:" + experience_str + "/" + total_experience_str + "----------------------------" + extra_space3)
            print("HP:"+health_point_str+"/"+health_point_max_str+extra_space1+"-MP:"+mana_point_str+"/"+mana_point_max_str+extra_space2+"--------------------------------")
            print("1.STR:" + strength_str + "-"+weapon_strength_str+"---------------------------------------" + extra_space4)
            print("2.DEX:" + dexterity_str + "---------------------------------------------")
            print("3.LUK:" + luck_str + "---------------------------------------------")
            print("4.INT:" + intelligence_str + "---------------------------------------------")
            print("Avail.-sp:" + status_point_str + "----------------------------------------")
            print("-----------------------------------------------------")
            print("damage:-" + damage_str + "-------------------------------------")
            print("-----------------------------------------------------")
            print("")
            print("")
            choice = raw_input("Choose 1-4 to increase stats. Or press enter to exit. ")
            if choice == "":
                status = False
                os.system("clear")
            elif choice == "1" or "2" or "3" or "4":
                how_many = int(input("How much do you want to increase by?"))
                if how_many <= character.status_point and how_many > 0:
                    if choice == "1":
                        character.increase_strength(how_many)
                    if choice == "2":
                        character.increase_dexterity(how_many)
                    if choice == "3":
                        character.increase_luck(how_many)
                    if choice == "4":
                        character.increase_intelligence(how_many)
                    os.system("clear")
                else:
                    print("invalid")
                    choice = raw_input("Press enter")
                    os.system("clear")
            else:
                print("invalid")
                choice = raw_input("Press enter")
                os.system("clear")
    elif choice == "2":
        hunting = True
        os.system("clear")
        meso_earned = 0
        while hunting:
            display.hunting(character.health_point, character.mana_point)
            character.calculate_damage()
            choice = raw_input("Select ")
            if choice == "1":
                chance = random.randint(1, character.damage)
                if chance == 1:
                    character.death()
                    hunting=False
                else:
                    randomInt = random.randint(1, 10)
                    if 1 <= randomInt <= 3:
                        chance_word = "small number"
                        character.experience += 1
                        if character.dr_killer:
                            character.kills+= 2
                    if 4 <= randomInt <= 7:
                        chance_word = "lot"
                        character.experience += 2
                        if character.dr_killer:
                            character.kills+= 3
                    if 8 <= randomInt <= 9:
                        chance_word = "bunch"
                        character.experience += 3
                        if character.dr_killer:
                            character.kills+= 4
                    if randomInt == 10:
                        chance_word = "crap ton"
                        character.experience += 4
                        if character.dr_killer:
                            character.kills+= 6
                    print("You defeated a " + chance_word + " of Snails.")
                    if 1 <= randomInt <= 3:
                        chance_word = "1"
                    if 4 <= randomInt <= 7:
                        chance_word = "2"
                    if 8 <= randomInt <= 9:
                        chance_word = "3"
                    if randomInt == 10:
                        chance_word = "4"
                    meso_earned = (50 + randomInt * 30)
                    random_health_loss= random.randint(0, character.health_point_max() - character.dexterity)
                    character.health_point -= random_health_loss
                    print("your health went down by "+str(random_health_loss)+".")
                    print("You got " + chance_word + " exp and " + str(meso_earned)+ " mesos.")
                    character.meso += meso_earned
                    character.check_level(True)
                    character.check_health_point()
                choice = raw_input("Press enter to continue.")
            elif choice == "2":
                chance = random.randint(1, character.damage)
                if 1 <= chance <= 3:
                    character.death()
                    hunting=False
                else:
                    randomInt = random.randint(1, 12)
                    if 1 <= randomInt <= 3:
                        chance_word = "small number"
                        character.experience += 2
                        if character.dr_killer:
                            character.kills+= 2
                    if 4 <= randomInt <= 8:
                        chance_word = "lot"
                        character.experience += 5
                        if character.dr_killer:
                            character.kills+= 3
                    if 9 <= randomInt <= 11:
                        chance_word = "bunch"
                        character.experience += 7
                        if character.dr_killer:
                            character.kills+= 4
                    if randomInt == 12:
                        chance_word = "crap ton"
                        character.experience += 10
                        if character.dr_killer:
                            character.kills+= 6
                    print("You defeated a " + chance_word + " of Slimes and Stumps.")
                    if 1 <= randomInt <= 3:
                        chance_word = "2"
                        if character.bob_the_builder:
                            character.branch += 1
                    if 4 <= randomInt <= 7:
                        chance_word = "5"
                        if character.bob_the_builder:
                            character.branch += 2
                    if 8 <= randomInt <= 9:
                        chance_word = "7"
                        if character.bob_the_builder:
                            character.branch += 3
                    if randomInt == 10:
                        chance_word = "10"
                        if character.bob_the_builder:
                            character.branch += 4
                    meso_earned = (100 + randomInt * 60)
                    random_health_loss= random.randint(0, character.health_point_max() - character.dexterity)
                    character.health_point -= random_health_loss
                    print("your health went down by "+str(random_health_loss)+".")
                    print("You got " + chance_word + " exp and " + str(meso_earned)+ " mesos.")
                    character.meso += meso_earned
                    character.check_level(True)
                    character.check_health_point()
                choice = raw_input("Press enter to continue.")
            elif choice == "3":
                chance = random.randint(1, character.damage)
                if 1 <= chance <= 5:
                    character.death()
                    hunting=False
                else:
                    randomInt = random.randint(1, 15)
                    if 1 <= randomInt <= 4:
                        chance_word = "small number"
                        character.experience += 5
                        if character.dr_killer:
                            character.kills+= 2
                    if 5 <= randomInt <= 11:
                        chance_word = "lot"
                        character.experience += 9
                        if character.dr_killer:
                            character.kills+= 3
                    if 12 <= randomInt <= 14:
                        chance_word = "bunch"
                        character.experience += 13
                        if character.dr_killer:
                            character.kills+= 4
                    if randomInt == 15:
                        chance_word = "crap ton"
                        character.experience += 20
                        if character.dr_killer:
                            character.kills+= 6
                    print("You defeated a " + chance_word + " of Pigs.")
                    if 1 <= randomInt <= 3:
                        chance_word = "1"
                    if 4 <= randomInt <= 7:
                        chance_word = "2"
                        if character.john_the_butcher:
                            character.pig_meat += 1
                    if 8 <= randomInt <= 9:
                        chance_word = "3"
                        if character.john_the_butcher:
                            character.pig_meat += 2
                    if randomInt == 10:
                        chance_word = "4"
                        if character.john_the_butcher:
                            character.pig_meat += 3
                    meso_earned = (200 + randomInt * 100)
                    random_health_loss= random.randint(0, character.health_point_max() - character.dexterity)
                    character.health_point -= random_health_loss
                    print("your health went down by "+str(random_health_loss)+".")
                    print("You got " + chance_word + " exp and " + str(meso_earned)+ " mesos.")
                    character.meso += meso_earned
                    character.check_level(True)
                    character.check_health_point()
                choice = raw_input("Press enter. ")
            elif choice == "4":
                chance = random.randint(1, character.damage)
                if 1 <= chance <= 9:
                    character.death()
                    hunting=False
                else:
                    randomInt = random.randint(1, 20)
                    if 1 <= randomInt <= 6:
                        chance_word = "small number"
                        character.experience += 10
                        if character.dr_killer:
                            character.kills+= 2
                    if 7 <= randomInt <= 15:
                        chance_word = "lot"
                        character.experience += 16
                        if character.dr_killer:
                            character.kills+= 3
                    if 16 <= randomInt <= 19:
                        chance_word = "bunch"
                        character.experience += 24
                        if character.dr_killer:
                            character.kills+= 4
                    if randomInt == 20:
                        chance_word = "crap ton"
                        character.experience += 30
                        if character.dr_killer:
                            character.kills+= 6
                    print("You defeated a " + chance_word + " of Mushrooms")
                    if 1 <= randomInt <= 3:
                        chance_word = "10"
                    if 4 <= randomInt <= 7:
                        chance_word = "16"
                    if 8 <= randomInt <= 9:
                        chance_word = "24"
                    if randomInt == 10:
                        chance_word = "30"
                    meso_earned = (250 + randomInt * 150)
                    random_health_loss= random.randint(0, character.health_point_max() - character.dexterity)
                    character.health_point -= random_health_loss
                    print("your health went down by "+str(random_health_loss)+".")
                    print("You got " + chance_word + " exp and " + str(meso_earned)+ " mesos.")
                    character.meso += meso_earned
                    character.check_level(True)
                    character.check_health_point()
                choice = raw_input("Press enter. ")
            elif choice == "5":
                if character.red_potion > 0:
                    character.red_potion +- 1
                    character.health_point += 50
                else :
                    print("You don't have any.")
            elif choice == "6":
                hunting = False
            os.system("clear")
    elif choice == "3":
        os.system("clear")
        quest = True
        while quest:
            display.quest()
            choice = raw_input("Select ")
            if choice == "1":
                os.system("clear")
                if character.kills < 100 and character.dr_killer:
                    display.dr_killer_incomplete(character.kills)
                    choice == raw_input("Press enter.")
                elif character.kills >= 100 and character.dr_killer:
                    display.dr_killer_completed()
                    character.dr_killer= False
                    character.meso += 2000
                    character.kills= 0
                else:
                    display.dr_killer_quest()
                    choice = raw_input("Select ")
                    if choice == "1":
                        character.dr_killer= True
                os.system("clear")
            elif choice == "2":
                os.system("clear")
                if character.branch< 30 and character.bob_the_builder:
                    display.bob_the_builder_incomplete(character.branch)
                elif character.branch>= 30 and character.bob_the_builder:
                    display.bob_the_builder_completed()
                    character.bob_the_builder = False
                    character.meso += 3000
                    character.branch= 0
                    choice = raw_input("Press enter.")
                else:
                    display.bob_the_builder_quest()
                    choice = raw_input("Select ")
                    if choice == "1":
                        character.bob_the_builder = True
                os.system("clear")
            elif choice == "3":
                os.system("clear")
                if character.pig_meat < 20 and character.john_the_butcher:
                    john_the_butcher_incomplete(character.pig_meat)
                    character.bob_the_builder = False
                    choice = raw_input("Press enter. ")
                elif character.pig_meat >= 20 and character.bob_the_builder:
                    display.john_the_butcher_completed()
                    character.john_the_butcher = False
                    character.pig_meat = 0
                    character.meso += 5000
                    choice = raw_input("Press enter. ")
                else:
                    display.john_the_butcher_quest()
                    choice = raw_input("Press enter. ")
                    if choice == "1":
                        character.john_the_butcher = True
                os.system("clear")
            elif choice == "4":
                quest = False
                os.system("clear")
            else:
                os.system("clear")
    elif choice == "4":
        store = True
        os.system("clear")
        while store:
            display.store()
            choice = raw_input("Select: ")
            if choice == "1":
                if character.sword1:
                    print("You already have that weapon.")
                elif character.meso >= 2000 and character.sword1 == False:
                    character.sword1 = True
                    character.meso -= 2000
                    character.add_weapon_stat
                    print("You have bought the item.")
                else:
                    print("Not enough mesos.")
                choice == raw_input("Press enter.")
                os.system("clear")
            elif choice == "2":
                if character.blade1:
                    print("You already have that weapon.")
                elif character.meso >= 5000 and character.blade1 == False:
                    character.blade1 = True
                    character.meso -= 5000
                    character.add_weapon_stat
                    print("You have bought the item.")
                else:
                    print("Not enough mesos.")
                choice == raw_input("Press enter. ")
                os.system("clear")
            elif choice == "3":
                if character.axe1:
                    print("You already have that weapon.")
                elif character.meso >= 10000 and character.axe1 == False:
                    character.axe1 = True
                    character.meso -= 10000
                    character.add_weapon_stat
                    print("You have bought the item.")
                else:
                    print("Not enough mesos.")
                choice == raw_input("Press enter. ")
                os.system("clear")
            elif choice == "4":
                how_many = int(input("How many? "))
                if character.meso > (how_many * 100):
                    character.meso -= (how_many * 100)
                    character.red_potion += how_many
                    print("You bought " + str(how_many) + " Red potions.")
                else:
                    print("Not enough mesos.")
                choice == raw_input("Press enter. ")
                os.system("clear")
            elif choice == "5":
                store = False
                os.system("clear")
            else:
                os.system("clear")
    elif choice == "5":
        os.system("clear")
        extra_space5 = ""
        extra_space6 = ""
        sword1_str = ""
        blade1_str = ""
        axe1_str = ""
        red_potion_str = "--------------"
        branch_str = ""
        pig_meat_str = ""
        meso_str = str(character.meso)
        if character.meso < 1000000:
            meso_str +="-"
        if character.meso < 100000:
            meso_str +="-"
        if character.meso < 10000:
            meso_str +="-"
        if character.meso < 1000:
            meso_str +="-"
        if character.meso < 100:
            meso_str +="-"
        if character.meso < 10:
            meso_str +="-"
        if character.sword1 == True:
            sword1_str = "Beginner's-sword"
        else:
            extra_space5 += "----------------"
        if character.blade1 == True:
            blade1_str = "Razor-Blade"
        else:
            extra_space5 += "-----------"
        if character.axe1 == True:
            axe1_str = "Maple-Axe"
        else:
            extra_space5 +="---------"
        if character.red_potion > 0:
            red_potion_str = "Red-potion-x"+str(character.red_potion)
            if character.red_potion < 10:
                red_potion_str += "-"
        if character.branch == 0:
            extra_space6 += "---------"
        if character.pig_meat == 0:
            extra_space6 += "----------"
        if character.branch > 0:
            branch_str = "Branch-x"+str(character.branch)
            if character.branch < 10:
                    extra_space6 += "-"
        if character.pig_meat > 0:
            pig_meat_str = "Pig-meat-x"+str(character.pig_meat)
            if character.pig_meat < 10:
                    extra_space6 += "-"
        print("-----------------------------------------------------")
        print("----------------------Inventory----------------------")
        print("-EQUIP-----------------------------------------------")
        print("-"+sword1_str+"-"+blade1_str+"-"+axe1_str+"--------------"+extra_space5)
        print("-----------------------------------------------------")
        print("-USE-------------------------------------------------")
        print("-"+red_potion_str+"--------------------------------------")
        print("-----------------------------------------------------")
        print("-ETC-------------------------------------------------")
        print("-"+branch_str+"-"+pig_meat_str+"--------------------------------"+extra_space6)
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-MESO:"+meso_str+"----------------------------------------")
        print("-----------------------------------------------------")
        print("")
        print("")
        choice = raw_input("Press enter to go back. ")
        os.system("clear")
    elif choice == "6":
        os.system("clear")
        print("HA. Nice try. This is a beta version.")
        choice == raw_input("Press enter to go back ")
        os.system("clear")
    else:
        os.system("clear")
