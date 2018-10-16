from easygui import *
import sys
while 1:
    msgbox("e-BazzaR")

    msg ="Choose Your Shopping Category"
    title = "Home"
    choices = ["Electronics", "Mobiles", "Clothings", "Cosmatics", "Furniture"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("Your choice: " + str(choice), "Choice Result")
    if choice=="Electronics" :
        msg ="Electronic Store"
        title = "E-BazzaR"
        choices = ["Accessories", "Keyboard", "Mouse", "PC", "Headphones"]
        choice1 = choicebox(msg, title, choices)
        if choice1=="Accessories":
           msg ="Accessories Store"
           title = "E-BazzaR"
           choices = ["Vendor1: 5 $", "Vendor2: 6 $", "Vendor3: 4 $"]
           choice = choicebox(msg, title, choices)
        elif choice1=="Keyboard":
           msg ="Keyboard Store"
           title = "E-BazzaR"
           choices = ["Vendor1: 12 $", "Vendor2: 16 $", "Vendor3: 14 $"]
           choice = choicebox(msg, title, choices) 
        elif choice1=="Mouse":
           msg ="Mouse Store"
           title = "E-BazzaR"
           choices = ["Vendor1: 10 $", "Vendor2: 6 $", "Vendor3: 9 $"]
           choice = choicebox(msg, title, choices)  
        elif choice1=="PC":
           msg ="PC Store"
           title = "E-BazzaR"
           choices = ["Vendor1: 300 $", "Vendor2: 260 $", "Vendor3: 440 $"]
           choice = choicebox(msg, title, choices) 
        elif choice1=="Headphones":
           msg ="Headphones Store"
           title = "E-BazzaR"
           choices = ["Vendor1: 12 $", "Vendor2: 16 $", "Vendor3: 14 $"]
           choice = choicebox(msg, title, choices)     
    
    
    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)
