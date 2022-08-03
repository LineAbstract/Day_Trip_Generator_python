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

# trip picker function

# trip dictionary

# trip complete?
