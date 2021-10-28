import json
from JsonMapping import Mapping_Dict
from artifact_helpers import *

f = open("Penguinhead82.json", "r", encoding='utf-8')
Json_Data = json.load(f)
f.close()

Monster_data = Json_Data["unit_list"]

for monster in Monster_data:
    if monster["unit_level"] == 40:
        if monster["unit_master_id"] in Mapping_Dict["Monsters"]:
            name = Mapping_Dict["Monsters"][monster["unit_master_id"]]["Name"]
        else:
            name = monster["unit_master_id"]
        if name not in Monster_Info:
            Monster_Info[name] = {}
            Monster_Info[name]["Element"] = ""
            Monster_Info[name]["Type"] = ""
            Monster_Info[name]["Efficiency"] = {}
            Monster_Info[name]["Artifacts"] = {}
            Monster_Info[name]["Artifacts"]["Element"] = []
            Monster_Info[name]["Artifacts"]["Type"] = []
            Monster_Info[name]["Efficiency"]["Element"] = 0
            Monster_Info[name]["Efficiency"]["Type"] = 0
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
                Monster_Info[name]["Efficiency"][type] = monster_efficiency(name, subs)


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

    Inventory.append(artifact)

Inventory = sorted(Inventory, key=lambda d: d['type']) 


f = open("Inventory.json", "w")
json.dump(Inventory, f, indent = 6)
f.close()