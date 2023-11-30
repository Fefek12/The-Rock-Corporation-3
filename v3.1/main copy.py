import tkinter as tk
from tkinter import messagebox

# Game varibles
clicks = 0
rebirth = 1
rebirthCost = 100
skinsCost = 10000

# Stats varibles
clicksSpend = 0
totalClicks = 0

# Skins varibles
marsRock = False
marsRockEquiped = False

moonRock = False
moonRockEquiped = False

amethystRock = False
amethystRockEquiped = False

bread = False
breadEquiped = False

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
    global upgradeThreeBought, upgradeFourBought, upgradeOneBought, upgradeTwoBought, clicksshort

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
        global clicks, rebirth, rebirthCost, clicksSpend

        if rebirthCost <= clicks:
            rebirth = rebirth + 1
            clicks = 0
            clicksSpend = clicksSpend + rebirthCost
            rebirthCost = (rebirthCost * 2)

            rebirthWindow.destroy()
    def buyRebirth10():
        global clicks, rebirth, rebirthCost, clicksSpend

        if (rebirthCost * 10) <= clicks:
            rebirth = rebirth + 10
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 10)
            rebirthCost = rebirthCost * 10

            rebirthWindow.destroy()
    def buyRebirth100():
        global clicks, rebirth, rebirthCost, clicksSpend

        if (rebirthCost * 100) <= clicks:
            rebirth = rebirth + 100
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 100)
            rebirthCost = rebirthCost * 100

            rebirthWindow.destroy()
    def buyRebirth1000():
        global clicks, rebirth, rebirthCost, clicksSpend

        if (rebirthCost * 1000) <= clicks:
            rebirth = rebirth + 1000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 1000)
            rebirthCost = rebirthCost * 1000

            rebirthWindow.destroy()
    def buyRebirth10000():
        global clicks, rebirth, rebirthCost, clicksSpend

        if (rebirthCost * 10000) <= clicks:
            rebirth = rebirth + 10000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 10000)
            rebirthCost = rebirthCost * 10000

            rebirthWindow.destroy()
    def buyRebirth100000():
        global clicks, rebirth, rebirthCost, clicksSpend

        if (rebirthCost * 100000) <= clicks:
            rebirth = rebirth + 100000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 100000)
            rebirthCost = rebirthCost * 100000

            rebirthWindow.destroy()
    def buyRebirth1000000():
        global clicks, rebirth, rebirthCost, clicksSpend

        if (rebirthCost * 1000000) <= clicks:
            rebirth = rebirth + 1000000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 1000000)
            rebirthCost = rebirthCost * 1000000

            rebirthWindow.destroy()
    def buyRebirth10000000():
        global clicks, rebirth, rebirthCost, clicksSpend

        if (rebirthCost * 10000000) <= clicks:
            rebirth = rebirth + 10000000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 10000000)
            rebirthCost = rebirthCost * 10000000

            rebirthWindow.destroy()
    def buyRebirth100000000():
        global clicks, rebirth, rebirthCost, clicksSpend

        if (rebirthCost * 100000000) <= clicks:
            rebirth = rebirth + 100000000
            clicks = 0
            clicksSpend = clicksSpend + (rebirthCost * 100000000)
            rebirthCost = rebirthCost * 100000000

            rebirthWindow.destroy()
    def buyRebirth1000000000():
        global clicks, rebirth, rebirthCost, clicksSpend

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
    global rebirth, clicks, rebirthCost, totalClicks, clicksSpend, marsRock, marsRockEquiped, upgradeOneBought, upgradeTwoBought, upgradeThreeBought, upgradeFourBought, moonRock, moonRockEquiped, amethystRockEquiped, amethystRock, skinsCost, bread, breadEquiped

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
        "moonRockEquiped": moonRockEquiped,
        "amethystRock": amethystRock,
        "amethystRockEquiped": amethystRockEquiped,
        "skinsCost": skinsCost,
        "bread": bread,
        "breadEquiped": breadEquiped,
    }

    with open(save_file_name, "w") as save_file:
        save_file.write(str(game_state))
        messagebox.showinfo('Game Data ', "Game saved")
def load_game():
    global rebirth, clicks, rebirthCost, totalClicks, clicksSpend, marsRock, marsRockEquiped, upgradeOneBought, upgradeTwoBought, upgradeThreeBought, upgradeFourBought, moonRock, moonRockEquiped, amethystRock, amethystRockEquiped, skinsCost, bread, breadEquiped
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
            amethystRockEquiped = game_state["amethystRockEquiped"]
            amethystRock = game_state["amethystRock"]
            skinsCost = game_state["skinsCost"]
            bread = game_state["bread"]
            breadEquiped = game_state["breadEquiped"]

    except FileNotFoundError:
        messagebox.showinfo('Game Data', "No file found")
def clearGameData():
    global rebirth, clicks, rebirthCost, totalClicks, clicksSpend, marsRock, marsRockEquiped, upgradeOneBought, upgradeTwoBought, upgradeThreeBought, upgradeFourBought, moonRock, moonRockEquiped, amethystRockEquiped, amethystRock, skinsCost, bread, breadEquiped

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
        "moonRockEquiped": False,
        "amethystRock": False,
        "amethystRockEquiped": False,
        "skinsCost": 10000,
        "bread": False,
        "breadEquiped": False
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
    tk.Label(infoWindow, text='3.1', font=('Arial', 25)).pack()
    tk.Label(infoWindow, text='Beta testers', font=('Arial', 40)).pack()
    tk.Label(infoWindow, text='Ave_Filip12', font=('Arial', 25)).pack()

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

def marsRockPage():
    def marsRockBuy():
        global clicks, clicksSpend, marsRock, skinsCost
        
        if clicks >= skinsCost:
            clicks = clicks - skinsCost
            clicksSpend = clicksSpend + skinsCost
            marsRock = True
            skinsPage1.destroy()
    def marsRockEquip():
        global marsRockEquiped
        if moonRockEquiped or amethystRockEquiped or bread == True:
            messagebox.showinfo('Info', 'You have to unequip other skin!')
        elif moonRockEquiped == False:
            marsRockEquiped = True
            messagebox.showinfo('Info', 'Save game and exit to show changes')
            skinsPage1.destroy()
    def marsRockUnequip():
        global marsRockEquiped, root
        marsRockEquiped = False
        messagebox.showinfo('Info', 'Save game and exit to show changes')
        skinsPage1.destroy()
    
    def goToMoonNext():  # <-- is's killing window with mars rock
        skinsPage1.destroy()
        moonRockPage()

    # Moon Rock
    def moonRockPage():
        global moonRock, moonRockEquiped
        def moonRockBuy():
            global clicks, clicksSpend, moonRock, skinsCost
        
            if clicks >= skinsCost:
                clicks = clicks - skinsCost
                clicksSpend = clicksSpend + skinsCost
                moonRock = True
                skinsPage2.destroy()
        def moonRockEquip():
            global moonRockEquiped, marsRockEquiped
            if marsRockEquiped or amethystRockEquiped or bread == True:
                messagebox.showinfo('Info', 'You have to unequip other skin!')
            elif marsRockEquiped == False:
                moonRockEquiped = True
                messagebox.showinfo('Info', 'Save game and exit to show changes')
                skinsPage2.destroy()
        def moonRockUnequip():
            global moonRockEquiped, root
            moonRockEquiped = False
            messagebox.showinfo('Info', 'Save game and exit to show changes')
            skinsPage2.destroy()

        def backToMarsRock():
            skinsPage2.destroy()
            marsRockPage()
        def gotoAmethystRock():   # <-- is's killing window with moon rock
            skinsPage2.destroy()
            amethysRockPage()

        # Amethyst Rock
        def amethysRockPage():
            def backToMoonRock():
                skinsPage3.destroy()
                moonRockPage()
            def goToBreadPage():
                skinsPage3.destroy()
                breadPage()
            
            def amethystRockBuy():
                global clicks, clicksSpend, amethystRock, skinsCost
            
                if clicks >= skinsCost:
                    clicks = clicks - skinsCost
                    clicksSpend = clicksSpend + skinsCost
                    amethystRock = True
                    skinsPage3.destroy()
            def amethystRockEquip():
                global amethystRockEquiped
                if moonRockEquiped or marsRockEquiped or bread == True:
                    messagebox.showinfo('Info', 'You have to unequip other skin')
                elif amethystRockEquiped == False:
                    amethystRockEquiped = True
                    messagebox.showinfo('Info', 'Save game and exit to show changes')
                    skinsPage3.destroy()
            def amethystRockUnequip():
                global amethystRockEquiped, root
                amethystRockEquiped = False
                messagebox.showinfo('Info', 'Save game and exit to show changes')
                skinsPage1.destroy()

            # Bread
            def breadPage():
                def backToAmethystRock():
                    skinsPage4.destroy()
                    amethysRockPage()
                
                def breadBuy():
                    global clicks, clicksSpend, bread, skinsCost
                
                    if clicks >= (skinsCost + 90000):
                        clicks = clicks - (skinsCost + 90000)
                        clicksSpend = clicksSpend + (skinsCost + 90000)
                        bread = True
                        skinsPage4.destroy()
                def breadEquip():
                    global breadEquiped
                    if moonRockEquiped or marsRockEquiped or amethystRockEquiped == True:
                        messagebox.showinfo('Info', 'You have to unequip other skin')
                    elif breadEquiped == False:
                        breadEquiped = True
                        messagebox.showinfo('Info', 'Save game and exit to show changes')
                        skinsPage4.destroy()
                def breadUnequip():
                    global breadEquiped, root
                    breadEquiped = False
                    messagebox.showinfo('Info', 'Save game and exit to show changes')
                    skinsPage4.destroy()
            
                skinsPage4 = tk.Tk()
                skinsPage4.geometry('350x200')
                skinsPage4.title('Rock skins - Bread')
                skinsPage4.resizable(0,0)

                tk.Label(skinsPage4, text='[E] Bread', fg="purple", pady="40", font=('Arial', 25)).pack()
                tk.Button(skinsPage4, text="I'm a bread", fg='darkorange3', bg='darkorange4').pack()
                tk.Label(skinsPage4, text='Preview', font=('Arial', 5), pady=5).pack()
                if bread == True and breadEquiped == False:
                    tk.Button(skinsPage4, text='Equip', bg='green', command=breadEquip).pack()
                elif bread == False:
                    tk.Button(skinsPage4, text='Buy 100000 clicks', bg='green', command=breadBuy).pack()
                elif breadEquiped == True:
                    tk.Button(skinsPage4, text='Unequip', bg='red', command=breadUnequip).pack()

                skinsMenubar4 = tk.Menu(skinsPage4)
                skinsMenubar4.add_cascade(label='Back', command=backToAmethystRock)

                skinsPage4.config(menu=skinsMenubar4)
                skinsPage4.mainloop()

            skinsPage3 = tk.Tk()
            skinsPage3.geometry('350x200')
            skinsPage3.title('Rock skins - Amethyst Rock')
            skinsPage3.resizable(0,0)

            tk.Label(skinsPage3, text='[C] Amethyst Rock', fg="black", pady="40", font=('Arial', 25)).pack()
            tk.Button(skinsPage3, text="I'm a rock", fg='magenta', bg='pink').pack()
            tk.Label(skinsPage3, text='Preview', font=('Arial', 5), pady=5).pack()
            if amethystRock == True and amethystRockEquiped == False:
                tk.Button(skinsPage3, text='Equip', bg='green', command=amethystRockEquip).pack()
            elif amethystRock == False:
                tk.Button(skinsPage3, text='Buy 10000 clicks', bg='green', command=amethystRockBuy).pack()
            elif amethystRockEquiped == True:
                tk.Button(skinsPage3, text='Unequip', bg='red', command=amethystRockUnequip).pack()

            skinsMenubar3 = tk.Menu(skinsPage3)
            skinsMenubar3.add_cascade(label='Back', command=backToMoonRock)
            skinsMenubar3.add_cascade(label='Next', command=goToBreadPage)

            skinsPage3.config(menu=skinsMenubar3)
            skinsPage3.mainloop()


        skinsPage2 = tk.Tk()
        skinsPage2.geometry('350x200')
        skinsPage2.title('Rock skins - Moon Rock')
        skinsPage2.resizable(0,0)

        tk.Label(skinsPage2, text='[C] Moon Rock', fg="black", pady="40", font=('Arial', 25)).pack()
        tk.Button(skinsPage2, text="I'm a rock", fg='yellow', bg='lightgrey').pack()
        tk.Label(skinsPage2, text='Preview', font=('Arial', 5), pady=5).pack()
        if moonRock == True and moonRockEquiped == False:
            tk.Button(skinsPage2, text='Equip', bg='green', command=moonRockEquip).pack()
        elif moonRock == False:
            tk.Button(skinsPage2, text='Buy 10000 clicks', bg='green', command=moonRockBuy).pack()
        elif moonRockEquiped == True:
            tk.Button(skinsPage2, text='Unequip', bg='red', command=moonRockUnequip).pack()

        skinsMenubar2 = tk.Menu(skinsPage2)
        skinsMenubar2.add_cascade(label='Back', command=backToMarsRock)
        skinsMenubar2.add_cascade(label='Next', command=gotoAmethystRock)

        skinsPage2.config(menu=skinsMenubar2)
        skinsPage2.mainloop()

    skinsPage1 = tk.Tk()
    skinsPage1.geometry('350x200')
    skinsPage1.title('Rock skins - Mars Rock')
    skinsPage1.resizable(0,0)

    tk.Label(skinsPage1, text='[C] Mars Rock', fg="black", pady="40", font=('Arial', 25)).pack()
    tk.Button(skinsPage1, text="I'm a rock", fg='brown', bg='orange').pack()
    tk.Label(skinsPage1, text='Preview', font=('Arial', 5), pady=5).pack()
    if marsRock == True and marsRockEquiped == False:
        tk.Button(skinsPage1, text='Equip', bg='green', command=marsRockEquip).pack()
    elif marsRock == False:
        tk.Button(skinsPage1, text='Buy 10000 clicks', bg='green', command=marsRockBuy).pack()
    elif marsRockEquiped == True:
        tk.Button(skinsPage1, text='Unequip', bg='red', command=marsRockUnequip).pack()

    skinsMenubar = tk.Menu(skinsPage1)
    skinsMenubar.add_cascade(label='Next', command=goToMoonNext)

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
filemenu2.add_command(label='Skins Catalog', command=marsRockPage)
menubar.add_cascade(label="Open", menu=filemenu2)

# Counter config
counter = tk.Label(root,fg="black", pady="40", font=('Arial', 25))
counter.config(text=str(clicks))
counter.pack()

# Clicker Button
if marsRockEquiped == False and moonRockEquiped == False and amethystRockEquiped == False and breadEquiped == False:
    rock = tk.Button(root, text="I'm a rock", fg='lightgrey', bg='grey', command=count)
    rock.pack()
elif marsRockEquiped == True and moonRockEquiped == False and amethystRockEquiped == False and breadEquiped == False:
    rock = tk.Button(root, text="I'm a rock", fg='brown', bg='orange', command=count)
    rock.pack()
elif moonRockEquiped == True and marsRockEquiped == False and amethystRockEquiped == False and breadEquiped == False:
    rock = tk.Button(root, text="I'm a rock", fg='yellow', bg='lightgrey', command=count)
    rock.pack()
elif amethystRockEquiped == True and marsRockEquiped == False and moonRockEquiped == False and breadEquiped == False:
    rock = tk.Button(root, text="I'm a rock", fg='magenta', bg='pink', command=count)
    rock.pack()
elif amethystRockEquiped == False and marsRockEquiped == False and moonRockEquiped == False and breadEquiped == True:
    rock = tk.Button(root, text="I'm a bread", fg='darkorange3', bg='darkorange4', command=count)
    rock.pack()
tk.Label(root, text='(Just click it)', font=('Arial', 5)).pack() # <-- this funny 'click it' caption hehe

root.config(menu=menubar)
root.mainloop()