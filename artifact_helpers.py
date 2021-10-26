import json
import operator


Monster_Info = {}
All_Monsters = []

f = open("MonstersDB.json", "r")
if (f.read() != ""):
    f.seek(0)
    Monster_Info = json.load(f)
f.close()

Monster_Info = dict(sorted(Monster_Info.items(), key=operator.itemgetter(0)))


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

def monster_efficiency(Monster, Artifact):
    Monster_artifact = []
    for property in Artifact:
        if property[0] in Monster_Info[Monster]["Substats"]:
            Monster_artifact.append([property[0], property[1]])

    # print(Monster_artifact)

    return (calculate_efficiency(Monster_artifact))