#maplestorybeta
import os
import random
from .maplestorybeta import character
os.system("clear")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-------MAPLESTORY-BETA-------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("--------------------------Made-by:-Jaemin-Ko---------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("")
print("")
print("")
print("")
choice = raw_input("press enter to continue ")
character = character(name, 1, 0, 0, 5, 5, 5, 5, 0, 0, False, 0, False, 0, False, 0, False, False, False):
os.system("clear")
playing = True
while playing:
    print("-----------------------------------------------------")
    print("--------------------Maple-Island---------------------")
    print("-----------------------------------------------------")
    print("-----------------------OPTIONS-----------------------")
    print("-----------------------------------------------------")
    print("1.Status---------------------------------------------")
    print("2.Hunt-----------------------------------------------")
    print("3.Quests---------------------------------------------")
    print("4.Store----------------------------------------------")
    print("5.Inventory------------------------------------------")
    print("6.Go-to-Victoria-Island------------------------------")
    print("7.Quit-Game------------------------------------------")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("")
    print("")
    print("")
    print("")
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
        character.check_level(False)
        level_str = str(character.level)
        damage_str = str(character.damage)
        experience_str = str(character.experience)
        strength_str = str(character.strength)
        dexterity_str = str(character.dexterity)
        luck_str = str(character.luck)
        intelligence_str = str(character.intelligence)
        status_point_str = str(character.status_point)
        if character.level < 10:
            level_str += "-"
        if character.status_point < 100:
            status_point_str += "-"
        if character.status_point < 10:
            status_pointstr += "-"
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
            strength_str += "-"
        if character.dexterity < 10:
            dexterity_str += "-"
        if character.luck < 10:
            luck_str += "-"
        if character.intelligence < 10:
            intelligence_str += "-"
        extra_space = ""
        if character.experience < 1000000000:
            extra_space += "-"
        if character.experience < 100000000:
            extra_space += "-"
        if character.experience < 10000000:
            extra_space += "-"
        if character.experience < 1000000:
            extra_space += "-"
        if character.experience < 100000:
            extra_space += "-"
        if character.experience < 10000:
            extra_space += "-"
        if character.experience < 1000:
            extra_space += "-"
        if character.experience < 100:
            extra_space += "-"
        if character.experience < 10:
            extra_space += "-"
        percentage = str(round(character.experience /(character.total_experience), 2))
        total_experiencestr = str(character.total_experience)
        if (character.total_experience) < 1000000000:
            total_experiencestr += "-"
        if (character.total_experience) < 100000000:
            total_experiencestr += "-"
        if (character.total_experience) < 10000000:
            total_experiencestr += "-"
        if (character.total_experience) < 1000000:
            total_experiencestr += "-"
        if (character.total_experience) < 100000:
            total_experiencestr += "-"
        if (character.total_experience) < 10000:
            total_experiencestr += "-"
        if (character.total_experience) < 1000:
            total_experiencestr += "-"
        if (character.total_experience) < 100:
            total_experiencestr += "-"
        if (character.total_experience) < 10:
            total_experiencestr += "-"
        os.system("clear")
        while status:
            print("-----------------------------------------------------")
            print("-----------------------STATUS------------------------")
            print("-----------------------------------------------------")
            print("level:-" + level_str + "------------" + percentage + "%----------------------------")
            print("experience:-" + experience_str + "/" + total_experience_str + "-------------------" + extra_space)
            print("1.STR:-" + strength_str + "--------------------------------------------")
            print("2.DEX:-" + dexterity_str + "--------------------------------------------")
            print("3.LUK:-" + luck_str + "--------------------------------------------")
            print("4.INT:-" + intelligence_str + "--------------------------------------------")
            print("-----------------------------------------------------")
            print("Avail.-sp:-" + status_point_str + "---------------------------------------")
            print("-----------------------------------------------------")
            print("damage:-" + damage_str + "-------------------------------------")
            print("-----------------------------------------------------")
            print("")
            print("")
            print("")
            print("")
            choice = raw_input("Press enter to go back ")
            os.system("clear")
            how_many = "How much do you want to increase by?"
            if points_entered <= character.status_point:
                if choice == "1":
                    character.increase_strength
                if choice == "2":
                    character.increase_dexterity
                if choice == "3":
                    character.increase_luck
                if choice == "4":
                    character.increase_intelligence
                else:
                    print("invalid")
            else:
                    print("invalid")
    if choice == "2":
        hunting = True
        os.system("clear")
        while hunting:
            print("-----------------------------------------------------")
            print("-----------------------Hunting-----------------------")
            print("-----------------------------------------------------")
            print("-----------------------OPTIONS-----------------------")
            print("-----------------------------------------------------")
            print("1.Hunt-Snails-(LV1-5)--------------------------------")
            print("2.Hunt-Slimes-and-stumps-(LV3-7)---------------------")
            print("3.Hunt-Pigs-(LV5-10)---------------------------------")
            print("4.Hunt-Mushrooms-(LV7-10)----------------------------")
            print("5.Back-----------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("")
            print("")
            print("")
            print("")
            character.calculate_damage
            choice = raw_input("Select ")
            if choice == "1":
                chance = random.randint(1, character.damage)
                if chance == 1:
                    character.death
                    choice = raw_input("please press enter to continue.")
                    hunting=False
                else:
                    randomInt = random.randint(1, 10)
                    if 1 <= randomInt <= 3:
                        chanceword = "small number"
                        experience += 1
                        if drkiller:
                            character.kills+= 2
                    if 4 <= randomInt <= 7:
                        chanceword = "lot"
                        experience += 2
                        if drkiller:
                            character.kills+= 3
                    if 8 <= randomInt <= 9:
                        chanceword = "bunch"
                        experience += 3
                        if drkiller:
                            character.kills+= 4
                    if randomInt == 10:
                        chanceword = "crap ton"
                        experience += 4
                        if drkiller:
                            character.kills+= 6
                    print("You defeated a " + chanceword + " of Snails.")
                    if 1 <= randomInt <= 3:
                        chanceword = "1"
                    if 4 <= randomInt <= 7:
                        chanceword = "2"
                    if 8 <= randomInt <= 9:
                        chanceword = "3"
                    if randomInt == 10:
                        chanceword = "4"
                    print("You got " + chanceword + " experience.")
                    character.check_level(True)
                    print("")
                    choice = raw_input("please press enter to continue.")
            if choice == "2":
                chance = random.randint(1, damage)
                if 1 <= chance <= 3:
                    character.death
                    choice = raw_input("please press enter to continue.")
                    hunting=False
                else:
                    randomInt = random.randint(1, 12)
                    if 1 <= randomInt <= 3:
                        chanceword = "small number"
                        experience += 2
                        if drkiller:
                            character.kills+= 2
                    if 4 <= randomInt <= 8:
                        chanceword = "lot"
                        experience += 5
                        if drkiller:
                            character.kills+= 3
                    if 9 <= randomInt <= 11:
                        chanceword = "bunch"
                        experience += 7
                        if drkiller:
                            character.kills+= 4
                    if randomInt == 12:
                        chanceword = "crap ton"
                        experience += 10
                        if drkiller:
                            character.kills+= 6
                    print("You defeated a " + chanceword + " of Slimes and Stumps.")
                    if 1 <= randomInt <= 3:
                        chanceword = "2"
                    if 4 <= randomInt <= 7:
                        chanceword = "5"
                    if 8 <= randomInt <= 9:
                        chanceword = "7"
                    if randomInt == 10:
                        chanceword = "10"
                    print("You got " + chanceword + " experience.")
                    character.check_level(True)
                    print("")
                    choice = raw_input("please press enter to continue.")
            if choice == "3":
                chance = random.randint(1, damage)
                if 1 <= chance <= 5:
                    character.death
                    choice = raw_input("please press enter to continue.")
                    hunting=False
                else:
                    randomInt = random.randint(1, 15)
                    if 1 <= randomInt <= 4:
                        chanceword = "small number"
                        experience += 5
                        if drkiller:
                            character.kills+= 2
                    if 5 <= randomInt <= 11:
                        chanceword = "lot"
                        experience += 9
                        if drkiller:
                            character.kills+= 3
                    if 12 <= randomInt <= 14:
                        chanceword = "bunch"
                        experience += 13
                        if drkiller:
                            character.kills+= 4
                    if randomInt == 15:
                        chanceword = "crap ton"
                        experience += 20
                        if drkiller:
                            character.kills+= 6
                    print("You defeated a " + chanceword + " of Pigs.")
                    if 1 <= randomInt <= 3:
                        chanceword = "1"
                    if 4 <= randomInt <= 7:
                        chanceword = "2"
                    if 8 <= randomInt <= 9:
                        chanceword = "3"
                    if randomInt == 10:
                        chanceword = "4"
                    print("You got " + chanceword + " experience.")
                    character.check_level(True)
                    print("")
                    choice = raw_input("please press enter to continue.")
            if choice == "4":
                chance = random.randint(1, damage)
                if 1 <= chance <= 9:
                    character.death
                    choice = raw_input("please press enter to continue.")
                    hunting=False
                else:
                    randomInt = random.randint(1, 20)
                    if 1 <= randomInt <= 6:
                        chanceword = "small number"
                        experience += 10
                        if drkiller:
                            character.kills+= 2
                    if 7 <= randomInt <= 15:
                        chanceword = "lot"
                        experience += 16
                        if drkiller:
                            character.kills+= 3
                    if 16 <= randomInt <= 19:
                        chanceword = "bunch"
                        experience += 24
                        if drkiller:
                            character.kills+= 4
                    if randomInt == 20:
                        chanceword = "crap ton"
                        experience += 30
                        if drkiller:
                            character.kills+= 6
                    print("You defeated a " + chanceword + " of Mushrooms")
                    if 1 <= randomInt <= 3:
                        chanceword = "10"
                    if 4 <= randomInt <= 7:
                        chanceword = "16"
                    if 8 <= randomInt <= 9:
                        chanceword = "24"
                    if randomInt == 10:
                        chanceword = "30"
                    print("You got " + chanceword + " experience.")
                    character.check_level(True)
                    print("")
                    choice = raw_input("please press enter to continue.")
            if choice == "5":
                hunting = False
            os.system("clear")
            else:
                os.system("clear")
    if choice == "3":
        os.system("clear")
        quest = True
        while quest:
            print("-----------------------------------------------------")
            print("-----------------------QUESTS------------------------")
            print("-----------------------------------------------------")
            print("-----------------------OPTIONS-----------------------")
            print("-----------------------------------------------------")
            print("1.Dr.Killer's-plan-(LV1+)----------------------------")
            print("2.Bob-the-Builder's-supplies-(LV3+)------------------")
            print("3.John-the-Butcher's-request-(LV5+)------------------")
            print("4.Back-----------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("")
            print("")
            print("")
            print("")
            choice = raw_input("Select ")
            if choice == "1":
                os.system("clear")
                if character.kills < 100 and character.dr_killer:
                    kills_str = str(kills)
                    if character.kills< 10:
                        kills_str = "-" + kills_str
                    print("-----------------------------------------------------")
                    print("---------------Dr.Killer's-plan-(LV1+)---------------")
                    print("-----------------------------------------------------")
                    print("-'You-didn't-finish-the-job!'------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("----------------kills:-" + kills_str + "/100------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("")
                    print("")
                    print("")
                    print("")
                    choice == raw_input("Press enter.")
                if character.kills >= 100 and dr_killer:
                    print("-----------------------------------------------------")
                    print("---------------Dr.Killer's-plan-(LV1+)---------------")
                    print("-----------------------------------------------------")
                    print("-'Hmm...-Nothing-changed...'-------------------------")
                    print("-'Maybe-this-is-impossible...'-----------------------")
                    print("-'No!!!-I-will-not-give-up!!!'-----------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("----------------Reward:-2000-mesos-------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("")
                    print("")
                    print("")
                    print("")
                    character.dr_killer= False
                    meso += 2000
                    character.kills= 0
                else:
                    print("-----------------------------------------------------")
                    print("---------------Dr.Killer's-plan-(LV1+)---------------")
                    print("-----------------------------------------------------")
                    print("-'Hello.-My-name-is-Dr.Killer.'----------------------")
                    print("-'I-want-to-exterminate-all-monsters-in-maplestory'--")
                    print("-'I-believe-there-is-an-end-to-monsters'-spawning.'--")
                    print("-'Please-help-me.-I-will-give-you-a-great-reward.'---")
                    print("-----------------------------------------------------")
                    print("----------------*Kill-100-monsters-------------------")
                    print("----------------Reward:-1000-mesos-------------------")
                    print("-----------------------------------------------------")
                    print("-----------1.-Accept-----------2.-Decline------------")
                    print("-----------------------------------------------------")
                    print("")
                    print("")
                    print("")
                    print("")
                    choice = raw_input("Select ")
                    if choice == "1":
                        character.dr_killer= True
            if choice == "2":
                os.system("clear")
                if character.branch< 30 and character.bob_the_builder:
                    branch_str = branch
                    if character.branch< 10:
                        branch_str = "-" + branch_str
                    print("-----------------------------------------------------")
                    print("----------Bob-the-Builder's-supplies-(LV3+)----------")
                    print("-----------------------------------------------------")
                    print("-'Hmm..-I-don't-think-you-got-all-the-supplies.'-----")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-------------branches:-" + branch_str + "/30------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("")
                    print("")
                    print("")
                    print("")
                if character.branch>= 30 and character.bob_the_builder:
                    print("-----------------------------------------------------")
                    print("----------Bob-the-Builder's-supplies-(LV3+)----------")
                    print("-----------------------------------------------------")
                    print("-'Can-we-fix-it?'------------------------------------")
                    print("-'Yes-we-can!!!'-------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("--*30-branches-have-been-taken-from-your-inventory.--")
                    print("----------------Reward:-3000-mesos-------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("")
                    print("")
                    print("")
                    print("")
                    character.bob_the_builder = False
                    meso += 3000
                    character.branch= 0
                    choice = raw_input("Press enter.")
                else:
                    print("-----------------------------------------------------")
                    print("----------Bob-the-Builder's-supplies-(LV3+)----------")
                    print("-----------------------------------------------------")
                    print("-'Howdie!'-------------------------------------------")
                    print("-'I'm-fix-my-house!'---------------------------------")
                    print("-'But-I'm-in-need-of-some-supplies.'-----------------")
                    print("-'Wanna-give-me-a-hand?'-----------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------*Get-30-branches--------------------")
                    print("----------------Reward:-3000-mesos-------------------")
                    print("-----------------------------------------------------")
                    print("-----------1.-Accept-----------2.-Decline------------")
                    print("-----------------------------------------------------")
                    print("")
                    print("")
                    print("")
                    print("")
                    choice = raw_input("Select ")
                    if choice == "1":
                        character.bob_the_builder = True
            if choice == "3":
                os.system("clear")
                if pigmeat < 20 and johnthebutcher:
                    pigmeatstr = str(pigmeat)
                    if pigmeat < 10:
                        pigmeatstr = "-" + pigmeatstr
                    print("-----------------------------------------------------")
                    print("---------John-the-Butcher's-request-(LV5-10)---------")
                    print("-----------------------------------------------------")
                    print("-'Hey!-I-don't-think-you-got-what-I've-asked-ya!'----")
                    print("-'Yea-you!!!'----------------------------------------")
                    print("-'Go-get-me-some-pigmeat!'---------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("------------pigmeat:-" + pigmeatstr + "/20--------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("")
                    print("")
                    print("")
                    print("")
                    character.bob_the_builder = False
                    choice = raw_input("Press enter.")
                if pigmeat >= 20 and character.bob_the_builder:
                    print("-----------------------------------------------------")
                    print("---------John-the-Butcher's-request-(LV5-10)---------")
                    print("-----------------------------------------------------")
                    print("-'Alrightttt~'---------------------------------------")
                    print("-'Thanks-buddy.'-------------------------------------")
                    print("-'Here's-some-mesos'---------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("--*20-pigmeat-have-been-taken-from-your-inventory.---")
                    print("----------------Reward:-5000-mesos-------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("")
                    print("")
                    print("")
                    print("")
                    johnthebutcher = False
                    pigmeat = 0
                    meso += 5000
                    choice = raw_input("Press enter.")
                else:
                    print("-----------------------------------------------------")
                    print("---------John-the-Butcher's-request-(LV5-10)---------")
                    print("-----------------------------------------------------")
                    print("-'Hey,-buddy!!'--------------------------------------")
                    print("-'Yea-you!!!'----------------------------------------")
                    print("-'Go-get-me-some-pigmeat!'---------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("------------------*Get-20-pigmeat--------------------")
                    print("----------------Reward:-5000-mesos-------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("")
                    print("")
                    print("")
                    print("")
                    choice = raw_input("Press enter.")
                    if choice == "1":
                        johnthebutcher = True
                os.system("clear")
            if choice == "4":
                quest = False
                os.system("clear")
            else:
                os.system("clear")
    if choice == "4":
        store = True
        os.system("clear")
        while store:
            print("-----------------------------------------------------")
            print("------------------------STORE------------------------")
            print("-----------------------------------------------------")
            print("----------------------ITEM-LIST----------------------")
            print("-----------------------------------------------------")
            print("1.Beginner's-sword-(Lv1)--------[atk+3]----2000-mesos")
            print("2.Razor-Blade-(Lv5)----[str+2]--[atk+6]----5000-mesos")
            print("3.Maple-Axe---(Lv8)----[st +5]-[atk+10]---10000-mesos")
            print("4.Back-----------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("")
            print("")
            print("")
            print("")
            choice = raw_input("Select: ")
            if choice == "1":
                character.get_sword1
            if choice == "2":
                character.get_blade1
            if choice == "3":
                character.get_axe1
            if choice == "4":
                store = False
                os.system("clear")
            else:
                os.system("clear")
    else:
        os.system("clear")
