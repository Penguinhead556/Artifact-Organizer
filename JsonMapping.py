def Add_Monster(_name, _element, _type):
    return dict(Name = _name, Element = _element, Type = _type)

Mapping_Dict = dict(
    Monsters = dict([ #ID is unit_master_id
        (15311, Add_Monster("Rina", "water", "support")),
        (15711, Add_Monster("Praha", "water", "support")),
        (17911, Add_Monster("Beth", "water", "attack")),
        (20511, Add_Monster("Bastet", "water", "support")),
        (16111, Add_Monster("Anavel", "water", "support")),
        (21512, Add_Monster("Helena", "fire", "hp")),
        (16112, Add_Monster("Rica", "fire", "attack")),
        (20512, Add_Monster("Sekmet", "fire", "support")),
        (23512, Add_Monster("Masha", "fire", "attack")),
        (15712, Add_Monster("Juno", "fire", "support")),
        (16113, Add_Monster("Charlotte", "wind", "attack")),
        (15713, Add_Monster("Seara", "wind", "attack")),
        (17913, Add_Monster("Ethna", "wind", "attack")),
        (21513, Add_Monster("Diana", "wind", "hp")),
        (25213, Add_Monster("Momo", "wind", "attack")),
        (23115, Add_Monster("Beelzebub", "dark", "attack")),
        (19811, Add_Monster("Lapis", "water", "attack")),
        (10911, Add_Monster("Konomiya", "water", "support")),
        (15911, Add_Monster("Megan", "water", "support")),
        (17311, Add_Monster("Xiao_Lin", "water", "attack")),
        (11811, Add_Monster("Tyron", "water", "attack")),
        (21211, Add_Monster("Mo_Long", "water", "hp")),
        (14511, Add_Monster("Sigmarus", "water", "attack")),
        (18311, Add_Monster("Mihyang", "water", "support")),
        (19611, Add_Monster("Tetra", "water", "support")),
        (20711, Add_Monster("Chilling", "water", "attack")),
        (16311, Add_Monster("Rigel", "water", "support")),
        (19411, Add_Monster("Galleon", "water", "hp")),
        (10611, Add_Monster("Tarq", "water", "attack")),
        (22011, Add_Monster("Sabrina", "water", "attack")),
        (18011, Add_Monster("Orion", "water", "support")),
        (19211, Add_Monster("Theomars", "water", "attack")),
        (21911, Add_Monster("Talia", "water", "attack")),
        (16811, Add_Monster("Shi_Hou", "water", "attack")),
        (17411, Add_Monster("Chandra", "water", "hp")),
        (18111, Add_Monster("Malaka", "water", "attack")),
        (13911, Add_Monster("Julie", "water", "attack")),
        (19911, Add_Monster("Stella", "water", "attack")),
        (1000111, Add_Monster("Water_Homonculus", "water", "attack")),
        (18811, Add_Monster("Aegir", "water", "attack")),
        (22711, Add_Monster("Covenant", "water", "attack")),
        (22911, Add_Monster("Abigail", "water", "attack")),
        (23111, Add_Monster("Belial", "water", "attack")),
        (11031, Add_Monster("Icaru", "water", "def")),
        (20811, Add_Monster("Tractor", "water", "def")),
        (14031, Add_Monster("Vigor", "water", "hp")),
        (13231, Add_Monster("Lulu", "water", "support")),
        (14111, Add_Monster("Luer", "water", "support")),
        (25111, Add_Monster("Suiki", "water", "attack")),
        (18411, Add_Monster("Gildong", "water", "attack")),
        (13411, Add_Monster("Sian", "water", "attack")),
        (22611, Add_Monster("Bolverk", "water", "hp")),
        (10131, Add_Monster("Elucia","water", "support")),
        (24511, Add_Monster("Moore", "water", "attack")),
        (17011, Add_Monster("Ariel", "water", "support")),
        (23711, Add_Monster("Heagang", "water", "support")),
        (15031, Add_Monster("Mina", "water", "attack")),
        (24711, Add_Monster("Borgnine", "water", "hp")),
        (19711, Add_Monster("Poseidon", "water", "attack")),
        (21012, Add_Monster("Racuni", "fire", "support")),
        (12112, Add_Monster("Colleen", "fire", "Support")),
        (17412, Add_Monster("Kumar", "fire", "hp")),
        (11512, Add_Monster("Spectra", "fire", "support")),
        (21212, Add_Monster("Xiong_Fei", "fire", "defense")),
        (10512, Add_Monster("Lucasha", "fire", "attack")),
        (20812, Add_Monster("Bulldozer", "fire", "hp")),
        (15512, Add_Monster("Hwa", "fire", "attack")),
        (16312, Add_Monster("Antares", "fire", "attack")),
        (19212, Add_Monster("Tesarion", "fire", "hp")),
        (14712, Add_Monster("Verdehile", "fire", "attack")),
        (20412, Add_Monster("Khmun", "fire", "support")),
        (21812, Add_Monster("Ophilia", "fire", "hp")),
        (21912, Add_Monster("Shaina", "fire", "attack")),
        (12032, Add_Monster("Khali", "fire", "attack")),
        (21312, Add_Monster("Ludo", "fire", "attack")),
        (13512, Add_Monster("Garo", "fire", "attack")),
        (20112, Add_Monster("Lisa", "fire", "attack")),
        (15312, Add_Monster("Chloe", "fire", "support")),
        (18912, Add_Monster("Brandia", "fire", "attack")),
        (18312, Add_Monster("Hwahee", "fire", "attack")),
        (22612, Add_Monster("Baleygr", "fire", "attack")),
        (22212, Add_Monster("Bellenus", "fire", "defense")),
        (18012, Add_Monster("Draco", "fire", "support")),
        (11032, Add_Monster("Roaq", "fire", "attack")),
        (14512, Add_Monster("Perna", "fire", "hp")),
        (16812, Add_Monster("Mei_Hou_Wang", "fire", "defense")),
        (13912, Add_Monster("Clara", "fire", "attack")),
        (24112, Add_Monster("Ken", "fire", "attack")),
        (24012, Add_Monster("Fire_Ryu", "fire", "attack")),
        (19812, Add_Monster("Astar", "fire", "attack")),
        (10332, Add_Monster("Tatu", "fire", "attack")),
        (20212, Add_Monster("Sin", "fire", "defense")),
        (21112, Add_Monster("Daphnis", "fire", "attack")),
        (21412, Add_Monster("Harmonia", "fire", "support")),
        (13312, Add_Monster("Akia", "fire", "attack")),
        (22712, Add_Monster("Carcano", "fire", "attack")),
        (23912, Add_Monster("Hongyeon", "fire", "support")),
        (16032, Add_Monster("Sath", "fire", "attack")),
        (25112, Add_Monster("Kaki", "fire", "attack")),
        (25012, Add_Monster("Tomoe", "fire", "support")),
        (25412, Add_Monster("Robo_P27", "fire", "support")),
        (25212, Add_Monster("Coco", "fire", "attack")),
        (11533, Add_Monster("Bernard", "wind", "support")),
        (21313, Add_Monster("Morris", "wind", "support")),
        (18713, Add_Monster("Mav", "wind", "hp")),
        (20613, Add_Monster("Imesety", "wind", "support")),
        (16513, Add_Monster("Copper", "wind", "defense")),
        (13413, Add_Monster("Lushen", "wind", "attack")),
        (13513, Add_Monster("Orochi", "wind", "hp")),
        (18313, Add_Monster("Chasun", "wind", "support")),
        (21213, Add_Monster("Feng_Yan", "wind", "defense")),
        (22013, Add_Monster("Zenobia", "wind", "attack")),
        (16213, Add_Monster("Briand", "wind", "hp")),
        (19713, Add_Monster("Triton", "wind", "defense")),
        (11613, Add_Monster("Delphoi", "wind", "support")),
        (11813, Add_Monster("Shimitae", "wind", "wind")),
        (21913, Add_Monster("Melissa", "wind", "attack")),
        (13813, Add_Monster("Katarina", "wind", "attack")),
        (21413, Add_Monster("Triana", "wind", "support")),
        (17013, Add_Monster("Eladriel", "wind", "support")),
        (15513, Add_Monster("Yen", "wind", "attack")),
        (17313, Add_Monster("Ling_Ling", "wind", "attack")),
        (22413, Add_Monster("Skogul", "wind", "hp")),
        (14513, Add_Monster("Teshar", "wind", "attack")),
        (21113, Add_Monster("Ganymede", "wind", "support")),
        (24213, Add_Monster("Wind_M_Bison", "wind", "hp")),
        (18813, Add_Monster("Hraesvelg", "wind", "attack")),
        (18013, Add_Monster("Aquila", "wind", "attack")),
        (22113, Add_Monster("Mellia", "wind", "support")),
        (18913, Add_Monster("Tiana", "wind", "support")),
        (25113, Add_Monster("Fuuki", "wind", "hp")),
        (14613, Add_Monster("Lagmaron", "wind", "attack")),
        (10914, Add_Monster("Teon", "light", "support")),
        (11034, Add_Monster("Belladeon", "light", "defense")),
        (10514, Add_Monster("Kabilla", "light", "attack")),
        (15214, Add_Monster("Darion", "light", "defense")),
        (14914, Add_Monster("Lyn", "light", "attack")),
        (19114, Add_Monster("Fran", "light", "support")),
        (19214, Add_Monster("Elsharion", "light", "attack")),
        (21814, Add_Monster("Jeanne", "light", "hp")),
        (13714, Add_Monster("Ahman", "light", "hp")),
        (21914, Add_Monster("Deva", "light", "attack")),
        (15314, Add_Monster("Iona", "light", "support")),
        (13514, Add_Monster("Gin", "light", "attack")),
        (19314, Add_Monster("Loren", "light", "attack")),
        (22414, Add_Monster("Einheri", "light", "defense")),
        (14034, Add_Monster("Eshir", "light", "hp")),
        (18014, Add_Monster("Gemini", "light", "attack")),
        (11534, Add_Monster("Shamann", "light", "defense")),
        (23914, Add_Monster("Dongbaek", "light", "support")),
        (19215, Add_Monster("Veromos", "dark", "support")),
        (19815, Add_Monster("Lanett", "dark", "defense")),
        (15615, Add_Monster("Jamie", "dark", "attack")),
        (14035, Add_Monster("Jultan", "dark", "hp")),
        (19415, Add_Monster("Frigate", "dark", "support")),
        (1000215, Add_Monster("Dark_Homonculus", "dark", "support")),
        (23015, Add_Monster("Eirgar", "dark", "attack")),
        (11035, Add_Monster("Kro", "dark", "attack")),
        (15035, Add_Monster("Miho", "dark", "attack")),
        (20615, Add_Monster("Amduat", "dark", "support")),
        (13105, Add_Monster("Dark Sandman", "dark", "defense")),
        (10515, Add_Monster("Hellea", "dark", "attack")),
        (20015, Add_Monster("Karl", "dark", "attack")),
        (11815, Add_Monster("Aschubel", "dark", "attack"))
    ]),
    Artifacts = dict([
        (400, "S1_CD"),
        (401, "S2_CD"),
        (402, "S3_CD"),
        (403, "S4_CD"),
        (404, "S1_Recovery"),
        (405, "S2_Recovery"),
        (406, "S3_Recovery"),
        (407, "S1_ACC"),
        (408, "S2_ACC"),
        (409, "S3_ACC"),
        (302, "DMG_on_Wind"),
        (301, "DMG_on_Water"),
        (300, "DMG_on_Fire"),
        (303, "DMG_on_Light"),
        (304, "DMG_on_Dark"),
        (307, "DMG_from_Wind"),
        (306, "DMG_from_Water"),
        (305, "DMG_from_Fire"),
        (308, "DMG_from_Light"),
        (309, "DMG_from_Dark"),
        (222, "CD_as_HP_is_Good"),
        (223, "CD_as_HP_is_Bad"),
        (224, "Single_TGT_CD"),
        (200, "Lost_HP_ATK_up"),
        (201, "Lost_HP_DEF_up"),
        (202, "Lost_HP_SPD_up"),
        (204, "ATK_INC_Effect"),
        (206, "SPD_INC_Effect"),
        (205, "DEF_INC_Effect"),
        (208, "Counter_DMG"),
        (209, "Teamup_DMG"),
        (210, "Bomb_DMG"),
        (215, "Life_Drain"),
        (216, "HP_Revived"),
        (217, "ATK_Bar_Revived"),
        (218, "ADL_DMG_HP"),
        (219, "ADL_DMG_ATK"),
        (220, "ADL_DMG_DEF"),
        (221, "ADL_DMG_SPD"),
        (214, "CD_Recieved")
    ])
)

# print(Mapping_Dict)