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
choice=raw_input("press enter to continue")
lvl=1
meso=0
sp=0
exp=0
str1=5
dex1=5
luk1=5
int1=5
dmg=5
word=""
if choice=="administrator":
    lvl=100
    meso=1000000000
playing=True
hunting=True
os.system('clear')
while playing:
    print("-----------------------------------------------------")
    print("--------------------Maple-Island---------------------")
    print("-----------------------------------------------------")
    print("-----------------------OPTIONS-----------------------")
    print("-----------------------------------------------------")
    print("-1.-Status-------------------------------------------")
    print("-2.-Hunt---------------------------------------------")
    print("-3.-Quests-------------------------------------------")
    print("-4.-Party-Quest--------------------------------------")
    print("-5.-Store--------------------------------------------")
    print("-6.-Inventory----------------------------------------")
    print("-7.-Go-to-Victoria-Island----------------------------")
    print("-8.-Quit-Game----------------------------------------")
    print("-----------------------------------------------------")
    print("")
    print("")
    hunting=True
    choice=raw_input("Select")
    if choice=="8":
        break
    if choice=="1":
        while exp>(lvl^2+2*lvl):
            exp-=(lvl^2+2*lvl)
            lvl+=1
            sp+=5
        level=str(lvl)
        damage=str(dmg)
        experience=str(exp)
        strength=str(str1)
        dexterity=str(dex1)
        luck=str(luk1)
        intelligence=str(int1)
        statusPoint=str(sp)
        if lvl<10:
            level+="-"
        if exp<10:
            experience+="-"
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
        percentage=str(round(exp/(lvl^2+2*lvl),1))
        os.system('clear')
        print("-----------------------------------------------------")
        print("-----------------------STATUS------------------------")
        print("-----------------------------------------------------")
        print("---LEVEL:-"+level+"---------------"+experience+"%-----------------------")
        print("-----------------------------------------------------")
        print("-STR:-"+strength+"---------------------------------------------")
        print("-DEX:-"+dexterity+"---------------------------------------------")
        print("-LUK:-"+luck+"---------------------------------------------")
        print("-INT:-"+intelligence+"---------------------------------------------")
        print("-----------------------------------------------------")
        print("-Avail.-SP:-"+statusPoint+"--------------------------------------")
        print("-----------------------------------------------------")
        print("-Damage:-"+damage+"------------------------------------")
        print("-----------------------------------------------------")
        print("")
        print("")
        print("")
        print("")
        choice=raw_input("Press enter to go back")
        os.system('clear')
    if choice=="2":
        os.system('clear')
        while hunting:
            print("-----------------------------------------------------")
            print("-----------------------Hunting-----------------------")
            print("-----------------------------------------------------")
            print("-----------------------OPTIONS-----------------------")
            print("-----------------------------------------------------")
            print("-1.-Hunt-Snails-(LV1-5)------------------------------")
            print("-2.-Hunt-Slimes-(LV3-7)------------------------------")
            print("-3.-Hunt-Pigs-(LV5-10)-------------------------------")
            print("-4.-Hunt-Mushrooms-(LV7-10)--------------------------")
            print("-5.-Back---------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("-----------------------------------------------------")
            print("")
            print("")
            print("")
            print("")
            choice=raw_input("Select")
            if choice=="5":
                hunting=False
            if choice=="1":
                if dex%2=1:
                    atk=dmg+str1+(dex+1)/2+lvl
                else:
                    atk=dmg+str1+dex/2+lvl
                chance=random.randint(1,atk)
                if chance==1:
                    print("you died...")
                    print("")
                    choice=raw_input("please press enter to continue.")
                    if exp>10:
                        exp-=10
                else:
                    random1=random.randint(1,10)
                    if 1<=random1<=3:
                        word="small amount"
                        exp+=1
                    if 4<=random1<=7:
                        word="lot"
                        exp+=2
                    if 8<=random1<=9:
                        word="bunch"
                        exp+=3
                    if random1==10:
                        word="crap ton"
                        exp+=4
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
            os.system('clear')
