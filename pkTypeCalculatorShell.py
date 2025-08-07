#!/usr/bin/env python

import json
import os
import sys
import time
import collections
import configparser
import time

textbarrier = "*********************************************"

def printtext(message=' '):
    if __name__ == '__main__':
        print(message)

def generalWarning(message):
    if __name__ == '__main__':
        print()
        print(textbarrier)
        print(message)
        print(textbarrier)
        print()
        time.sleep(0.50)

def forcekill():
    sys.exit("the program has been forcefully terminated due to an error")


def accessIni(request):
    try:
        config = configparser.ConfigParser()
        config.read('pk-type-calculator.ini')

    except KeyError:
        printtext("there has been an KeyError, the program was most likely unable to access a key in the config.ini, or is unable to access the ini itself")
        forcekill()
    except NameError:
        printtext("there has been an NameError, the program was most likely unable to read a section name")
        forcekill()
    except AttributeError:
        printtext("there has been an AttributeError, the program was most likely unable to access an objects attribute")
        forcekill()
    global sprites
    global rootFolder
    global path2glossary
    rootFolder = config['DEFAULT']['apiPath']
    path2glossary = config['DEFAULT']['path2glossary']
    sprites = config['SPRITES']['sprites']

    if not __name__ == '__main__':
        if request == "rootFolder":
            return config['DEFAULT']['apiPath']
        elif request == "path2glossary":
            return config['DEFAULT']['path2glossary']
        elif request == "sprites":
            return config['SPRITES']['sprites']


def typecalc(hassecondtype, atkOrDef):
    vunerable_elements = set(current_pokemon["pokemon_vunerable"])
    resistance_elements = set(current_pokemon["pokemon_resistance"])
    immune_elements = set(current_pokemon["pokemon_immunity"])
    strength_elements = set(current_pokemon["pokemon_strength"])
    weakness_elements = set(current_pokemon["pokemon_weakness"])
    incapable_elements = set(current_pokemon["pokemon_incapable"])

    def removeDuplicateDef():
        for element in vunerable_elements:
            for childElement in resistance_elements:
                if element == childElement:
                    current_pokemon["pokemon_vunerable"].remove(element)
                    current_pokemon["pokemon_resistance"].remove(element)
        
    def removeDuplicateAtk():
        for element in strength_elements:
            for childElement in normalAtk:
                if element == childElement:
                    normalAtk.remove(element)
        for element in weakness_elements:
            for childElement in incapable_elements:
                if element == childElement:
                    current_pokemon["pokemon_incapable"].remove(element)
        for element in normalAtk:
            for childElement in weakness_elements:
                if element == childElement:
                    current_pokemon["pokemon_weakness"].remove(element)

    
    if hassecondtype:
        removeDuplicateDef()

    def calcVunerable(hassecondtype):
        if not hassecondtype:
            generalWarning("pokemon recieves double damage from these types")
            for item in current_pokemon["pokemon_vunerable"]:
                printtext(f"{item}x2")
            return current_pokemon["pokemon_vunerable"]
        elif hassecondtype:
            generalWarning("pokemon recieves double/quad damage from these types")
            for element in vunerable_elements:
                countedElement = current_pokemon["pokemon_vunerable"].count(element)
                if countedElement == 1:
                    printtext(f"{element}x2")
                elif countedElement == 2:
                    printtext(f"{element}x4")
            return current_pokemon["pokemon_vunerable"]

    def calcResistance(hassecondtype):
        if not hassecondtype:
            generalWarning("pokemon recieves half damage from these types")
            for item in current_pokemon["pokemon_resistance"]:
                printtext(f"{item}x0.5")
            return current_pokemon["pokemon_resistance"]
        elif hassecondtype:
            generalWarning("pokemon recieves half/quarter damage from these types")
            for element in resistance_elements:
                countedElement = current_pokemon["pokemon_resistance"].count(element)
                if countedElement == 1:
                    printtext(f"{element}x0.5")
                elif countedElement == 2:
                    printtext(f"{element}x0.25")
            return current_pokemon["pokemon_resistance"]

    def calcImmune(hassecondtype):
        generalWarning("pokemon recieves no damage from these types")
        for element in immune_elements:
            printtext(f"{element}x0")
        return current_pokemon["pokemon_immunity"]

    def printStrength():
        generalWarning("pokemon deals double damage against these types")
        for element in current_pokemon["pokemon_strength"]:
            printtext(f"{element}x2")
        return current_pokemon["pokemon_strength"]

    def printWeakness():
        generalWarning("pokemon deals half damage against these types")
        for element in current_pokemon["pokemon_weakness"]:
            printtext(f"{element}x0.5")
        return current_pokemon["pokemon_weakness"]
        

    def printIncapable():
        generalWarning("pokemon deals no damage against these types")
        for element in current_pokemon["pokemon_incapable"]:
            printtext(f"{element}x0")
        return current_pokemon["pokemon_incapable"]
        #for element in incapable_elements:
        #    countedElement = current_pokemon["pokemon_incapable"].count(element)
        #    if countedElement == 2:
        #        current_pokemon["pokemon_incapable"].remove(element)
        #        printtext(f"{element}")
    
    def printNormalattack():
        generalWarning("pokemon deals neutral damage against these types")
        for item in normalAtk:
            printtext(f"{item}x1")

    def calcNormaldefense():
        #printtext(normalDef)
        for item in current_pokemon['pokemon_resistance']:
            for item2 in normalDef:
                if item == item2:
                    normalDef.remove(item)
        #printtext(normalDef)
        for item in current_pokemon['pokemon_vunerable']:
            for item2 in normalDef:
                if item == item2:
                    normalDef.remove(item)
        #printtext(normalDef)
        for item in current_pokemon['pokemon_immunity']:
            for item2 in normalDef:
                if item == item2:
                    normalDef.remove(item)
        generalWarning("pokemon recieves neutral damage against these types")
        for item in normalDef:
            printtext(f"{item}x1")

    if atkOrDef == "attack":
        removeDuplicateAtk()
        printStrength()
        printWeakness()
        printIncapable()
        printNormalattack()

    elif atkOrDef == "defense":
        calcImmune(hassecondtype)
        calcResistance(hassecondtype)
        calcVunerable(hassecondtype)
        calcNormaldefense()



def clearCurrentPkmon():
    for key in current_pokemon:
        current_pokemon[key].clear()
    normalAtk = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]
    normalDef = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]

global current_pokemon
current_pokemon = {
    #defense
    "pokemon_vunerable" : [],
    "pokemon_resistance" : [],
    "pokemon_immunity" :[],
    #offense
    "pokemon_strength" : [],
    "pokemon_weakness" : [],
    "pokemon_incapable" : []
}
global normalAtk
global normalDef
normalAtk = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]
normalDef = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]

def maketypecall(pktype):
    typeGlossary = f"{rootFolder}{path2glossary}index.json"
    try:
        with open(typeGlossary, "r") as file:
            content = json.load(file)
            for item in content["results"]:
                if item["name"] == pktype:
                    nextpath = item["url"]
            try:
                with open(f"{rootFolder}{nextpath}index.json","r") as file:
                    content = json.load(file)

                    vunerable_list = content["damage_relations"]["double_damage_from"]
                    for item in vunerable_list:
                        current_pokemon["pokemon_vunerable"].append(item["name"])

                    resistance_list = content["damage_relations"]["half_damage_from"]
                    for item in resistance_list:
                        current_pokemon["pokemon_resistance"].append(item["name"])

                    immunity_list = content["damage_relations"]["no_damage_from"]
                    for item in immunity_list:
                        current_pokemon["pokemon_immunity"].append(item["name"])

                    strength_list = content["damage_relations"]["double_damage_to"]
                    for item in strength_list:
                        current_pokemon["pokemon_strength"].append(item["name"])

                    weakness_list = content["damage_relations"]["half_damage_to"]
                    for item in weakness_list:
                        current_pokemon["pokemon_weakness"].append(item["name"])

                    incapable_list = content["damage_relations"]["no_damage_to"]
                    for item in incapable_list:
                        current_pokemon["pokemon_incapable"].append(item["name"])
            except FileNotFoundError:
                printtext("pokemon type file not found")
    except FileNotFoundError:
        printtext("the type library file has not been found. make sure it is in the correct directory or that the ini has the correct variables")

def main():
    running = True
    inMenu = True
    try:
        while running:
            while inMenu:
                choice = str(input("what type match up would you like to calculate?\n attack or defense?: ")).lower()
                if choice == "attack":
                    inMenu = False
                elif choice == "defense":
                    inMenu = False
                else:
                    print(f"{choice} was invalid")
            
            if choice == "attack":
                hassecondtype = False
                while True:
                    attacktype = str(input("please input an attacking pokemon type (F to finish): ")).lower()
                    if attacktype == "f":
                        break
                    elif attacktype.isalpha():
                        try:
                            for item in normalAtk:
                                if item == attacktype:
                                    maketypecall(item)
                        except KeyboardInterrupt:
                            printtext("canceled")
                typecalc(hassecondtype,choice)
                clearCurrentPkmon()
                inMenu = True

            if choice == "defense":
                hassecondtype = False
                hasNoFirstType = True
                while hasNoFirstType:
                    type1 = str(input("what is the first type of your pokemon?: ")).lower()
                    if not type1.isalpha():
                            generalWarning("you MUST enter a primary typing")
                    else:
                        hasNoFirstType = False

                type2 = str(input("what is the second type of your pokemon?: ")).lower()
                if type2.isalpha():
                    hassecondtype = True
                    maketypecall(type2)
                else:
                    generalWarning("skipping secondary typing")
                if type1.isalpha() and not type1 == type2:
                    maketypecall(type1)
                    typecalc(hassecondtype, choice)
                    clearCurrentPkmon()
                    inMenu = True
                else:
                    generalWarning("you cannot enter duplicate types")
    except KeyboardInterrupt:
        print()

    printtext("goodbye")

if __name__ == '__main__':
    accessIni("i am terrible at this carreer")
    main()
