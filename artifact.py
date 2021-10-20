from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
import json

ws = Tk()
ws.title('Artifact Tool')
# ws.geometry('400x300')

Monster_Info = {}

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


# def calculate_efficiency(artifact, monster):


# label = Label(ws, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
cols = ('Monster', 'Sub1', 'Sub2', 'Sub3', 'Sub4', 'Current Efficiency', 'Max Efficiency')
listBox = ttk.Treeview(ws, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=10)


listBox.delete(*listBox.get_children())
for key in Monster_Info:
    listBox.insert("", "end", value=key)

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
        command=display_selected
    )

    # positioning widget
    Label(top, text = "Element or Type:").grid(row = 0, column = 0)
    elements_select.grid(row=0, column=1)


    # setting variable for Integers
    Sub1 = StringVar()
    Sub1.set(elements[0])

    # creating widget
    elements_select = OptionMenu(
        top,
        Sub1,
        *flat_subproperties,
        command=display_selected
    )

    # positioning widget
    Label(top, text = "Sub1").grid(row = 1, column = 0)
    elements_select.grid(row=1, column=1)

    sub1_value = StringVar()
    sub1_value.set(elements[0])

    e1 = Entry(top, textvariable=sub1_value).grid(row = 1, column = 2)

    # setting variable for Integers
    Sub2 = StringVar()

    # creating widget
    elements_select = OptionMenu(
        top,
        Sub2,
        *flat_subproperties,
        command=display_selected
    )

    # positioning widget
    Label(top, text = "Sub2").grid(row = 2, column = 0)
    elements_select.grid(row=2, column=1)

    sub2_value = StringVar()
    e2 = Entry(top, textvariable=sub2_value).grid(row = 2, column = 2)


    # setting variable for Integers
    Sub3 = StringVar()

    # creating widget
    elements_select = OptionMenu(
        top,
        Sub3,
        *flat_subproperties,
        command=display_selected
    )

    # positioning widget
    Label(top, text = "Sub3").grid(row = 3, column = 0)
    elements_select.grid(row=3, column=1)

    sub3_value = StringVar()

    e3 = Entry(top, textvariable=sub3_value).grid(row = 3, column = 2)


    # setting variable for Integers
    Sub4 = StringVar()

    # creating widget
    elements_select = OptionMenu(
        top,
        Sub4,
        *flat_subproperties,
        command=display_selected
    )

    # positioning widget
    Label(top, text = "Sub4").grid(row = 4, column = 0)
    elements_select.grid(row=4, column=1)

    sub4_value = StringVar()

    e4 = Entry(top, textvariable=sub4_value).grid(row = 4, column = 2)


#############################################################################################
    Monster_info = []
    with open('MonstersDB.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            Monster_info.append(row)

    Suitable_Monsters = []
    Suitable_Monsters4 = []
    Suitable_Monsters3 = []
    Suitable_Monsters2 = []

    for Monster in Monster_info:
        if artifact_type.get() in Monster:
            Monster_Display = []
            # print(Monster[0])
            Monster_Display.append(Monster[0])
            matching_properties = 0
            if Sub1.get() in Monster:
                matching_properties = matching_properties + 1
                Monster_Display.append(Sub1.get())
            if Sub2.get() in Monster:
                matching_properties = matching_properties + 1
                Monster_Display.append(Sub2.get())
            if Sub3.get() in Monster:
                matching_properties = matching_properties + 1
                Monster_Display.append(Sub3.get())
            if Sub4.get() in Monster:
                matching_properties = matching_properties + 1
                Monster_Display.append(Sub4.get())
            
            if matching_properties == 2:
                Suitable_Monsters2.append(Monster_Display)
            if matching_properties == 3:
                Suitable_Monsters3.append(Monster_Display)
            if matching_properties == 4:
                Suitable_Monsters4.append(Monster_Display)

    Suitable_Monsters = Suitable_Monsters4 + Suitable_Monsters3 + Suitable_Monsters2
    print(Suitable_Monsters)

    # tempList = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]
    # tempList.sort(key=lambda e: e[1], reverse=True)

    listBox.delete(*listBox.get_children())
    for i in Suitable_Monsters:
        listBox.insert("", "end", values=i)



def open_add_build():
    row_counter = 0

    #Create a Button to Open the Toplevel Window
    top= Toplevel(ws)
    top.title("Add Monster")

    Monster_name = StringVar()
    Monster_name.set(elements[0])

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
    *elements,
    command=display_selected
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
    *types,
    command=display_selected
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
        
        Monster_Info[Monster_name.get()] = Current_Monster

        f = open("MonstersDB.json", "w")
        json.dump(Monster_Info, f, indent = 6)
        f.close()

        top.destroy()

    save = Button(top, text = "save", command = lambda: save_monster(Monster_name, Element, Type, artifact_properties)).grid(row = row_counter)

    top.mainloop()

def open_check_build():
    row_counter = 0

    Selected_Monster = listBox.item(listBox.focus())['values'][0]

    #Create a Button to Open the Toplevel Window
    top = Toplevel(ws)
    top.title("Check Build")


    Label(top, text= Selected_Monster).grid(row = row_counter, column = 0)
   
    row_counter = row_counter + 1

    cols = ('Monster', 'Sub1', 'Sub2', 'Sub3', 'Sub4', 'Efficiency')
    Current_Artifact_List = ttk.Treeview(top, columns=cols, show='headings')

    for col in cols:
        Current_Artifact_List.heading(col, text=col)    
    Current_Artifact_List.grid(row=row_counter, column=0, columnspan=10)
    
    top.mainloop()


Button(ws, text="Show Monsters", width=15, command=show).grid(row=4, column=0)

# Label(ws, text= "Click the button to Open Popup Window", font= ('Helvetica 18')).place(relx=.5, rely=.5, anchor= CENTER)
Button(ws, text= "Add Build", background= "white", foreground= "blue", font= ('Helvetica 13 bold'), command= open_add_build).grid(row=4, column=1)
Button(ws, text= "Update Monster", background= "white", foreground= "blue", font= ('Helvetica 13 bold'), command= open_check_build).grid(row=4, column=2)
Button(ws, text="Close", width=15, command=exit).grid(row=4, column=3)

# infinite loop 
ws.mainloop()