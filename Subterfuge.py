# this program allows you to compute the result of potential battles in subterfuge

import tkinter as tk


mySubs = 0
enemySubs = 0
speed = 1

# specialists w/ combat phase
martyr      = 0
elder       = 0
assassin    = 0
saboteur    = 0
doubleAgent = 0
lietenant   = 0
general     = 0
warHero     = 0
king        = 0
infiltrator = 0

# movement specs
helmsman    = 0
smuggler    = 0
pirate      = 0
navigator   = 0
admiral     = 0
# lietenant   = 0
# general     = 0

# outpost specs
inspector   = 0
security    = 0
queen       = 0
princess    = 0
investigator= 0
tinkerer    = 0
minister    = 0
sentry      = 0
hypnotist   = 0
# king        = 0


# GUI START
window = tk.Tk()

label = tk.Label(window, text = "Subterfuge Battle Simulator")
label.pack()

# allied forces
x1 = 100

label = tk.Label(window, text = "Subs:")
label.pack()
label.place(x = x1, y = 50)

entrySubs = tk.Entry(window)
entrySubs.place(x = x1, y = 75)

label = tk.Label(window, text = "Specialists w/combat phase:")
label.place(x = x1, y = 100)

label = tk.Label(window, text = "Martyr")
label.place(x = x1, y = 125)

label = tk.Label(window, text = "Revered Elder")
label.place(x = x1, y = 175)

label = tk.Label(window, text = "Assassin")
label.place(x = x1, y = 225)

label = tk.Label(window, text = "Saboteur")
label.place(x = x1, y = 275)

label = tk.Label(window, text = "Double Agent")
label.place(x = x1, y = 325)

label = tk.Label(window, text = "Lietenant")
label.place(x = x1, y = 375)

label = tk.Label(window, text = "General")
label.place(x = x1, y = 425)

label = tk.Label(window, text = "War Hero")
label.place(x = x1, y = 475)

label = tk.Label(window, text = "Infiltrator")
label.place(x = x1, y = 525)

label = tk.Label(window, text = "King")
label.place(x = x1, y = 575)   

# outpost specs
x2 = 350
label = tk.Label(window, text = "Outpost specs:")
label.place(x = x2, y = 100)

label = tk.Label(window, text = "Inspector")
label.place(x = x2, y = 125)

label = tk.Label(window, text = "Security Agent?")
label.place(x = x2, y = 175)

label = tk.Label(window, text = "Inspector")
label.place(x = x2, y = 225)


# enemy forces

label = tk.Label(window, text = "Enemy Subs:")
label.pack()
label.place(x = 550, y = 50)

entryEnemySubs = tk.Entry(window)
entryEnemySubs.place(x = 550, y = 75)

def getTextFunc(var, entryVar):
    if entryVar.get() == "":
        var = 0
    else:
        var = entryVar.get()

def calculateButtonFunc():
    getTextFunc(mySubs, entrySubs)
    getTextFunc(enemySubs, entryEnemySubs)

calculateButton = tk.Button(window, text = "Calculate", command = calculateButtonFunc)

window.mainloop()

# NOTE: if I make this section of code into functions, maybe I can call them within the GUI to simulate combat?
# COMBAT

# specialist phases
# Phase 1



# Phase 2


# Phase 3


# Phase 4


# Phase 5


# Phase 6



# Combat Phase (drillers, shields, etc)