from artifact_h import *

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

class Configure_Monsters:
    def __init__(self, top_handle, monster, element, type, substats):
        self.substats = substats
        self.Original_Monster = monster

        #Create a Button to Open the Toplevel Window
        
        top_handle.title("Add Monster")

        self.Monster_name = StringVar()
        self.Element = StringVar()
        self.Type = StringVar()
        self.Monster_name.set(monster)
        self.Element.set(element)
        self.Type.set(type)

        row_counter = 0
    
        Label(top_handle, text= "Monster Name:").grid(row = row_counter, column = 0)
        e1 = Entry(top_handle, textvariable=self.Monster_name).grid(row = row_counter, column = 1)
        row_counter = row_counter + 1

        # creating widget
        elements_select = OptionMenu(
        top_handle,
        self.Element,
        *elements
        )


        Label(top_handle, text = "Element:").grid(row = row_counter, column = 0)
        # positioning widget
        elements_select.grid(row = row_counter, column = 1)
        row_counter = row_counter + 1


         # creating widget
        types_select = OptionMenu(
        top_handle,
        self.Type,
        *types
        )

        # positioning widget
        Label(top_handle, text = "Type:").grid(row = row_counter, column = 0)
        types_select.grid(row = row_counter, column = 1)
        row_counter = row_counter + 1

        # setting variable for Integers
        self.artifact_properties = []
        self.artifact_checkboxes = []

        for groups in subproperties:
            column_counter = 0
            for subproperty in groups:
                v = IntVar()
                c = Checkbutton(top_handle, text=subproperty,variable=v, onvalue=1, offvalue=0)
                c.grid(row = row_counter, column = column_counter)
                if subproperty in self.substats:
                    c.select()
                    print(v.get())
                    print(subproperty)
                self.artifact_properties.append(v)
                self.artifact_checkboxes.append(c)
                column_counter = column_counter + 1
            row_counter = row_counter + 1

    def save(self):
        Current_Monster = {}
        data = []
        substats = []
        for i in self.artifact_properties:
            data.append(i.get())

        for i in range(len(data)):
            if data[i] == 1:
                substats.append(flat_subproperties[i])

        # Current_Monster["Monster"] = Monster_name.get()
        Current_Monster["Element"] = self.Element.get()
        Current_Monster["Type"] = self.Type.get()
        Current_Monster["Substats"] = substats
        
        
        print ({self.Monster_name.get() : Current_Monster})
        return {self.Monster_name.get() : Current_Monster}

        

        

        
