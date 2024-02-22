inventory = ["pine cone"]
status_func = {"mentalhp":50, "sockhp":5, "shoehp":15, "sockson":True, "shoeson":True, "squirrelalive":True}
def print_hp ():
    print("Mental HP", status_func["mentalhp"],
      "\nSock HP", status_func["sockhp"],
      "\nShoe HP", status_func["shoehp"])
    return

""" 0 = yes, 1 = no
 path choices A or Z ."""
def inventory_update():
    print(inventory)
    return

def status_update():
    if status_func["sockson"]:
        socks_on = "Yes"
    else:
        socks_on = "No"
    if status_func ["shoeson"]:
        shoes_on = "Yes"
    else:
        shoes_on = "No"
    print("Are you wearing socks? ", socks_on)
    print("Are you wearing Shoes? ", shoes_on)
    return
# elif for not being able to take off your shoes/socks when they are already off
def socksoff():
    if status_func["sockhp"] >0:
        inventory.append("Socks")
        print("You shove the socks in your pocket.")
        status_func["sockson"] = False
    elif status_func["sockson"] == False and status_func["sockhp"] > 0:
        print("You feet are ruddy with mud. You aren't wearing your socks.")
    else:
        print("You socks are too holey to wear. No need to carry the dead weight anymore.")
    status_func["sockson"] = False
    return

def shoesoff():
    if status_func["shoehp"] >0:
        inventory.append("Shoes")
        print("You tie the laces together and hang them around your neck.")
        status_func["shoeson"] = False
    elif status_func["shoeson"] == False and status_func["shoehp"] >0:
        print("You've tied them tight. How can you forget that they're on?")
    else:
        print("They are too battered to go on. Time to say goodbye.")
        status_func["shoeson"] = False
        return

def shoeson():
    if status_func["shoeson"] == False and status_func["shoehp"] > 0:
        inventory.remove("Shoes")
        print("You tie the laces tight and are ready to trek on.")
        status_func["shoeson"] = True
    elif status_func["shoeson"] == True:
        print("What are you doing? They're already on your feet.")
    else:
        print("You don't have those anymore. What are you looking for?")

def sockson():
    if status_func["sockson"] == False and status_func["sockhp"] > 0:
        inventory.remove("Socks")
        print("They look a little worse for wear but they cover your feet.")
        status_func["sockson"] = True
    elif status_func["sockson"] == True:
        print("You're already wearing them, silly.")
    else:
        print("They disintegrated awhile ago. What are you searching for?")
#elif for if there is no input
# write same function for socks
def inputchecker(userinputvar):
    x = int(userinputvar)
    flag_var = False
    while flag_var == False:
        if x == 0 or x == 1:
            flag_var = True
            return x
            break
        elif x == 2:
            status_update()
            x = input("Have you made a choice yet? 0 for Yes, 1 for No.")
            x = int(x)
        elif x == 3:
            inventory_update()
            x = input("Have you made a choice yet? 0 for Yes, 1 for No.")
            x = int(x)
        else:
            x = input("Sorry, I couldn't hear you. Speak up.")
            x = int(x)
# write same functions for socks
def shoes_on_off(shoeq):
    z = int(shoeq)
    if shoeq == 0:
         shoeson()
    elif shoeq == 1:
        shoesoff()
    return

def socks_on_off(sockq):
    a = int(sockq)
    if sockq == 0:
        sockson()
    elif sockq == 1:
        socksoff()
    return

""" x = input("Do you want to wear your shoes? 0 for Yes, 1 for No.")
y = inputchecker(x)
shoes_on_off(y)

b = input("What about your socks? Do you want to wear them? 0 for Yes, 1 for No.")
c = inputchecker(b)
socks_on_off(c) """
