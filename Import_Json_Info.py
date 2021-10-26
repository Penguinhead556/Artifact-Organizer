import json
from JsonMapping import Mapping_Dict
from artifact_helpers import *

f = open("Penguinhead82.json", "r", encoding='utf-8')
Json_Data = json.load(f)
f.close()

Monster_data = Json_Data["unit_list"]

for monster in Monster_data:
    if monster["unit_level"] == 40:
        name = Mapping_Dict["Monsters"][monster["unit_master_id"]]["Name"]
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
                type = "Type"
            elif artifact["type"] == 2:
                type = "Element"
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
