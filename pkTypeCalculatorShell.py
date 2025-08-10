#!/usr/bin/env python

import json
import os
import sys
import time
import collections
import configparser
import time



def printtext(message=' '):
    if __name__ == '__main__':
        print(message)

def generalWarning(message):
    textbarrier = "*********************************************"
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
        print(typebuffer)
        for element in current_pokemon['normalAtk']:
            for childElement in typebuffer:
                if typebuffer.count(element) > 0:
                    print(f"{element} was saved")
                elif typebuffer.count(element) == -1:
                    print(f"{element} was destroyed")
                    current_pokemon['normalAtk'].remove(element)
        print(typebuffer)


        #for element in strength_elements:
        #    for childElement in current_pokemon['normalAtk']:
        #        if element == childElement:
        #            current_pokemon['normalAtk'].remove(element)
        #for element in weakness_elements:
        #    for childElement in incapable_elements:
        #        if element == childElement:
        #            current_pokemon["pokemon_incapable"].remove(element)
        #for element in current_pokemon['normalAtk']:
        #    for childElement in weakness_elements:
        #        if element == childElement:
        #            current_pokemon["pokemon_weakness"].remove(element)

    
    if hassecondtype:
        removeDuplicateDef()

    if atkOrDef == "attack":
        removeDuplicateAtk()
    elif atkOrDef == "defense":
        calcImmune(hassecondtype)
        calcResistance(hassecondtype)
        calcVunerable(hassecondtype)
        calcNormaldefense()

def resettypebuffer():
        global typebuffer
        typebuffer = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]

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
    for item in current_pokemon['normalAtk']:
        printtext(f"{item}x1")

def clearCurrentPkmon():
    for key in current_pokemon:
        if not key == "normalAtk" and not key == "normalDef":
            current_pokemon[key].clear()
        elif key == "normalAtk" or key == "normalDef":
            current_pokemon[key] = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]

global typebuffer
typebuffer = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]

global current_pokemon
current_pokemon = {
    #defense
    "pokemon_vunerable" : [],
    "pokemon_resistance" : [],
    "pokemon_immunity" :[],
    "normalDef" : ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"],
    #offense
    "pokemon_strength" : [],
    "pokemon_weakness" : [],
    "pokemon_incapable" : [],
    "normalAtk" : ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel","fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]
}

def maketypecall(pktype, choice, hassecondtype=False):
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
                    resettypebuffer()

                    #defense

                    vunerable_list = content["damage_relations"]["double_damage_from"]
                    for item in vunerable_list:
                        current_pokemon["pokemon_vunerable"].append(item["name"])

                    resistance_list = content["damage_relations"]["half_damage_from"]
                    for item in resistance_list:
                        current_pokemon["pokemon_resistance"].append(item["name"])

                    immunity_list = content["damage_relations"]["no_damage_from"]
                    for item in immunity_list:
                        current_pokemon["pokemon_immunity"].append(item["name"])

                    #attack

                    strength_list = content["damage_relations"]["double_damage_to"]
                    for item in strength_list:
                        counted = current_pokemon['pokemon_strength'].count(item['name'])
                        if counted == 0:
                            current_pokemon["pokemon_strength"].append(item["name"])
                    for item in strength_list:
                        for element in typebuffer:
                            if element == item['name']:
                                typebuffer.remove(element)
                    print(f"strong ele{current_pokemon['pokemon_strength']}")

                    weakness_list = content["damage_relations"]["half_damage_to"]
                    for item in weakness_list:
                        counted = current_pokemon['pokemon_weakness'].count(item['name'])
                        if counted == 0:
                            current_pokemon['pokemon_weakness'].append(item["name"])
                    for item in weakness_list:
                        for element in typebuffer:
                            if element == item['name']:
                                typebuffer.remove(element)
                    print(f"weak ele{current_pokemon['pokemon_weakness']}")
                    
                    incapable_list = content["damage_relations"]["no_damage_to"]
                    for item in incapable_list:
                        counted = current_pokemon['pokemon_incapable'].count(item['name'])
                        if counted == 0:
                            current_pokemon['pokemon_incapable'].append(item["name"])
                    for item in incapable_list:
                        for element in typebuffer:
                            if element == item['name']:
                                typebuffer.remove(element)
                    print(f"incap ele{current_pokemon['pokemon_incapable']}")

                    print()
                    print(current_pokemon)
                    print("before")
                    print(typebuffer)
                    print(current_pokemon['normalAtk'])
                    for element in current_pokemon['normalAtk']:
                        for childElement in typebuffer:
                            if typebuffer.count(element) == -1:
                                current_pokemon['normalAtk'].remove(element)
                    print("after")
                    print(typebuffer)
                    print(current_pokemon['normalAtk'])
                    print()
                    print(current_pokemon)
                    print()

                    for element in current_pokemon['pokemon_weakness']:
                        for item in current_pokemon['pokemon_incapable']:
                            if element == item:
                                current_pokemon['pokemon_incapable'].remove(item)
                    print(current_pokemon['normalAtk'])
                    for element in current_pokemon['normalAtk']:
                        for item in current_pokemon['pokemon_weakness']:
                            if element == item:
                                current_pokemon['pokemon_weakness'].remove(item)
                        for item in current_pokemon['pokemon_incapable']:
                            if element == item:
                                current_pokemon['pokemon_incapable'].remove(item)
                    print(current_pokemon['normalAtk'])
                    for element in current_pokemon['pokemon_strength']:
                        for item in current_pokemon['normalAtk']:
                            if element == item:
                                current_pokemon['normalAtk'].remove(item)
                        for item in current_pokemon['pokemon_weakness']:
                            if element == item:
                                current_pokemon['pokemon_weakness'].remove(item)
                        for item in current_pokemon['pokemon_incapable']:
                            if element == item:
                                current_pokemon['pokemon_incapable'].remove(item)
                    print(current_pokemon['normalAtk'])

                    #if choice == "attack":
                        #typecalc(False,choice)

                    if choice == "defense":
                        typecalc(hassecondtype,choice)

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
                while True:
                    attacktype = str(input("please input an attacking pokemon type (F to finish): ")).lower()
                    if attacktype == "f":
                        break
                    elif attacktype.isalpha():
                        try:
                            for item in current_pokemon['normalAtk']:
                                if item == attacktype:
                                    maketypecall(item, choice)
                        except KeyboardInterrupt:
                            printtext("canceled")
                #print pk types
                printStrength()
                printNormalattack()
                printWeakness()
                printIncapable()
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
                        for item in current_pokemon['normalAtk']:
                            if item == type1:
                                hasNoFirstType = False

                type2 = str(input("what is the second type of your pokemon?: ")).lower()
                if type2.isalpha():
                    for item in current_pokemon['normalAtk']:
                        if item == type2:
                            hassecondtype = True
                            maketypecall(type2, choice, hassecondtype)
                else:
                    generalWarning("skipping secondary typing")
                if type1.isalpha() and not type1 == type2:
                    maketypecall(type1, choice, hassecondtype)
                    clearCurrentPkmon()
                    inMenu = True
                else:
                    generalWarning("you cannot enter duplicate types")
    except KeyboardInterrupt:
        print()

    printtext("goodbye")

if __name__ == '__main__':
    accessIni("i am terrible at this")
    main()
