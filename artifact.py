from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv

ws = Tk()
ws.title('Artifact Tool')
# ws.geometry('400x300')

def display_selected(choice):
    # choice = variable.get()
    print(choice)

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


flat_subproperties = []

for rows in subproperties:
    flat_subproperties = flat_subproperties + rows


# setting variable for Integers
artifact_type = StringVar()
artifact_type.set(elements[0])

# creating widget
elements_select = OptionMenu(
    ws,
    artifact_type,
    *all_types,
    command=display_selected
)

# positioning widget
Label(ws, text = "Element or Type:").grid(row = 0, column = 0)
elements_select.grid(row=0, column=1)


# setting variable for Integers
Sub1 = StringVar()
Sub1.set(elements[0])

# creating widget
elements_select = OptionMenu(
    ws,
    Sub1,
    *flat_subproperties,
    command=display_selected
)

# positioning widget
Label(ws, text = "Sub1").grid(row = 0, column = 2)
elements_select.grid(row=0, column=3)

# setting variable for Integers
Sub2 = StringVar()
Sub2.set(elements[0])

# creating widget
elements_select = OptionMenu(
    ws,
    Sub2,
    *flat_subproperties,
    command=display_selected
)

# positioning widget
Label(ws, text = "Sub2").grid(row = 0, column = 4)
elements_select.grid(row=0, column=5)



# setting variable for Integers
Sub3 = StringVar()
Sub3.set(elements[0])

# creating widget
elements_select = OptionMenu(
    ws,
    Sub3,
    *flat_subproperties,
    command=display_selected
)

# positioning widget
Label(ws, text = "Sub3").grid(row = 0, column = 6)
elements_select.grid(row=0, column=7)


# setting variable for Integers
Sub4 = StringVar()
Sub4.set(elements[0])

# creating widget
elements_select = OptionMenu(
    ws,
    Sub4,
    *flat_subproperties,
    command=display_selected
)

# positioning widget
Label(ws, text = "Sub4").grid(row = 0, column = 8)
elements_select.grid(row=0, column=9)




def show():

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

# label = Label(ws, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
cols = ('Monster', 'Sub1', 'Sub2', 'Sub3', 'Sub4')
listBox = ttk.Treeview(ws, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=10)

showScores = Button(ws, text="Show Monsters", width=15, command=show).grid(row=4, column=0)
closeButton = Button(ws, text="Close", width=15, command=exit).grid(row=4, column=1)


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
        data = []
        for i in artifact_properties:
            data.append(i.get())
        print(Monster_name.get())
        print(Element.get())
        print(Type.get())
        print(data)

        f = open("MonstersDB.csv", "a")
        f.write(Monster_name.get())
        f.write(",")
        f.write(Element.get())
        f.write(",")
        f.write(Type.get())
        for i in range(len(data)):
            if data[i] == 1:
                f.write(",")
                f.write(flat_subproperties[i])
        f.write("\n")
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

# Label(ws, text= "Click the button to Open Popup Window", font= ('Helvetica 18')).place(relx=.5, rely=.5, anchor= CENTER)
Button(ws, text= "Add Build", background= "white", foreground= "blue", font= ('Helvetica 13 bold'), command= open_add_build).grid(row=4, column=2)
Button(ws, text= "Check Build", background= "white", foreground= "blue", font= ('Helvetica 13 bold'), command= open_check_build).grid(row=4, column=3)

# infinite loop 
ws.mainloop()