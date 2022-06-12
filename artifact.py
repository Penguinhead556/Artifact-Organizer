from artifact_h import *

Monster_Info = {}
Inventory_data = {}
All_Monsters = []
Monster_Info, Inventory_data = initialize_data()

ws = Tk()
ws.title('Artifact Tool')

Label(ws, text = "Artifact Index:").grid(row = 0, column = 0)

type_label = StringVar()
type_label.set("Type is: -")
Label(ws, textvariable = type_label).grid(row = 0, column = 4)


Artifact_Index = StringVar()
Artifact_Index.set(0)
e2 = Entry(ws, textvariable=Artifact_Index).grid(row = 0, column = 1)


# setting variable for Integers
rolls_remaining = StringVar()
rolls_remaining.set(0)

# setting variable for Integers
artifact_type = StringVar()
artifact_type.set(elements[0])

# setting variable for Integers
Sub1 = StringVar()
Sub1.set("")

sub1_value = StringVar()
sub1_value.set(0)

# setting variable for Integers
Sub2 = StringVar()
Sub2.set("")

sub2_value = StringVar()
sub2_value.set(0)

# setting variable for Integers
Sub3 = StringVar()
Sub3.set("")

sub3_value = StringVar()
sub3_value.set(0)

# setting variable for Integers
Sub4 = StringVar()
Sub4.set("")

sub4_value = StringVar()
sub4_value.set(0)

def find_monsters(subproperties, type, rolls):
    output = []

    listbox_entry = []
    listbox_entry.append("Current Artifact")

    artifact_type.set(type)

    if 1 <= len(subproperties):
        listbox_entry.append(subproperties[0])
        Sub1.set(subproperties[0][0])
        sub1_value.set(subproperties[0][1])
    else:
        listbox_entry.append("")
        Sub1.set("")
        sub1_value.set(0)

    if 2 <= len(subproperties):
        listbox_entry.append(subproperties[1])
        Sub2.set(subproperties[1][0])
        sub2_value.set(subproperties[1][1])
    else:
        listbox_entry.append("")
        Sub2.set("")
        sub2_value.set(0)

    if 3 <= len(subproperties):
        listbox_entry.append(subproperties[2])
        Sub3.set(subproperties[2][0])
        sub3_value.set(subproperties[2][1])
    else:
        listbox_entry.append("")
        Sub3.set("")
        sub3_value.set(0)

    if 4 <= len(subproperties):
        listbox_entry.append(subproperties[3])
        Sub4.set(subproperties[3][0])
        sub4_value.set(subproperties[3][1])
    else:
        listbox_entry.append("")
        Sub4.set("")
        sub4_value.set(0)

    listbox_entry.append(calculate_efficiency(subproperties))
    listbox_entry.append(calculate_efficiency(subproperties) + (rolls/8*100))
        
    output.append(listbox_entry)


    for key in Monster_Info:
        if type in elements:
            _artifact_type = "Element"
            _efficiency = Monster_Info[key]["Efficiency"]["Element"]
        elif type in types:
            _artifact_type = "Type"
            _efficiency = Monster_Info[key]["Efficiency"]["Type"]
        if Monster_Info[key][_artifact_type] == type:
            Best_Case_Artifact = []
            for curr_sub in subproperties:
                print(key)
                if curr_sub[0] in Monster_Info[key]["Substats"]:
                    Best_Case_Artifact.append(curr_sub)
            
            if Best_Case_Artifact != []:
                max_efficiency = calculate_efficiency(Best_Case_Artifact) + (rolls/8*100)
            else:
                max_efficiency = 0
            if max_efficiency > _efficiency and max_efficiency > 70:
                listbox_entry = []
                listbox_entry.append(key)
                for subs in Monster_Info[key]["Artifacts"][_artifact_type]:
                    listbox_entry.append(subs[0] + " : " + subs[1] + "%")
                while len(listbox_entry) < 5:
                    listbox_entry.append("")
                listbox_entry.append(_efficiency)
                listbox_entry.append(max_efficiency)
                output.append(listbox_entry)
                
    
    return output

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


def load():
    type_label.set("Type is: " + Inventory_data[int(Artifact_Index.get())]["type"])

    Suitable_Monsters = find_monsters(Inventory_data[int(Artifact_Index.get())]["subproperties"], Inventory_data[int(Artifact_Index.get())]["type"], Inventory_data[int(Artifact_Index.get())]["Rolls"])

    Suitable_Monsters.sort(key = lambda Suitable_Monsters: Suitable_Monsters[6], reverse = True)

    listBox.delete(*listBox.get_children())
    for i in Suitable_Monsters:
        listBox.insert("", "end", values=i)

def next():
    Artifact_Index.set(int(Artifact_Index.get()) + 1)
    load()

def Button_Load_JSON():
    global Monster_Info
    load_json(Monster_Info)
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
    update_List()

def show():

    top= Toplevel(ws)
    top.title("Configure Artifact")


    # creating widget
    elements_select = OptionMenu(
        top,
        artifact_type,
        *all_types,
    )

    # positioning widget
    Label(top, text = "Element or Type:").grid(row = 0, column = 0)
    elements_select.grid(row=0, column=1)


    # creating widget
    elements_select = OptionMenu(
        top,
        rolls_remaining,
        *[4, 3, 2, 1, 0],
    )

    # positioning widget
    Label(top, text = "Rolls Remaining:").grid(row = 0, column = 2)
    elements_select.grid(row=0, column=3)

    # creating widget
    elements_select = OptionMenu(
        top,
        Sub1,
        *flat_subproperties,
    )

    # positioning widget
    Label(top, text = "Sub1").grid(row = 1, column = 0)
    elements_select.grid(row=1, column=1)


    e1 = Entry(top, textvariable=sub1_value).grid(row = 1, column = 2)

    # creating widget
    elements_select = OptionMenu(
        top,
        Sub2,
        *flat_subproperties,
    )

    # positioning widget
    Label(top, text = "Sub2").grid(row = 2, column = 0)
    elements_select.grid(row=2, column=1)


    e2 = Entry(top, textvariable=sub2_value).grid(row = 2, column = 2)

    # creating widget
    elements_select = OptionMenu(
        top,
        Sub3,
        *flat_subproperties,
    )

    # positioning widget
    Label(top, text = "Sub3").grid(row = 3, column = 0)
    elements_select.grid(row=3, column=1)

    e3 = Entry(top, textvariable=sub3_value).grid(row = 3, column = 2)

    # creating widget
    elements_select = OptionMenu(
        top,
        Sub4,
        *flat_subproperties,
    )

    # positioning widget
    Label(top, text = "Sub4").grid(row = 4, column = 0)
    elements_select.grid(row=4, column=1)

    e4 = Entry(top, textvariable=sub4_value).grid(row = 4, column = 2)

############################################################################################

    def display_Monsters():
        

        subproperties = []
        if Sub1.get() != "":
            subproperties.append([Sub1.get(), sub1_value.get()])
        if Sub2.get() != "":
            subproperties.append([Sub2.get(), sub2_value.get()])
        if Sub3.get() != "":
            subproperties.append([Sub3.get(), sub3_value.get()])
        if Sub4.get() != "":
            subproperties.append([Sub4.get(), sub4_value.get()])


        Suitable_Monsters = find_monsters(subproperties, artifact_type.get(), int(rolls_remaining.get()))

        Suitable_Monsters.sort(key = lambda Suitable_Monsters: Suitable_Monsters[6], reverse = True)

        listBox.delete(*listBox.get_children())
        for i in Suitable_Monsters:
            listBox.insert("", "end", values=i)

        type_label.set("Type is: " + artifact_type.get())

        top.destroy()

    Button(top, text="Find Monsters", width=15, command=display_Monsters).grid(row=5, column=0)


def Inventory():
    top= Toplevel(ws)
    top.title("Configure Artifact")

    cols = ('ID', 'Type', 'Sub1', 'Sub2', 'Sub3', 'Sub4', 'Current Efficiency', 'Max Efficiency')
    Inventory_Listbox = ttk.Treeview(top, columns=cols, show='headings')

    for col in cols:
        Inventory_Listbox.heading(col, text=col)    
    Inventory_Listbox.grid(row=0, column=0, columnspan=10)

    Ndex = 0
    for Art in Inventory_data:
        inv_box_values = []
        inv_box_values.append(str(Ndex))
        inv_box_values.append(Art["type"])
        for i in range(4):
            if i < len(Art["subproperties"]):
                inv_box_values.append(Art["subproperties"][i])
            else:
                inv_box_values.append("")
        _efficiency = calculate_efficiency(Art["subproperties"])
        inv_box_values.append(str(_efficiency))
        inv_box_values.append(str(_efficiency + Art["Rolls"] * 12.5))

        Inventory_Listbox.insert("", "end", value = inv_box_values)

        Ndex = Ndex + 1


    def display_Monsters():
        if Inventory_Listbox.focus() == "":
            ctypes.windll.user32.MessageBoxW(0, "Please Select a Monster", "error", 1)
        else:
            Selected_Artifact = Inventory_data[int(Inventory_Listbox.item(Inventory_Listbox.focus())['values'][0])]

        Artifact_Index.set(Inventory_Listbox.item(Inventory_Listbox.focus())['values'][0])
        
        Suitable_Monsters = find_monsters(Selected_Artifact["subproperties"], Selected_Artifact["type"], Selected_Artifact["Rolls"])

        Suitable_Monsters.sort(key = lambda Suitable_Monsters: Suitable_Monsters[6], reverse = True)

        listBox.delete(*listBox.get_children())
        for i in Suitable_Monsters:
            listBox.insert("", "end", values=i)

        type_label.set("Type is: " + Selected_Artifact["type"])

        top.destroy()

    Button(top, text="Find Monsters", width=15, command=display_Monsters).grid(row=5, column=0)


def open_add_build():
    top = Toplevel(ws)

    MonsterPage = Configure_Monsters(top, "", "", "", [])

    def save_monster():
        Monster_Info.update(MonsterPage.save())
        update_List()
        top.destroy()

    Button(top, text = "save", command = save_monster).grid(row = top.grid_size()[1])

def open_update_monster():

    if listBox.focus() == "":
        Selected_Monster = All_Monsters[0]
    else:
        Selected_Monster = listBox.item(listBox.focus())['values'][0]

    top = Toplevel(ws)

    Original_Monster = Selected_Monster

    # print(Monster_Info["21813"])

    subs = []
    if "Substats" in Monster_Info[Selected_Monster]:
        subs = Monster_Info[Selected_Monster]["Substats"]
    MonsterPage = Configure_Monsters(top, Selected_Monster, Monster_Info[Selected_Monster]["Element"], Monster_Info[Selected_Monster]["Type"], subs)

    def save_monster():
        
        saved_Monster = MonsterPage.save()
        if Original_Monster not in saved_Monster:
            Monster_Info[saved_Monster]["Artifacts"] = {}
            Monster_Info[saved_Monster]["Artifacts"]["Element"] = Monster_Info[Original_Monster]["Artifacts"]["Element"]
            Monster_Info[saved_Monster]["Artifacts"]["Type"] = Monster_Info[Original_Monster]["Artifacts"]["Type"]
            Monster_Info[saved_Monster]["Efficiency"] = Monster_Info[Original_Monster]["Efficiency"]
            Monster_Info[saved_Monster]["Efficiency"]["Element"] = Monster_Info[Original_Monster]["Efficiency"]["Element"]
            Monster_Info[saved_Monster]["Efficiency"]["Type"] = Monster_Info[Original_Monster]["Efficiency"]["Type"]
            del Monster_Info[Original_Monster]
        else:
            Monster_Info[Original_Monster]["Substats"] = saved_Monster[Original_Monster]["Substats"]
        update_List()
        top.destroy()

    Button(top, text = "save", command = save_monster).grid(row = top.grid_size()[1])


    # row_counter = 0

    # if listBox.focus() == "":
    #     Selected_Monster = All_Monsters[0]
    # else:
    #     Selected_Monster = listBox.item(listBox.focus())['values'][0]

    # #Create a Button to Open the Toplevel Window
    # top = Toplevel(ws)
    # top.title("Check Build")

    # # setting variable for Integers
    # Artifact_Category = StringVar()
    # Monster = StringVar()

    # Label(top, text="Monster:").grid(row = row_counter, column = 0)
    # Monster_Select = ttk.Combobox(top, textvariable=Monster)
    # Monster_Select.grid(row = row_counter, column = 1)

    # elements_select = OptionMenu(
    #     top,
    #     Artifact_Category,
    #     *["Element", "Type"],
    # )

    # # positioning widget
    # Artifact_Category.set("Element")
    # Label(top, text="Artifact_Category:").grid(row = row_counter, column = 2)
    # elements_select.grid(row=row_counter, column=3)

    # row_counter = row_counter + 1

    # cols = ('Monster', 'Sub1', 'Sub2', 'Sub3', 'Sub4', 'Efficiency')
    # Current_Artifact_List = ttk.Treeview(top, columns=cols, show='headings')
    # curr_list_values = []

    # for col in cols:
    #     Current_Artifact_List.heading(col, text=col)    
    # Current_Artifact_List.grid(row=row_counter, column=0, columnspan=10)
    # row_counter = row_counter + 1

    # def update_tree(data):
    #     Current_Artifact_List.delete(*Current_Artifact_List.get_children())
    #     for i in data:
    #         tree_values = []
    #         tree_values.append(i)
    #         Category = Artifact_Category.get()
    #         for subs in Monster_Info[i]["Artifacts"][Category]:
    #             tree_values.append(subs[0] + " : " + subs[1] + "%")
    #         tree_values.append(Monster_Info[i]["Efficiency"][Category])
    #         Current_Artifact_List.insert("", "end", values=tree_values)

    
        

    # def checkkey(*args):
        
    #     value = Monster.get()
    #     print(value)
        
    #     # get data from l
    #     if value == '':
    #         curr_list_values = All_Monsters
    #     else:
    #         curr_list_values = []
    #         for item in All_Monsters:
    #             if value.lower() in item.lower():
    #                 curr_list_values.append(item)                
    
    #     # update data in listbox
    #     Monster_Select['values'] = curr_list_values
    #     update_tree(curr_list_values)
    
    
    # #creating text box 
   
    # # Monster_Select.bind('<KeyRelease>', checkkey)
    # Monster.trace("w", checkkey)
    # Artifact_Category.trace("w", checkkey)
    # Monster.set(Selected_Monster)
    # print(Selected_Monster)
    # update_tree([Selected_Monster])
    
    # # elements_select.bind('<FocusOut>', checkkey)
    
    # def add_artifacts():
    #     add_artifacts_level = Toplevel(top)
    #     if Current_Artifact_List.focus() != "":
    #         Monster_to_Modify = Current_Artifact_List.item(Current_Artifact_List.focus())['values'][0]
    #     else:
    #         ctypes.windll.user32.MessageBoxW(0, "Please Select a Monster", "error", 1)
    #         add_artifacts_level.destroy() 

    #     Monster_Type = Artifact_Category.get()

    #     # setting variable for Integers
    #     Sub1 = StringVar()

    #     # creating widget
    #     elements_select = OptionMenu(
    #         add_artifacts_level,
    #         Sub1,
    #         *flat_subproperties,
    #     )

    #     # positioning widget
    #     Label(add_artifacts_level, text = "Sub1").grid(row = 1, column = 0)
    #     elements_select.grid(row=1, column=1)

    #     sub1_value = StringVar()
    #     sub1_value.set(0)

    #     e1 = Entry(add_artifacts_level, textvariable=sub1_value).grid(row = 1, column = 2)

    #     # setting variable for Integers
    #     Sub2 = StringVar()

    #     # creating widget
    #     elements_select = OptionMenu(
    #         add_artifacts_level,
    #         Sub2,
    #         *flat_subproperties,
    #     )

    #     # positioning widget
    #     Label(add_artifacts_level, text = "Sub2").grid(row = 2, column = 0)
    #     elements_select.grid(row=2, column=1)

    #     sub2_value = StringVar()
    #     sub2_value.set(0)
    #     e2 = Entry(add_artifacts_level, textvariable=sub2_value).grid(row = 2, column = 2)


    #     # setting variable for Integers
    #     Sub3 = StringVar()
        

    #     # creating widget
    #     elements_select = OptionMenu(
    #         add_artifacts_level,
    #         Sub3,
    #         *flat_subproperties,
    #     )
        
    #     # positioning widget
    #     Label(add_artifacts_level, text = "Sub3").grid(row = 3, column = 0)
    #     elements_select.grid(row=3, column=1)

    #     sub3_value = StringVar()
    #     sub3_value.set(0)

    #     e3 = Entry(add_artifacts_level, textvariable=sub3_value).grid(row = 3, column = 2)


    #     # setting variable for Integers
    #     Sub4 = StringVar()
        

    #     # creating widget
    #     elements_select = OptionMenu(
    #         add_artifacts_level,
    #         Sub4,
    #         *flat_subproperties,
    #     )
        
    #     # positioning widget
    #     Label(add_artifacts_level, text = "Sub4").grid(row = 4, column = 0)
    #     elements_select.grid(row=4, column=1)

    #     sub4_value = StringVar()
    #     sub4_value.set(0)

    #     e4 = Entry(add_artifacts_level, textvariable=sub4_value).grid(row = 4, column = 2)

    #     def Apply_Artifact():
    #         artifact_info = []
    #         artifact_info.append([Sub1.get(), sub1_value.get()])
    #         artifact_info.append([Sub2.get(), sub2_value.get()])
    #         artifact_info.append([Sub3.get(), sub3_value.get()])
    #         artifact_info.append([Sub4.get(), sub4_value.get()])
    #         Monster_Info[Monster_to_Modify]["Artifacts"][Monster_Type] = artifact_info
    #         Monster_Info[Monster_to_Modify]["Efficiency"][Monster_Type] = monster_efficiency(Monster_to_Modify, artifact_info)
    #         checkkey()
    #         add_artifacts_level.destroy()

    #     Button(add_artifacts_level, text="Apply", width=15, command=Apply_Artifact).grid(row=5, column=0)

    # Button(top, text="Change Artifacts", width=15, command=add_artifacts).grid(row=row_counter, column=0)
    # top.mainloop()

Button(ws, text="Load", width=15, command=load).grid(row=0, column=2)
Button(ws, text="Next", width=15, command=next).grid(row=0, column=3)


Button(ws, text="Load JSON", width=15, command=Button_Load_JSON).grid(row=4, column=0)
Button(ws, text="Input Artifact", width=15, command=show).grid(row=4, column=1)
Button(ws, text="Inventory", width=15, command=Inventory).grid(row=4, column=2)
Button(ws, text="Add Build", command= open_add_build).grid(row=4, column=3)
Button(ws, text="Update Monster", command= open_update_monster).grid(row=4, column=4)

def on_closing():
    f = open("MonstersDB.json", "w")
    json.dump(Monster_Info, f, indent = 6)
    f.close()
    ws.destroy()

ws.protocol("WM_DELETE_WINDOW", on_closing)
# infinite loop 
ws.mainloop()