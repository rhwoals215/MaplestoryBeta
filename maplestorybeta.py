#maplestorybeta
import os
import random
os.system('clear')
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
choice=raw_input("press enter to continue ")
lvl=1
meso=0
sp=0
exp=0
str1=5
dex1=5
luk1=5
int1=5
dmg=str1+(dex1-(dex1%2))/2+lvl
word=""
drkiller=False
kills=0
bobthebuilder=False
branch=0
johnthebutcher=False
pigmeat=0
if choice=="administrator":
    lvl=100
    meso=1000000000
playing=True
os.system('clear')
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
    choice=raw_input("Select: ")
    if choice==None:
        os.system('clear')
    if choice=="7":
        print("Are you sure? Your progress will not be saved.")
        choice=raw_input("type 1 to quit ")
        if choice=="1":
            break
        os.system('clear')
    if choice=="1":
        while exp>(lvl^2+2*lvl):
            exp-=(lvl^2+2*lvl)
            lvl+=1
            sp+=5
        level=str(lvl)
        dmg=str1+(dex1-(dex1%2))/2+lvl
        damage=str(dmg)
        experience=str(exp)
        strength=str(str1)
        dexterity=str(dex1)
        luck=str(luk1)
        intelligence=str(int1)
        statusPoint=str(sp)
        if lvl<10:
            level+="-"
        if sp<100:
            statusPoint+="-"
        if sp<10:
            statusPoint+="-"
        if dmg<10000000:
            damage+="-"
        if dmg<1000000:
            damage+="-"
        if dmg<100000:
            damage+="-"
        if dmg<10000:
            damage+="-"
        if dmg<1000:
            damage+="-"
        if dmg<100:
            damage+="-"
        if dmg<10:
            damage+="-"
        if str1<10:
            strength+="-"
        if dex1<10:
            dexterity+="-"
        if luk1<10:
            luck+="-"
        if int1<10:
            intelligence+="-"
        extra=""
        if exp<1000000000:
            extra+="-"
        if exp<100000000:
            extra+="-"
        if exp<10000000:
            extra+="-"
        if exp<1000000:
            extra+="-"
        if exp<100000:
            extra+="-"
        if exp<10000:
            extra+="-"
        if exp<1000:
            extra+="-"
        if exp<100:
            extra+="-"
        if exp<10:
            extra+="-"
        percentage=str(round(exp/(lvl^2+2*lvl),1))
        total=str(lvl^2+2*lvl)
        if (lvl^2+2*lvl)<1000000000:
            total+="-"
        if (lvl^2+2*lvl)<100000000:
            total+="-"
        if (lvl^2+2*lvl)<10000000:
            total+="-"
        if (lvl^2+2*lvl)<1000000:
            total+="-"
        if (lvl^2+2*lvl)<100000:
            total+="-"
        if (lvl^2+2*lvl)<10000:
            total+="-"
        if (lvl^2+2*lvl)<1000:
            total+="-"
        if (lvl^2+2*lvl)<100:
            total+="-"
        if (lvl^2+2*lvl)<10:
            total+="-"
        os.system('clear')
        print("-----------------------------------------------------")
        print("-----------------------STATUS------------------------")
        print("-----------------------------------------------------")
        print("LEVEL:-"+level+"------------"+percentage+"%----------------------------")
        print("exp:-"+experience+"/"+total+"---------------------------"+extra)
        print("-----------------------------------------------------")
        print("Avail.-SP:-"+statusPoint+"---------------------------------------")
        print("------------------------------------------------------")
        print("Damage:-"+damage+"------------------------------------")
        print("-----------------------------------------------------")
        print("")
        print("")
        print("")
        print("")
        choice=raw_input("Press enter to go back ")
        os.system('clear')
    if choice=="2":
        hunting=True
        os.system('clear')
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
            dmg=str1+(dex1-(dex1%2))/2+lvl
            choice=raw_input("Select ")
            if choice=="1":
                chance=random.randint(1,dmg)
                if chance==1:
                    print("you died...")
                    print("")
                    hunting=False
                    if exp>10:
                        exp-=10
                        print("You lost 10 exp.")
                    choice=raw_input("please press enter to continue.")
                else:
                    random1=random.randint(1,10)
                    if 1<=random1<=3:
                        word="small number"
                        exp+=1
                        if drkiller:
                            kills+=2
                    if 4<=random1<=7:
                        word="lot"
                        exp+=2
                        if drkiller:
                            kills+=3
                    if 8<=random1<=9:
                        word="bunch"
                        exp+=3
                        if drkiller:
                            kills+=4
                    if random1==10:
                        word="crap ton"
                        exp+=4
                        if drkiller:
                            kills+=6
                    print("You defeated a "+word+" of Snails.")
                    if 1<=random1<=3:
                        word="1"
                    if 4<=random1<=7:
                        word="2"
                    if 8<=random1<=9:
                        word="3"
                    if random1==10:
                        word="4"
                    print("You got "+word+" exp.")
                    while exp>(lvl^2+2*lvl):
                        exp-=(lvl^2+2*lvl)
                        lvl+=1
                        sp+=5
                        print("You leveled up!!!")
                    print("")
                    choice=raw_input("please press enter to continue.")
            if choice=="2":
                chance=random.randint(1,dmg)
                if 1<=chance<=3:
                    print("you died...")
                    print("")
                    hunting=False
                    if exp>10:
                        exp-=10
                        print("You lost 10 exp.")
                    choice=raw_input("please press enter to continue.")
                else:
                    random1=random.randint(1,12)
                    if 1<=random1<=3:
                        word="small number"
                        exp+=2
                        if drkiller:
                            kills+=2
                    if 4<=random1<=8:
                        word="lot"
                        exp+=5
                        if drkiller:
                            kills+=3
                    if 9<=random1<=11:
                        word="bunch"
                        exp+=7
                        if drkiller:
                            kills+=4
                    if random1==12:
                        word="crap ton"
                        exp+=10
                        if drkiller:
                            kills+=6
                    print("You defeated a "+word+" of Slimes and Stumps.")
                    if 1<=random1<=3:
                        word="2"
                    if 4<=random1<=7:
                        word="5"
                    if 8<=random1<=9:
                        word="7"
                    if random1==10:
                        word="10"
                    print("You got "+word+" exp.")
                    while exp>(lvl^2+2*lvl):
                        exp-=(lvl^2+2*lvl)
                        lvl+=1
                        sp+=5
                        print("You leveled up!!!")
                    print("")
                    choice=raw_input("please press enter to continue.")
            if choice=="3":
                chance=random.randint(1,dmg)
                if 1<=chance<=5:
                    print("you died...")
                    print("")
                    hunting=False
                    if exp>10:
                        exp-=10
                        print("You lost 10 exp.")
                    choice=raw_input("please press enter to continue.")
                else:
                    random1=random.randint(1,15)
                    if 1<=random1<=4:
                        word="small number"
                        exp+=5
                        if drkiller:
                            kills+=2
                    if 5<=random1<=11:
                        word="lot"
                        exp+=9
                        if drkiller:
                            kills+=3
                    if 12<=random1<=14:
                        word="bunch"
                        exp+=13
                        if drkiller:
                            kills+=4
                    if random1==15:
                        word="crap ton"
                        exp+=20
                        if drkiller:
                            kills+=6
                    print("You defeated a "+word+" of Pigs.")
                    if 1<=random1<=3:
                        word="1"
                    if 4<=random1<=7:
                        word="2"
                    if 8<=random1<=9:
                        word="3"
                    if random1==10:
                        word="4"
                    print("You got "+word+" exp.")
                    while exp>(lvl^2+2*lvl):
                        exp-=(lvl^2+2*lvl)
                        lvl+=1
                        sp+=5
                        print("You leveled up!!!")
                    print("")
                    choice=raw_input("please press enter to continue.")
            if choice=="4":
                chance=random.randint(1,dmg)
                if 1<=chance<=9:
                    print("you died...")
                    print("")
                    hunting=False
                    if exp>10:
                        exp-=10
                        print("You lost 10 exp.")
                    choice=raw_input("please press enter to continue.")


                else:
                    random1=random.randint(1,20)
                    if 1<=random1<=6:
                        word="small number"
                        exp+=10
                        if drkiller:
                            kills+=2
                    if 7<=random1<=15:
                        word="lot"
                        exp+=16
                        if drkiller:
                            kills+=3
                    if 16<=random1<=19:
                        word="bunch"
                        exp+=24
                        if drkiller:
                            kills+=4
                    if random1==20:
                        word="crap ton"
                        exp+=30
                        if drkiller:
                            kills+=6
                    print("You defeated a "+word+" of Mushrooms")
                    if 1<=random1<=3:
                        word="10"
                    if 4<=random1<=7:
                        word="16"
                    if 8<=random1<=9:
                        word="24"
                    if random1==10:
                        word="30"
                    print("You got "+word+" exp.")
                    while exp>(lvl^2+2*lvl):
                        exp-=(lvl^2+2*lvl)
                        lvl+=1
                        sp+=5
                        print("You leveled up!!!")
                    print("")
                    choice=raw_input("please press enter to continue.")
            if choice=="5":
                hunting=False
            os.system('clear')
    if choice=="3":
        os.system('clear')
        quest=True
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
            choice=raw_input("Select ")
            if choice=="1":
                if kills<100 and drkiller:
                    killsstr=str(kills)
                    if kills<10:
                        killsstr="-"+killsstr
                    print("-----------------------------------------------------")
                    print("---------------Dr.Killer's-plan-(LV1+)---------------")
                    print("-----------------------------------------------------")
                    print("-'You-didn't-finish-the-job!'------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("----------------kills:-"+killsstr+"/100------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("")
                    print("")
                    print("")
                    print("")
                    choice==raw_input("Press enter.")
                if kills>100 and drkiller:
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
                    drkiller=False
                    meso+=2000
                    kills=0
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
                    choice=raw_input("Select ")
                    if choice=="1":
                        drkiller=True
            if choice=="2":
                if branch<30 and bobthebuilder:
                    branchstr=branch
                    if branch<10:
                        branchstr="-"+branchstr
                    print("-----------------------------------------------------")
                    print("----------Bob-the-Builder's-supplies-(LV3+)----------")
                    print("-----------------------------------------------------")
                    print("-'Hmm..-I-don't-think-you-got-all-the-supplies.'-----")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-------------branches:-"+branchstr+"/30------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("")
                    print("")
                    print("")
                    print("")
                if branch>=30 and bobthebuilder:
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
                    bobthebuilder=False
                    meso+=3000
                    branch=0
                    choice=raw_input("Press enter.")
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
                    choice=raw_input("Select ")
                    if choice=="1":
                        bobthebuilder=True
            if choice=="3":
                if pigmeat<20 and johnthebutcher:
                    pigmeatstr=str(pigmeat)
                    if pigmeat<10:
                        pigmeatstr="-"+pigmeatstr
                    print("-----------------------------------------------------")
                    print("---------John-the-Butcher's-request-(LV5-10)---------")
                    print("-----------------------------------------------------")
                    print("-'Hey!-I-don't-think-you-got-what-I've-asked-ya!'----")
                    print("-'Yea-you!!!'----------------------------------------")
                    print("-'Go-get-me-some-pigmeat!'---------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("------------pigmeat:-"+pigmeatstr+"/20--------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("-----------------------------------------------------")
                    print("")
                    print("")
                    print("")
                    print("")
                    bobthebuilder=False
                    choice=raw_input("Press enter.")
                if pigmeat>=20 and bobthebuilder:
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
                    johnthebutcher=False
                    pigmeat=0
                    meso+=5000
                    choice=raw_input("Press enter.")
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
                    choice=raw_input("Press enter.")
                    if choice=="1":
                        johnthebutcher=True
                os.system('clear')
    if choice=="4":
        while store:
            print("-----------------------------------------------------")
            print("------------------------STORE------------------------")
            print("-----------------------------------------------------")
            print("----------------------ITEM-LIST----------------------")
            print("-----------------------------------------------------")
            print("1.Beginner's-sword-(Lv1)--------[atk+3]----2000-mesos")
            print("3.Maple-Axe---(Lv8)----[str+5]-[atk+10]---10000-mesos")
            print("2.Razor-Blade-(Lv5)----[str+2]--[atk+6]----5000-mesos")
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
            choice=raw_input("Select: ")
            if choice=="1":
                sword1=True
            if choice=="2":
                blade1=True
            if choice=="3":
                axe1=True
            if choice=="4":
                os.system('clear')
