class Display(object):
    def __init__(self):
        None
    @staticmethod
    def opening():
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
    @staticmethod
    def maple_island():
        print("-----------------------------------------------------")
        print("-------------------[Maple-Island]--------------------")
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
    @staticmethod
    def hunting(health_point, mana_point):
        print("-----------------------------------------------------")
        print("----------------------[Hunting]----------------------")
        print("-----------------------------------------------------")
        print("-----------------------OPTIONS-----------------------")
        print("-----------------------------------------------------")
        print("1.Hunt-Snails-(LV1-5)--------------------------------")
        print("2.Hunt-Slimes-and-stumps-(LV3-7)---------------------")
        print("3.Hunt-Pigs-(LV5-10)---------------------------------")
        print("4.Hunt-Mushrooms-(LV7-10)----------------------------")
        print("5.Use-Red-Potion-------------------------------------")
        print("6.Back-----------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("")
        print("HP: " + str(health_point) + " MP: " + str(mana_point))
    @staticmethod
    def quest():
        print("-----------------------------------------------------")
        print("----------------------[QUESTS]-----------------------")
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
        print("-----------------------------------------------------")
        print("")
        print("")
    @staticmethod
    def dr_killer_incomplete(kills):
        kills_str = str(kills)
        if kills< 10:
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
        print("-----------------------------------------------------")
        print("----------------kills:-" + kills_str + "/100------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("")
        print("")
    @staticmethod
    def dr_killer_completed():
        print("-----------------------------------------------------")
        print("---------------Dr.Killer's-plan-(LV1+)---------------")
        print("-----------------------------------------------------")
        print("-'Hmm...-Nothing-changed...'-------------------------")
        print("-'Maybe-this-is-impossible...'-----------------------")
        print("-'No!!!-I-will-not-give-up!!!'-----------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("----------------Reward:-2000-mesos-------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("")
        print("")
    @staticmethod
    def dr_killer_quest():
        print("-----------------------------------------------------")
        print("---------------Dr.Killer's-plan-(LV1+)---------------")
        print("-----------------------------------------------------")
        print("-'Hello.-My-name-is-Dr.Killer.'----------------------")
        print("-'I-want-to-exterminate-all-monsters-in-maplestory'--")
        print("-'I-believe-there-is-an-end-to-monsters'-spawning.'--")
        print("-'Please-help-me.-I-will-give-you-a-great-reward.'---")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("----------------*Kill-100-monsters-------------------")
        print("----------------Reward:-1000-mesos-------------------")
        print("-----------------------------------------------------")
        print("-----------1.-Accept-----------2.-Decline------------")
        print("-----------------------------------------------------")
        print("")
        print("")
    @staticmethod
    def bob_the_builder_incomplete(branch):
        branch_str = str(branch)
        if branch< 10:
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
        print("-----------------------------------------------------")
        print("-------------branches:-" + branch_str + "/30------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("")
        print("")
    @staticmethod
    def bob_the_builder_completed():
        print("-----------------------------------------------------")
        print("----------Bob-the-Builder's-supplies-(LV3+)----------")
        print("-----------------------------------------------------")
        print("-'Can-we-fix-it?'------------------------------------")
        print("-'Yes-we-can!!!'-------------------------------------")
        print("-----------------------------------------------------")
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
    @staticmethod
    def bob_the_builder_quest():
        print("-----------------------------------------------------")
        print("----------Bob-the-Builder's-supplies-(LV3+)----------")
        print("-----------------------------------------------------")
        print("-'Howdie!'-------------------------------------------")
        print("-'I'm-fix-my-house!'---------------------------------")
        print("-'But-I'm-in-need-of-some-supplies.'-----------------")
        print("-'Wanna-give-me-a-hand?'-----------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------*Get-30-branches--------------------")
        print("----------------Reward:-3000-mesos-------------------")
        print("-----------------------------------------------------")
        print("-----------1.-Accept-----------2.-Decline------------")
        print("-----------------------------------------------------")
        print("")
        print("")
    @staticmethod
    def john_the_butcher_incomplete(pig_meat):
        pig_meat_str = str(pig_meat)
        if pig_meat < 10:
            pig_meat_str = "-" + pig_meat_str
        print("-----------------------------------------------------")
        print("---------John-the-Butcher's-request-(LV5-10)---------")
        print("-----------------------------------------------------")
        print("-'Hey!-I-don't-think-you-got-what-I've-asked-ya!'----")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-------------pig-meat:-" + pig_meat_str + "/20------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("")
        print("")
    @staticmethod
    def john_the_butcher_completed():
        print("-----------------------------------------------------")
        print("---------John-the-Butcher's-request-(LV5-10)---------")
        print("-----------------------------------------------------")
        print("-'Alrightttt~'---------------------------------------")
        print("-'Thanks-buddy.'-------------------------------------")
        print("-'Here's-some-mesos'---------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("--*20-pig-meat-have-been-taken-from-your-inventory.--")
        print("----------------Reward:-5000-mesos-------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("")
        print("")
    @staticmethod
    def john_the_butcher_quest():
        print("-----------------------------------------------------")
        print("---------John-the-Butcher's-request-(LV5-10)---------")
        print("-----------------------------------------------------")
        print("-'Hey,-buddy!!'--------------------------------------")
        print("-'Yea-you!!!'----------------------------------------")
        print("-'Go-get-me-some-pig-meat!'--------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------*Get-20-pig-meat--------------------")
        print("----------------Reward:-5000-mesos-------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("")
        print("")
    @staticmethod
    def store():
        print("-----------------------------------------------------")
        print("-----------------------[STORE]-----------------------")
        print("-----------------------------------------------------")
        print("----------------------ITEM-LIST----------------------")
        print("-----------------------------------------------------")
        print("1.Beginner's-sword--------------[atk+3]----2000-mesos")
        print("2.Razor-Blade----------[str+2]--[atk+6]----5000-mesos")
        print("3.Maple-Axe------------[st +5]-[atk+10]---10000-mesos")
        print("4.Red-potion--------------------------------100-mesos")
        print("5.back-----------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("-----------------------------------------------------")
        print("")
        print("")
