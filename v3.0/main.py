import tkinter as tk
from tkinter import messagebox

# Game varibles
clicks = 0
rebirth = 1
rebirthCost = 100

# Stats varibles
clicksSpend = 0
totalClicks = 0

# Skins varibles
marsRock = False
marsRockEquiped = False

moonRock = False
moonRockEquiped = False

# Upgrades varibles
upgradeOneBought = False
upgradeTwoBought = False
upgradeThreeBought = False
upgradeFourBought = False

# Game data varibles
save_file_name = "game_save.json"

def count():
    global rebirth, clicks, totalClicks

    clicks = clicks + (1 * rebirth)
    totalClicks = totalClicks + (1 * rebirth)
    counter.config(text=str(clicks))

def openUpgradeWindow():
    global upgradeThreeBought, upgradeFourBought, upgradeOneBought, upgradeTwoBought

    def buyFirstUpgrade():
        global rebirthCost, clicks, clicksSpend, upgradeOneBought

        if clicks >= 1000:
            clicks = clicks - 1000
            clicksSpend = clicksSpend + 1000
            rebirthCost = rebirthCost - 10

            upgradeOneBought = True
            upgradeWindow.destroy()
    def buySecondUpgrade():
        global clicks, clicksSpend, rebirth, upgradeTwoBought
        
        if clicks >= 1000000:
            clicks = clicks - 1000000
            clicksSpend = clicksSpend + 1000000
            rebirth = rebirth * 2

            upgradeTwoBought = True
            upgradeWindow.destroy()
    def buyThirdUpdate():
        global rebirthCost, clicks, clicksSpend, upgradeThreeBought

        if clicks >= 1000000:
            clicks = clicks - 1000000
            clicksSpend = clicksSpend + 1000000
            rebirthCost = rebirthCost - 100

            upgradeThreeBought = True
            upgradeWindow.destroy()

    upgradeWindow = tk.Tk()
    upgradeWindow.title('Upgrade - Page 1')
    upgradeWindow.geometry('200x100')
    upgradeWindow.resizable(0,0)

    def goToPage2():
        messagebox.showinfo('Info', 'Next page is not detected')

    # Upgrade 1
    tk.Label(upgradeWindow, text='Rebirth cost - 10').grid(column=0, row=0)
    if upgradeOneBought == False:
        tk.Button(upgradeWindow, text='Buy 1000', bg='green', command=buyFirstUpgrade).grid(column=1, row=0)
    elif upgradeOneBought == True:
         tk.Button(upgradeWindow, text='Puashed', bg='red').grid(column=1, row=0)

    # Upgrade 2
    tk.Label(upgradeWindow, text='2x my rebirth').grid(column=0, row=1)
    if upgradeTwoBought == False:
        tk.Button(upgradeWindow, text='Buy 1000000', bg='green', command=buySecondUpgrade).grid(column=1, row=1)
    elif upgradeTwoBought == True:
        tk.Button(upgradeWindow, text='Puashed', bg='red').grid(column=1, row=1)

    # Update 3
    tk.Label(upgradeWindow, text='Rebirth cost - 100').grid(column=0, row=2)
    if upgradeThreeBought == False:
        tk.Button(upgradeWindow, text='Buy 1000000', bg='green',command=buyThirdUpdate).grid(column=1, row=2)
    elif upgradeThreeBought == True:
        tk.Button(upgradeWindow, text='Puashed', bg='red').grid(column=1, row=2)

    # Next page menubar
    upgradeMenubar = tk.Menu(upgradeWindow)
    upgradeMenubar.add_cascade(label='Next page', command=goToPage2)

    upgradeWindow.config(menu=upgradeMenubar)
    upgradeWindow.mainloop()

def openRebirthWindow():
    global rebirth

    # Buy rebirth functions
    def buyRebirth1():
        global clicks
        global rebirth
        global rebirthCost
        global clicksSpend

        if rebirthCost <= clicks:
            rebirth = rebirth + 1
            clicks = 0
            clicksSpend = clicksSpend + rebirthCost
            rebirthCost = (rebirthCost * 2)

            rebirthWindow.destroy()
    def buyRebirth10():
        global clicks
        global rebirthCost
        global rebirth
        global clicksSpend

        if (rebirthCost * 10) <= clicks:
            rebirth = rebirth + 10
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 10)
            rebirthCost = rebirthCost * 10

            rebirthWindow.destroy()
    def buyRebirth100():
        global clicks
        global rebirthCost
        global rebirth
        global clicksSpend

        if (rebirthCost * 100) <= clicks:
            rebirth = rebirth + 100
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 100)
            rebirthCost = rebirthCost * 100

            rebirthWindow.destroy()
    def buyRebirth1000():
        global clicks
        global rebirthCost
        global rebirth
        global clicksSpend

        if (rebirthCost * 1000) <= clicks:
            rebirth = rebirth + 1000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 1000)
            rebirthCost = rebirthCost * 1000

            rebirthWindow.destroy()
    def buyRebirth10000():
        global clicks
        global rebirthCost
        global rebirth
        global rock
        global clicksSpend

        if (rebirthCost * 10000) <= clicks:
            rebirth = rebirth + 10000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 10000)
            rebirthCost = rebirthCost * 10000

            rebirthWindow.destroy()
    def buyRebirth100000():
        global clicks
        global rebirthCost
        global rebirth
        global rock
        global clicksSpend

        if (rebirthCost * 100000) <= clicks:
            rebirth = rebirth + 100000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 100000)
            rebirthCost = rebirthCost * 100000

            rebirthWindow.destroy()
    def buyRebirth1000000():
        global clicks
        global rebirthCost
        global rebirth
        global rock
        global clicksSpend

        if (rebirthCost * 1000000) <= clicks:
            rebirth = rebirth + 1000000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 1000000)
            rebirthCost = rebirthCost * 1000000

            rebirthWindow.destroy()
    def buyRebirth10000000():
        global clicks
        global rebirthCost
        global rebirth
        global rock
        global clicksSpend

        if (rebirthCost * 10000000) <= clicks:
            rebirth = rebirth + 10000000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 10000000)
            rebirthCost = rebirthCost * 10000000

            rebirthWindow.destroy()
    def buyRebirth100000000():
        global clicks
        global rebirthCost
        global rebirth
        global rock
        global clicksSpend

        if (rebirthCost * 100000000) <= clicks:
            rebirth = rebirth + 100000000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 100000000)
            rebirthCost = rebirthCost * 100000000

            rebirthWindow.destroy()
    def buyRebirth1000000000():
        global clicks
        global rebirthCost
        global rebirth
        global rock
        global clicksSpend

        if (rebirthCost * 1000000000) <= clicks:
            rebirth = rebirth + 1000000000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 1000000000)
            rebirthCost = rebirthCost * 1000000000

            rebirthWindow.destroy()

    rebirthWindow = tk.Tk()
    rebirthWindow.title('Rebirth - Page 1')
    rebirthWindow.geometry('300x300')
    rebirthWindow.resizable(0,0)

    # 1 rebirth
    tk.Label(rebirthWindow, text='1 Rebirth: '+ str(rebirthCost), font=('Arial', 10)).grid(column=0, row=1)
    tk.Button(rebirthWindow, text='Rebirth', bg='green', command=buyRebirth1).grid(column=1, row=1)

    # 10 Rebirth
    tk.Label(rebirthWindow, text='10 Rebirth: '+ str(rebirthCost * 10), font=('Arial', 10)).grid(column=0, row=2)
    tk.Button(rebirthWindow, text='Rebirth', bg='green', command=buyRebirth10).grid(column=1, row=2)

    # 100 Rebirth
    tk.Label(rebirthWindow, text='100 Rebirth: '+ str(rebirthCost * 100), font=('Arial', 10)).grid(column=0, row=3)
    tk.Button(rebirthWindow, text='Rebirth', bg='green', command=buyRebirth100).grid(column=1, row=3)

    # 1000 Rebirth
    tk.Label(rebirthWindow, text='1K Rebirth: '+ str(rebirthCost * 1000), font=('Arial', 10)).grid(column=0, row=4)
    tk.Button(rebirthWindow, text='Rebirth', bg='green', command=buyRebirth1000).grid(column=1, row=4)

    # 10000 Rebirth
    tk.Label(rebirthWindow, text='10K Rebirth: '+ str(rebirthCost * 10_000), font=('Arial', 10)).grid(column=0, row=5)
    tk.Button(rebirthWindow, text='Rebirth', bg='green', command=buyRebirth10000).grid(column=1, row=5)

    # 100000 Rebirth
    tk.Label(rebirthWindow, text='100K Rebirth: '+ str(rebirthCost * 100_000), font=('Arial', 10)).grid(column=0, row=6)
    tk.Button(rebirthWindow, text='Rebirth', bg='green', command=buyRebirth100000).grid(column=1, row=6)

    # 1000000 Rebirth
    tk.Label(rebirthWindow, text='1M Rebirth: '+ str(rebirthCost * 1_000_000), font=('Arial', 10)).grid(column=0, row=7)
    tk.Button(rebirthWindow, text='Rebirth', bg='green', command=buyRebirth1000000).grid(column=1, row=7)

    # 10000000 Rebirth
    tk.Label(rebirthWindow, text='10M Rebirth: '+ str(rebirthCost * 10_000_000), font=('Arial', 10)).grid(column=0, row=8)
    tk.Button(rebirthWindow, text='Rebirth', bg='green', command=buyRebirth10000000).grid(column=1, row=8)

    # 100000000 Rebirth
    tk.Label(rebirthWindow, text='100M Rebirth: '+ str(rebirthCost * 100_000_000), font=('Arial', 10)).grid(column=0, row=9)
    tk.Button(rebirthWindow, text='Rebirth', bg='green', command=buyRebirth100000000).grid(column=1, row=9)

    # 1000000000 Rebirth
    tk.Label(rebirthWindow, text='1B Rebirth: '+ str(rebirthCost * 1_000_000_000), font=('Arial', 10)).grid(column=0, row=10)
    tk.Button(rebirthWindow, text='Rebirth', bg='green', command=buyRebirth1000000000).grid(column=1, row=10)



    rebirthWindow.mainloop()

# Save, clear and load data
def save_game():
    global rebirth, clicks, rebirthCost, totalClicks, clicksSpend, marsRock, marsRockEquiped, upgradeOneBought, upgradeTwoBought, upgradeThreeBought, upgradeFourBought, moonRock, moonRockEquiped

    game_state = {
        "clicks": clicks,
        "rebirth": rebirth,
        "rebirthCost": rebirthCost, 
        "clicksSpend": clicksSpend,
        "totalClicks": totalClicks,
        "marsRock": marsRock,
        "marsRockEquiped": marsRockEquiped,
        "upgrade1": upgradeOneBought,
        "upgrade2": upgradeTwoBought,
        "upgrade3": upgradeThreeBought,
        "upgrade4": upgradeFourBought,
        "moonRock": moonRock,
        "moonRockEquiped": moonRockEquiped
    }

    with open(save_file_name, "w") as save_file:
        save_file.write(str(game_state))
        messagebox.showinfo('Game Data ', "Game saved")
def load_game():
    global rebirth, clicks, rebirthCost, totalClicks, clicksSpend, marsRock, marsRockEquiped, upgradeOneBought, upgradeTwoBought, upgradeThreeBought, upgradeFourBought, moonRock, moonRockEquiped
    try:
        with open(save_file_name, "r") as save_file:
            game_state = eval(save_file.read())
            clicks = game_state["clicks"]
            rebirth = game_state["rebirth"]
            rebirthCost = game_state["rebirthCost"]
            totalClicks = game_state["totalClicks"]
            clicksSpend = game_state["clicksSpend"]
            marsRock = game_state["marsRock"]
            marsRockEquiped = game_state["marsRockEquiped"]
            upgradeOneBought = game_state["upgrade1"]
            upgradeTwoBought = game_state["upgrade2"]
            upgradeThreeBought = game_state["upgrade3"]
            upgradeFourBought = game_state["upgrade4"]
            moonRockEquiped = game_state["moonRockEquiped"]
            moonRock = game_state["moonRock"]

    except FileNotFoundError:
        messagebox.showinfo('Game Data', "No file found")
def clearGameData():
    global rebirth, clicks, rebirthCost, totalClicks, clicksSpend, marsRock, marsRockEquiped, upgradeOneBought, upgradeTwoBought, upgradeThreeBought, upgradeFourBought, moonRock, moonRockEquiped

    game_state = {
        "clicks": 0,
        "rebirth": 1,
        "rebirthCost": 100,
        "clicksSpend": 0,
        "totalClicks": 0,
        "marsRock": False,
        "marsRockEquiped": False,
        "upgrade1": False,
        "upgrade2": False,
        "upgrade3": False,
        "upgrade4": False,
        "moonRock": False,
        "moonRockEquiped": False
    }

    with open(save_file_name, "w") as save_file:
        save_file.write(str(game_state))
        messagebox.showinfo('Game Data', "Game data cleared")
        root.destroy()
def openInfoWindow():
    infoWindow = tk.Tk()
    infoWindow.title('Info')
    infoWindow.geometry("400x400")
    infoWindow.resizable(0,0)

    tk.Label(infoWindow, text='Authors', font=('Arial', 40)).pack()
    tk.Label(infoWindow, text='Fefek', font=('Arial', 25)).pack()
    tk.Label(infoWindow, text='Version', font=('Arial', 40)).pack()
    tk.Label(infoWindow, text='3.0', font=('Arial', 25)).pack()
    tk.Label(infoWindow, text='Beta testers', font=('Arial', 40)).pack()
    tk.Label(infoWindow, text='Figamaster', font=('Arial', 25)).pack()
    tk.Label(infoWindow, text='W1KT04_', font=('Arial', 25)).pack()

    infoWindow.mainloop()

def openStatsWindow():
    statsWindow = tk.Tk()
    statsWindow.title('Stats')
    statsWindow.geometry('200x80')
    statsWindow.resizable(0,0)

    tk.Label(statsWindow, text=('Total Clicks: ' + str(totalClicks))).grid(column=0, row=0)
    tk.Label(statsWindow, text=('Rebirths: ' + str(rebirth))).grid(column=0, row=1)
    tk.Label(statsWindow, text=('Clicks Spend: ' + str(clicksSpend))).grid(column=0, row=2)

    statsWindow.mainloop()

def openSkinsMenu():
    def marsRockBought():
        global clicks, clicksSpend, marsRock
        
        if clicks >= 10000:
            clicks = clicks - 10000
            clicksSpend = clicksSpend + 10000
            marsRock = True
            skinsPage1.destroy()
    def marsRockEquip():
        global marsRockEquiped
        marsRockEquiped = True
        messagebox.showinfo('Info', 'Save game and exit to show changes')
        skinsPage1.destroy()
    def marsRockUnequip():
        global marsRockEquiped, root
        marsRockEquiped = False
        messagebox.showinfo('Info', 'Save game and exit to show changes')
        skinsPage1.destroy()

    def goToMoonRock():
        global moonRock, moonRockEquiped

        skinsPage1.destroy() # <-- is's killing window with mars rock

        def moonRockBought():
            global clicks, clicksSpend, moonRock
        
            if clicks >= 10000:
                clicks = clicks - 10000
                clicksSpend = clicksSpend + 10000
                moonRock = True
                skinsPage2.destroy()
        def moonRockEquip():
            global moonRockEquiped
            moonRockEquiped = True
            messagebox.showinfo('Info', 'Save game and exit to show changes')
            skinsPage2.destroy()
        def moonRockUnequip():
            global marsRockEquiped, root
            marsRockEquiped = False
            messagebox.showinfo('Info', 'Save game and exit to show changes')
            skinsPage1.destroy()

        def backToMarsRock():
            skinsPage2.destroy()
            openSkinsMenu()

        skinsPage2 = tk.Tk()
        skinsPage2.geometry('350x200')
        skinsPage2.title('Rock skins - Moon Rock')
        skinsPage2.resizable(0,0)

        tk.Label(skinsPage2, text='Moon Rock', fg="black", pady="40", font=('Arial', 25)).pack()
        tk.Button(skinsPage2, text="I'm a rock", fg='yellow', bg='lightgrey').pack()
        tk.Label(skinsPage2, text='Preview', font=('Arial', 5), pady=5).pack()
        if moonRock == True and moonRockEquiped == False:
            tk.Button(skinsPage2, text='Equip', bg='green', command=moonRockEquip).pack()
        elif moonRock == False:
            tk.Button(skinsPage2, text='Buy 10000 clicks', bg='green', command=moonRockBought).pack()
        elif moonRockEquiped == True:
            tk.Button(skinsPage2, text='Unequip', bg='red', command=moonRockUnequip).pack()

        skinsMenubar2 = tk.Menu(skinsPage2)
        skinsMenubar2.add_cascade(label='Back', command=backToMarsRock)

        skinsPage2.config(menu=skinsMenubar2)
        skinsPage2.mainloop()

    skinsPage1 = tk.Tk()
    skinsPage1.geometry('350x200')
    skinsPage1.title('Rock skins - Mars Rock')
    skinsPage1.resizable(0,0)

    tk.Label(skinsPage1, text='Mars Rock', fg="black", pady="40", font=('Arial', 25)).pack()
    tk.Button(skinsPage1, text="I'm a rock", fg='brown', bg='orange').pack()
    tk.Label(skinsPage1, text='Preview', font=('Arial', 5), pady=5).pack()
    if marsRock == True and marsRockEquiped == False:
        tk.Button(skinsPage1, text='Equip', bg='green', command=marsRockEquip).pack()
    elif marsRock == False:
        tk.Button(skinsPage1, text='Buy 10000 clicks', bg='green', command=marsRockBought).pack()
    elif marsRockEquiped == True:
        tk.Button(skinsPage1, text='Unequip', bg='red', command=marsRockUnequip).pack()

    skinsMenubar = tk.Menu(skinsPage1)
    skinsMenubar.add_cascade(label='Next page', command=goToMoonRock)

    skinsPage1.config(menu=skinsMenubar)
    skinsPage1.mainloop()

# Root window
load_game() # <-- Auto load

root = tk.Tk()
root.title("The Rock Corporation 3")
root.geometry("350x200")
root.resizable(0,0)

# Settings menubar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Info", command=openInfoWindow)
filemenu.add_command(label="Save", command=save_game)
filemenu.add_command(label="Clear Data", command=clearGameData)
menubar.add_cascade(label="Settings", menu=filemenu)

# Action menubar
filemenu2 = tk.Menu(menubar, tearoff=0)
filemenu2.add_command(label="Rebirths Window", command=openRebirthWindow)
filemenu2.add_command(label='Upgrades Window', command=openUpgradeWindow)
filemenu2.add_command(label='Stats Window', command=openStatsWindow)
filemenu2.add_command(label='Skins Catalog', command=openSkinsMenu)
menubar.add_cascade(label="Open", menu=filemenu2)

# Counter config
counter = tk.Label(root,fg="black", pady="40", font=('Arial', 25))
counter.config(text=str(clicks))
counter.pack()

# Clicker Button
if marsRockEquiped == False and moonRockEquiped == False:
    rock = tk.Button(root, text="I'm a rock", fg='lightgrey', bg='grey', command=count)
    rock.pack()
elif marsRockEquiped == True and moonRockEquiped == False:
    rock = tk.Button(root, text="I'm a rock", fg='brown', bg='orange', command=count)
    rock.pack()
elif moonRockEquiped == True and marsRockEquiped == False:
    rock = tk.Button(root, text="I'm a rock", fg='yellow', bg='lightgrey', command=count)
    rock.pack()

tk.Label(root, text='(Just click it)', font=('Arial', 5)).pack() # <-- this funny 'click it' caption hehe

root.config(menu=menubar)
root.mainloop()