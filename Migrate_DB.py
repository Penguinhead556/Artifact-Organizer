import csv    
import json
    
Monster_info = []
Json_Dictionary = {}

f = open("MonstersDB.json", "r")
if (f.read() != ""):
    f.seek(0)
    Json_Dictionary = json.load(f)
f.close()

with open('MonstersDB.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        Monster_info.append(row)

for monster in Monster_info:
    monster_name = monster[0]
    element = monster[1]
    type = monster[2]
    if monster_name not in Json_Dictionary:
        Json_Dictionary[monster_name] = {}
        Json_Dictionary[monster_name]["Efficiency"] = {}
        Json_Dictionary[monster_name]["Artifacts"] = {}
        Json_Dictionary[monster_name]["Artifacts"]["Element"] = []
        Json_Dictionary[monster_name]["Artifacts"]["Type"] = []
        Json_Dictionary[monster_name]["Efficiency"]["Element"] = 0
        Json_Dictionary[monster_name]["Efficiency"]["Type"] = 0
    Json_Dictionary[monster_name]["Element"] = element
    Json_Dictionary[monster_name]["Type"] = type
    Json_Dictionary[monster_name]["Substats"] = monster[3:]

f = open("MonstersDB.json", "w")
json.dump(Json_Dictionary, f, indent = 6)
f.close()

