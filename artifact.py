from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter import ttk
import ctypes
import csv
import json

ws = Tk()
ws.title('Artifact Tool')
# ws.geometry('400x300')

Monster_Info = {}
All_Monsters = []

f = open("MonstersDB.json", "r")
if (f.read() != ""):
    f.seek(0)
    Monster_Info = json.load(f)
f.close()


elements = ['-', 'fire','water', 'wind','light', 'dark']
types = ['-', 'attack', 'hp', 'def', 'support']

all_types = elements+types

subproperties = [
    ["S1 CD", "S2 CD", "S3 CD", "S4 CD"],
    ["S1 Recovery", "S2 Recovery", "S3 Recovery"],
    ["S1 ACC", "S2 ACC", "S3 ACC"],
    ["DMG on Wind", "DMG on Water", "DMG on Fire", "DMG on Light", "DMG on Dark"],
    ["DMG from Wind", "DMG from Water", "DMG from Fire", "DMG from Light", "DMG from Dark"],
    ["CD as HP is Good", "CD as HP is Bad", "Single TGT CD"],
    ["Lost HP ATK up", "Lost HP DEF up", "Lost HP SPD up"],
    ["ATK INC Effect", "SPD INC Effect", "DEF INC Effect"],
    ["Counter DMG", "Teamup DMG", "Bomb DMG"],
    ["Life Drain", "HP Revived", "ATK Bar Revived"],
    ["ADL DMG HP", "ADL DMG ATK", "ADL DMG DEF", "ADL DMG SPD"],
    ["CD Recieved"]
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

    return (calculate_efficiency(Monster_artifact))

# def calculate_efficiency(artifact, monster):


# label = Label(ws, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
cols = ('Monster', 'Sub1', 'Sub2', 'Sub3', 'Sub4', 'Current Efficiency', 'Max Efficiency')
listBox = ttk.Treeview(ws, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=10)

def update_List():
    All_Monsters.clear()
    # print(All_Monsters)
    listBox.delete(*listBox.get_children())
    for key in Monster_Info:
        listBox.insert("", "end", value=[key, "", "", "", "", str(Monster_Info[key]["Efficiency"]["Element"]) + " | " + str(Monster_Info[key]["Efficiency"]["Type"])])
        All_Monsters.append(key)

update_List()

def show():

    top= Toplevel(ws)
    top.title("Configure Artifact")

    # setting variable for Integers
    artifact_type = StringVar()
    artifact_type.set(elements[0])

    # creating widget
    elements_select = OptionMenu(
        top,
        artifact_type,
        *all_types,
    )

    # positioning widget
    Label(top, text = "Element or Type:").grid(row = 0, column = 0)
    elements_select.grid(row=0, column=1)


    # setting variable for Integers
    rolls_remaining = StringVar()
    rolls_remaining.set(4)

    # creating widget
    elements_select = OptionMenu(
        top,
        rolls_remaining,
        *[4, 3, 2, 1],
    )

    # positioning widget
    Label(top, text = "Rolls Remaining:").grid(row = 0, column = 2)
    elements_select.grid(row=0, column=3)

    # setting variable for Integers
    Sub1 = StringVar()
    Sub1.set(elements[0])

    # creating widget
    elements_select = OptionMenu(
        top,
        Sub1,
        *flat_subproperties,
    )

    # positioning widget
    Label(top, text = "Sub1").grid(row = 1, column = 0)
    elements_select.grid(row=1, column=1)

    sub1_value = StringVar()
    sub1_value.set(0)

    e1 = Entry(top, textvariable=sub1_value).grid(row = 1, column = 2)

    # setting variable for Integers
    Sub2 = StringVar()
    Sub2.set(elements[0])

    # creating widget
    elements_select = OptionMenu(
        top,
        Sub2,
        *flat_subproperties,
    )

    # positioning widget
    Label(top, text = "Sub2").grid(row = 2, column = 0)
    elements_select.grid(row=2, column=1)

    sub2_value = StringVar()
    sub2_value.set(0)
    e2 = Entry(top, textvariable=sub2_value).grid(row = 2, column = 2)


    # setting variable for Integers
    Sub3 = StringVar()
    Sub3.set(elements[0])

    # creating widget
    elements_select = OptionMenu(
        top,
        Sub3,
        *flat_subproperties,
    )

    # positioning widget
    Label(top, text = "Sub3").grid(row = 3, column = 0)
    elements_select.grid(row=3, column=1)

    sub3_value = StringVar()
    sub3_value.set(0)

    e3 = Entry(top, textvariable=sub3_value).grid(row = 3, column = 2)


    # setting variable for Integers
    Sub4 = StringVar()
    Sub4.set(elements[0])

    # creating widget
    elements_select = OptionMenu(
        top,
        Sub4,
        *flat_subproperties,
    )

    # positioning widget
    Label(top, text = "Sub4").grid(row = 4, column = 0)
    elements_select.grid(row=4, column=1)

    sub4_value = StringVar()
    sub4_value.set(0)

    e4 = Entry(top, textvariable=sub4_value).grid(row = 4, column = 2)


############################################################################################

    def find_monsters():
        Suitable_Monsters = []

        listbox_entry = []
        listbox_entry.append("Current Artifact")
        listbox_entry.append(Sub1.get() + " : " + sub1_value.get() + "%")
        listbox_entry.append(Sub2.get() + " : " + sub2_value.get() + "%")
        listbox_entry.append(Sub3.get() + " : " + sub3_value.get() + "%")
        listbox_entry.append(Sub4.get() + " : " + sub4_value.get() + "%")
            
        Suitable_Monsters.append(listbox_entry)


        for key in Monster_Info:
            if artifact_type.get() in elements:
                _artifact_type = "Element"
                _efficiency = Monster_Info[key]["Efficiency"]["Element"]
            elif artifact_type.get() in types:
                _artifact_type = "Type"
                _efficiency = Monster_Info[key]["Efficiency"]["Type"]
            if Monster_Info[key][_artifact_type] == artifact_type.get():
                Best_Case_Artifact = []
                if Sub1.get() in Monster_Info[key]["Substats"]:
                    Best_Case_Artifact.append([Sub1.get(), sub1_value.get()])
                if Sub2.get() in Monster_Info[key]["Substats"]:
                    Best_Case_Artifact.append([Sub2.get(), sub2_value.get()])
                if Sub3.get() in Monster_Info[key]["Substats"]:
                    Best_Case_Artifact.append([Sub3.get(), sub3_value.get()])
                if Sub4.get() in Monster_Info[key]["Substats"]:
                    Best_Case_Artifact.append([Sub4.get(), sub4_value.get()])
                
                max_efficiency = calculate_efficiency(Best_Case_Artifact) + (rolls_remaining.get()/8*100)
                if max_efficiency > _efficiency:
                    listbox_entry = []
                    listbox_entry.append(key)
                    for subs in Monster_Info[key]["Artifacts"][_artifact_type]:
                        listbox_entry.append(subs[0] + " : " + subs[1] + "%")
                    listbox_entry.append(_efficiency)
                    listbox_entry.append(max_efficiency)
                    Suitable_Monsters.append(listbox_entry)

        # Suitable_Monsters = Suitable_Monsters4 + Suitable_Monsters3 + Suitable_Monsters2
        # print(Suitable_Monsters)

        # tempList = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]
        # tempList.sort(key=lambda e: e[1], reverse=True)

        listBox.delete(*listBox.get_children())
        for i in Suitable_Monsters:
            listBox.insert("", "end", values=i)

        top.destroy()

    Button(top, text="Find Monsters", width=15, command=find_monsters).grid(row=5, column=0)


def open_add_build():
    row_counter = 0

    #Create a Button to Open the Toplevel Window
    top= Toplevel(ws)
    top.title("Add Monster")

    Monster_name = StringVar()

    Label(top, text= "Monster Name:").grid(row = row_counter, column = 0)
    e1 = Entry(top, textvariable=Monster_name).grid(row = row_counter, column = 1)
    row_counter = row_counter + 1

    Element = StringVar()
    Element.set(elements[0])

    # setting variable for Integers
    variable = StringVar()

    # creating widget
    elements_select = OptionMenu(
    top,
    Element,
    *elements
    )

    Label(top, text = "Element:").grid(row = row_counter, column = 0)
    # positioning widget
    elements_select.grid(row = row_counter, column = 1)
    row_counter = row_counter + 1

    # setting variable for Integers
    Type = StringVar()
    Type.set(types[0])

    # creating widget
    types_select = OptionMenu(
    top,
    Type,
    *types
    )

    # positioning widget
    Label(top, text = "Type:").grid(row = row_counter, column = 0)
    types_select.grid(row = row_counter, column = 1)
    row_counter = row_counter + 1

    # var1 = IntVar()
    # var2 = IntVar()
    # c1 = Checkbutton(top, text='Python',variable=var1, onvalue=1, offvalue=0)
    # c1.pack()
    # c2 = Checkbutton(top, text='C++',variable=var2, onvalue=1, offvalue=0)
    # c2.pack()

    artifact_properties = []
    artifact_checkboxes = []

    counter = 0
    for groups in subproperties:
        column_counter = 0
        for subproperty in groups:
            v = IntVar()
            var = IntVar()
            c = Checkbutton(top, text=subproperty,variable=v, onvalue=1, offvalue=0)
            c.grid(row = row_counter, column = column_counter)
            artifact_properties.append(v)
            artifact_checkboxes.append(c)
            column_counter = column_counter + 1
            counter = counter + 1
        row_counter = row_counter + 1

    def save_monster(Monster_name, Element, Type, artifact_properties):
        Current_Monster = {}
        data = []
        substats = []
        for i in artifact_properties:
            data.append(i.get())

        for i in range(len(data)):
            if data[i] == 1:
                substats.append(flat_subproperties[i])

        # Current_Monster["Monster"] = Monster_name.get()
        Current_Monster["Element"] = Element.get()
        Current_Monster["Type"] = Type.get()
        Current_Monster["Substats"] = substats
        Current_Monster["Artifacts"] = {}
        Current_Monster["Artifacts"]["Element"] = []
        Current_Monster["Artifacts"]["Type"] = []
        Current_Monster["Efficiency"] = {}
        Current_Monster["Efficiency"]["Element"] = 0
        Current_Monster["Efficiency"]["Type"] = 0
        
        Monster_Info[Monster_name.get()] = Current_Monster

        update_List()

        top.destroy()

    save = Button(top, text = "save", command = lambda: save_monster(Monster_name, Element, Type, artifact_properties)).grid(row = row_counter)

    top.mainloop()

def open_update_monster():
    row_counter = 0

    if listBox.focus() == "":
        Selected_Monster = All_Monsters[0]
    else:
        Selected_Monster = listBox.item(listBox.focus())['values'][0]

    #Create a Button to Open the Toplevel Window
    top = Toplevel(ws)
    top.title("Check Build")

    # setting variable for Integers
    Artifact_Category = StringVar()
    Monster = StringVar()

    Label(top, text="Monster:").grid(row = row_counter, column = 0)
    Monster_Select = ttk.Combobox(top, textvariable=Monster)
    Monster_Select.grid(row = row_counter, column = 1)

    elements_select = OptionMenu(
        top,
        Artifact_Category,
        *["Element", "Type"],
    )

    # positioning widget
    Artifact_Category.set("Element")
    Label(top, text="Artifact_Category:").grid(row = row_counter, column = 2)
    elements_select.grid(row=row_counter, column=3)

    row_counter = row_counter + 1

    cols = ('Monster', 'Sub1', 'Sub2', 'Sub3', 'Sub4', 'Efficiency')
    Current_Artifact_List = ttk.Treeview(top, columns=cols, show='headings')
    curr_list_values = []

    for col in cols:
        Current_Artifact_List.heading(col, text=col)    
    Current_Artifact_List.grid(row=row_counter, column=0, columnspan=10)
    row_counter = row_counter + 1

    def update_tree(data):
        Current_Artifact_List.delete(*Current_Artifact_List.get_children())
        for i in data:
            tree_values = []
            tree_values.append(i)
            Category = Artifact_Category.get()
            for subs in Monster_Info[i]["Artifacts"][Category]:
                tree_values.append(subs[0] + " : " + subs[1] + "%")
            tree_values.append(Monster_Info[i]["Efficiency"][Category])
            Current_Artifact_List.insert("", "end", values=tree_values)

    
        

    def checkkey(*args):
        
        value = Monster.get()
        print(value)
        
        # get data from l
        if value == '':
            curr_list_values = All_Monsters
        else:
            curr_list_values = []
            for item in All_Monsters:
                if value.lower() in item.lower():
                    curr_list_values.append(item)                
    
        # update data in listbox
        Monster_Select['values'] = curr_list_values
        update_tree(curr_list_values)
    
    
    #creating text box 
   
    # Monster_Select.bind('<KeyRelease>', checkkey)
    Monster.trace("w", checkkey)
    Artifact_Category.trace("w", checkkey)
    Monster.set(Selected_Monster)
    print(Selected_Monster)
    update_tree([Selected_Monster])
    
    # elements_select.bind('<FocusOut>', checkkey)
    
    def add_artifacts():
        add_artifacts_level = Toplevel(top)
        if Current_Artifact_List.focus() != "":
            Monster_to_Modify = Current_Artifact_List.item(Current_Artifact_List.focus())['values'][0]
        else:
            ctypes.windll.user32.MessageBoxW(0, "Please Select a Monster", "error", 1)
            add_artifacts_level.destroy() 

        Monster_Type = Artifact_Category.get()

        # setting variable for Integers
        Sub1 = StringVar()

        # creating widget
        elements_select = OptionMenu(
            add_artifacts_level,
            Sub1,
            *flat_subproperties,
        )

        # positioning widget
        Label(add_artifacts_level, text = "Sub1").grid(row = 1, column = 0)
        elements_select.grid(row=1, column=1)

        sub1_value = StringVar()
        sub1_value.set(0)

        e1 = Entry(add_artifacts_level, textvariable=sub1_value).grid(row = 1, column = 2)

        # setting variable for Integers
        Sub2 = StringVar()

        # creating widget
        elements_select = OptionMenu(
            add_artifacts_level,
            Sub2,
            *flat_subproperties,
        )

        # positioning widget
        Label(add_artifacts_level, text = "Sub2").grid(row = 2, column = 0)
        elements_select.grid(row=2, column=1)

        sub2_value = StringVar()
        sub2_value.set(0)
        e2 = Entry(add_artifacts_level, textvariable=sub2_value).grid(row = 2, column = 2)


        # setting variable for Integers
        Sub3 = StringVar()
        

        # creating widget
        elements_select = OptionMenu(
            add_artifacts_level,
            Sub3,
            *flat_subproperties,
        )
        
        # positioning widget
        Label(add_artifacts_level, text = "Sub3").grid(row = 3, column = 0)
        elements_select.grid(row=3, column=1)

        sub3_value = StringVar()
        sub3_value.set(0)

        e3 = Entry(add_artifacts_level, textvariable=sub3_value).grid(row = 3, column = 2)


        # setting variable for Integers
        Sub4 = StringVar()
        

        # creating widget
        elements_select = OptionMenu(
            add_artifacts_level,
            Sub4,
            *flat_subproperties,
        )
        
        # positioning widget
        Label(add_artifacts_level, text = "Sub4").grid(row = 4, column = 0)
        elements_select.grid(row=4, column=1)

        sub4_value = StringVar()
        sub4_value.set(0)

        e4 = Entry(add_artifacts_level, textvariable=sub4_value).grid(row = 4, column = 2)

        def Apply_Artifact():
            artifact_info = []
            artifact_info.append([Sub1.get(), sub1_value.get()])
            artifact_info.append([Sub2.get(), sub2_value.get()])
            artifact_info.append([Sub3.get(), sub3_value.get()])
            artifact_info.append([Sub4.get(), sub4_value.get()])
            Monster_Info[Monster_to_Modify]["Artifacts"][Monster_Type] = artifact_info
            Monster_Info[Monster_to_Modify]["Efficiency"][Monster_Type] = monster_efficiency(Monster_to_Modify, artifact_info)
            checkkey()
            add_artifacts_level.destroy()

        Button(add_artifacts_level, text="Apply", width=15, command=Apply_Artifact).grid(row=5, column=0)

    Button(top, text="Change Artifacts", width=15, command=add_artifacts).grid(row=row_counter, column=0)
    top.mainloop()


Button(ws, text="Input Artifact", width=15, command=show).grid(row=4, column=0)

# Label(ws, text= "Click the button to Open Popup Window", font= ('Helvetica 18')).place(relx=.5, rely=.5, anchor= CENTER)
Button(ws, text= "Add Build", background= "white", foreground= "blue", font= ('Helvetica 13 bold'), command= open_add_build).grid(row=4, column=1)
Button(ws, text= "Update Monster", background= "white", foreground= "blue", font= ('Helvetica 13 bold'), command= open_update_monster).grid(row=4, column=2)

def on_closing():
    f = open("MonstersDB.json", "w")
    json.dump(Monster_Info, f, indent = 6)
    f.close()
    ws.destroy()

ws.protocol("WM_DELETE_WINDOW", on_closing)
# infinite loop 
ws.mainloop()