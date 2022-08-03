# (5 points): As a developer, I want to make at least three commits with descriptive messages. 
# (5 points): As a developer, I want to store my destinations, restaurants, modes of transportation, and entertainments in their own separate Lists. 
# (5 points): As a developer, I want to store my final day trip selections in a Dictionary, with a unique key value pair for each piece of my day trip.
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
# (10 points): As a user, I want to display my completed trip in the console. 
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

# imports
import random

# lists 
destination_list = ["London", "Bora Bora", "Mars", "Santa's Workshop", "grandmas house", "Disneyland"]
restaurant_list = ["In n Out", "Olive Garden", "Chipotle", "Raised by Wolves", "Canlis", "Ipanema", "Cafe Boloud"]
transportation_list = ["rollerblade", "limosine", "private jet", "Greyhound bus", "hitchhiking", "donkey ride", "jet pack"]
entertainment_list = ["a comedy show", "fireworks", "the opera", "a hockey game", "paintballing", "going to The Met", "skydiving", "a city tour bus"]

# trip start
gen_start = False
def trip_gen_start():
    username = input("\nWelcome to the random day trip planner! \nWho are we creating this day trip for? Name: ")
    print(f"Hello {username}! You'll be selecting a destination, restaurant, transportation method and entertainment at random.")
    start_or_not = input("Shall we begin? Enter yes/no: ")
    if start_or_not == "yes":
        print("~~~~~\nCool! Let's begin!")
        global gen_start
        gen_start = True
        return
    elif start_or_not == "no":
        print("No problem! Hope you try again when you feel up to it!")
        return
    else:
        new_start = input("Last try, shall we begin? Enter yes/no: ")
        if new_start == "yes":
            print("Cool! Let's begin!")
            gen_start = True
            return
        elif new_start == "no":
            print("No problem! Hope you try again when you feel up to it!")
            gen_start = False
            return
        else:
            print("No problem! Hope you say yes next time =) ")
trip_gen_start()

# random pickers
trip_complete = False
def dest_picker():
    while gen_start == True and trip_complete == False:
        random_dest = random.choice(destination_list)
        user_choice = input(f"~~~~~\nFor your trip destination how about {random_dest}! Do you like this option? Enter yes/no: ")
        if user_choice == "yes" or user_choice == "Yes":
            print(f"{random_dest} is a great choice! Onto restaurants.")
            return random_dest
        elif user_choice == "no" or user_choice == "No":
            print("Let's try another destination.")
        else:
            input("Not quite sure what you mean. Enter yes/no next time.")

def rest_picker():
    while gen_start == True and trip_complete == False:    
        random_rest = random.choice(restaurant_list)
        user_choice = input(f"~~~~~\nHow about a lovely meal at {random_rest}? Enter yes/no: ")
        if user_choice == "yes" or user_choice == "Yes":
            print(f"Eating at {random_rest} will provide a fine dining experience! Your mode of transport is next!")
            return random_rest
        elif user_choice == "no" or user_choice == "No":
            print("Let's try another dining experience.")
        else:
            input("Not quite sure what you mean. Enter yes/no next time.")
            
def tran_picker():
    while gen_start == True and trip_complete == False:
        random_tran = random.choice(transportation_list)
        user_choice = input(f"~~~~~\nWould you like to get to your destination through {random_tran}? Enter yes/no: ")
        if user_choice == "yes" or user_choice == "Yes":
            print(f"A trip by {random_tran} will be a safe, fun and quick way to get your destination! Your nightly entertainment is next!")
            return random_tran
        elif user_choice == "no" or user_choice == "No":
            print("Let's try a different vehicle.")
        else:
            input("Not quite sure what you mean. Enter yes/no next time.")

def entr_picker():
    while gen_start == True and trip_complete == False:
        random_entr = random.choice(entertainment_list)
        user_choice = input(f"~~~~~\nHow about a fun activity like {random_entr}? Enter yes/no: ")
        if user_choice == "yes" or user_choice == "Yes":
            print(f"We're certain you'll have fun with {random_entr}!")
            return random_entr
        elif user_choice == "no" or user_choice == "No":
            print("Let's try another experience.")
        else:
            input("Not quite sure what you mean. Enter yes/no next time.")

# trip picker function
def trip_picker():
    global dest_picked
    dest_picked = dest_picker()
    global rest_picked
    rest_picked = rest_picker()
    global tran_picked
    tran_picked = tran_picker()
    global entr_picked
    entr_picked = entr_picker()
    print(f"~~~~~\nHere are your selections! Your day trip is set in {dest_picked} where you'll get there by {tran_picked}. \nWhile there, you'll enjoy a lovely meal at {rest_picked} and your activity of choice is {entr_picked}.")
trip_picker()

# trip dictionary
complete_trip = {dest_picked, rest_picked, tran_picked, entr_picked}

# trip complete?
while trip_complete != True:
    user_satisfied = input(f"~~~~~\nAre you happy with all of the trip selections? Enter yes/no: ")
    if user_satisfied == "yes":
        trip_complete = True
        print("~~~~~\nThank you for using this trip generator. Have a great time on your special day trip!")
    else: 
        print("Ok, let's try this again!")
        trip_picker()