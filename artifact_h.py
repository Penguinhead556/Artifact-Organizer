from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter import ttk
import ctypes
import json
import operator

from JsonMapping import Mapping_Dict
from Configure_Monsters import *


def initialize_data():
    f = open("MonstersDB.json", "r")
    if (f.read() != ""):
        f.seek(0)
        Monster_Info = json.load(f)
    f.close()


    f = open("Inventory.json", "r")
    if (f.read() != ""):
        f.seek(0)
        Inventory_data = json.load(f)
    f.close()

    Monster_Info = dict(sorted(Monster_Info.items(), key=operator.itemgetter(0)))

    return Monster_Info, Inventory_data

    


elements = ['-', 'fire','water', 'wind','light', 'dark']
types = ['-', 'attack', 'hp', 'def', 'support']

all_types = elements+types

subproperties = [
    ["S1_CD", "S2_CD", "S3_CD", "S4_CD"],
    ["S1_Recovery", "S2_Recovery", "S3_Recovery"],
    ["S1_ACC", "S2_ACC", "S3_ACC"],
    ["DMG_on_Wind", "DMG_on_Water", "DMG_on_Fire", "DMG_on_Light", "DMG_on_Dark"],
    ["DMG_from_Wind", "DMG_from_Water", "DMG_from_Fire", "DMG_from_Light", "DMG_from_Dark"],
    ["CD_as_HP_is_Good", "CD_as_HP_is_Bad", "Single_TGT_CD"],
    ["Lost_HP_ATK_up", "Lost_HP_DEF_up", "Lost_HP_SPD_up"],
    ["ATK_INC_Effect", "SPD_INC_Effect", "DEF_INC_Effect"],
    ["Counter_DMG", "Teamup_DMG", "Bomb_DMG"],
    ["Life_Drain", "HP_Revived", "ATK_Bar_Revived"],
    ["ADL_DMG_HP", "ADL_DMG_ATK", "ADL_DMG_DEF", "ADL_DMG_SPD"],
    ["CD_Recieved"]
]

property_range = [
    [[4, 6], [4, 6], [4, 6], [4, 6]],
    [[4, 6], [4, 6], [4, 6]],
    [[4, 6], [4, 6], [4, 6]],
    [[3, 5], [3, 5], [3, 5], [3, 5], [3, 5]],
    [[4, 6], [4, 6], [4, 6], [4, 6], [4, 6]],
    [[4, 6], [8, 12], [2, 4]],
    [[9, 14], [9, 14], [9, 14]],
    [[3, 5], [4, 6], [2, 4]],
    [[2, 4], [2, 4], [2,  4]],
    [[5, 8], [4, 6], [4, 6]],
    [[0.2, 0.3], [2, 4], [2, 4], [25, 40]],
    [[2, 4]]
]


flat_subproperties = []

for rows in subproperties:
    flat_subproperties = flat_subproperties + rows

flat_property_range = []

for rows in property_range:
    flat_property_range = flat_property_range + rows


def calculate_efficiency(Artifact):
    rolls = 0
    for substats in Artifact:
        substat_index = flat_subproperties.index(substats[0])
        rolls = rolls + float(substats[1]) / flat_property_range[substat_index][1]
    
    return round(rolls / 8 *100, 2)

def monster_efficiency(Monster, Artifact, Monster_Info):
    Monster_artifact = []
    for property in Artifact:
        if property[0] in Monster_Info[Monster]["Substats"]:
            Monster_artifact.append([property[0], property[1]])

    # print(Monster_artifact)

    return (calculate_efficiency(Monster_artifact))

def load_json(Monster_Info):

    f = open("Penguinhead82-23383202.json", "r", encoding='utf-8')
    Json_Data = json.load(f)
    f.close()

    Monster_data = Json_Data["unit_list"]

    for monster in Monster_data:
        if monster["unit_level"] == 40:
            if monster["unit_master_id"] in Mapping_Dict["Monsters"]:
                name = Mapping_Dict["Monsters"][monster["unit_master_id"]]["Name"]
                Monster_Info[name]["Element"] = Mapping_Dict["Monsters"][monster["unit_master_id"]]["Element"]
                Monster_Info[name]["Type"] = Mapping_Dict["Monsters"][monster["unit_master_id"]]["Type"]
            else:
                name = "_" + str(monster["unit_master_id"])

            orig_name = name
            dupe_counter = 0
            while name in Monster_Info:
                if "id" not in Monster_Info[name]:
                    Monster_Info[name]["id"] = monster["unit_id"]
                if Monster_Info[name]["id"] != monster["unit_id"]:
                    dupe_counter = dupe_counter + 1
                    name = orig_name + str(dupe_counter)
                    print(name)
                else:
                    break

            if name not in Monster_Info:
                Monster_Info[name] = {}
                Monster_Info[name]["id"] = monster["unit_id"]
                Monster_Info[name]["Element"] = ""
                Monster_Info[name]["Type"] = ""
                Monster_Info[name]["Efficiency"] = {}
                Monster_Info[name]["Artifacts"] = {}
                Monster_Info[name]["Artifacts"]["Element"] = []
                Monster_Info[name]["Artifacts"]["Type"] = []
                Monster_Info[name]["Efficiency"]["Element"] = 0
                Monster_Info[name]["Efficiency"]["Type"] = 0

                if dupe_counter > 0 and "Substats" in Monster_Info[orig_name]:
                    Monster_Info[name]["Substats"] = Monster_Info[orig_name]["Substats"]
                    Monster_Info[name]["Element"] = Monster_Info[orig_name]["Element"]
                    Monster_Info[name]["Type"] = Monster_Info[orig_name]["Type"]
            for artifact in monster["artifacts"]:
                if artifact["type"] == 1:
                    type = "Element"
                elif artifact["type"] == 2:
                    type = "Type"
                subs = []
                for subproperties in artifact["sec_effects"]:
                    if subproperties[0] in Mapping_Dict["Artifacts"]:
                        subs.append([Mapping_Dict["Artifacts"][subproperties[0]], str(subproperties[1])])
                
                Monster_Info[name]["Artifacts"][type] = subs
                if  "Substats" in Monster_Info[name]:
                    Monster_Info[name]["Efficiency"][type] = monster_efficiency(name, subs, Monster_Info)


    f = open("MonstersDB.json", "w")
    json.dump(Monster_Info, f, indent = 6)
    f.close()

    Inventory = []
    artifacts_inventory = Json_Data["artifacts"]

    for i in range(len(artifacts_inventory)):
        artifact = {}
        Powerup_lvl = artifacts_inventory[i]["pri_effect"][2]
        if Powerup_lvl < 3:
            Rolls = 4
        elif Powerup_lvl < 6:
            Rolls = 3
        elif Powerup_lvl < 9:
            Rolls = 2
        elif Powerup_lvl < 12:
            Rolls = 1
        else:
            Rolls = 0

        artifact["Rolls"] = Rolls
        Artifact_Type = Mapping_Dict["Artifact_Type"][artifacts_inventory[i]["type"]]

        if Artifact_Type == "Element":
            artifact["type"] = Mapping_Dict["Elements"][artifacts_inventory[i]["attribute"]]
        elif Artifact_Type == "Type":
            artifact["type"] = Mapping_Dict["Types"][artifacts_inventory[i]["unit_style"]]

        artifact_subs = []

        for subs in artifacts_inventory[i]["sec_effects"]:
            if subs[0] in Mapping_Dict["Artifacts"]:
                artifact_subs.append([Mapping_Dict["Artifacts"][subs[0]], str(subs[1])])

        artifact["subproperties"] = artifact_subs
        artifact["obtained"] = artifacts_inventory[i]["date_add"]

        Inventory.append(artifact)

    Inventory = sorted(Inventory, key=lambda d: d['obtained']) 


    f = open("Inventory.json", "w")
    json.dump(Inventory, f, indent = 6)
    f.close()
