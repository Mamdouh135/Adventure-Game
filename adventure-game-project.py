# importing random in order to choose random events each time the user plays
import random
# importing time in order to make a delay between each line
import time

# This is the color of the wand used in the game
wand_color = random.choice(['blue', 'green', 'red', 'purple', 'orange'])

# choosing random creature in order to be in the house when the user opens it
CREATURE = random.choice(["pirate", "dragon", "troll", "gorgon"])

# This is used to start and stop the game.
GAME_IS_ON = True


# print statements in order with a second delay
def print_pause(text: str) -> None:
    # This variable is used to control the delay between displaying statements
    # in the story.
    delay_time = 2
    # I use the escape sequence '\n' to split each statement into a list,
    # allowing me to display them sequentially and in order. I used the
    for i in text.split("\n"):
        print(i)
        # time.sleep() function to introduce a one-second delay between each
        # statement.
        time.sleep(delay_time)


# get and check user input, repeat if wrong
def input_and_validate(text):
    print(text)
    answer = input()
    if answer in ("1", "2"):
        return answer
    else:
        input_and_validate(text)


# This code prompts the user to choose whether to play, repeating the
# question until a valid response is received.
def play_again():
    global GAME_IS_ON, got_into_cave
    answer = input("Would you like to play again? (y/n)").lower()
    if answer == "y":
        GAME_IS_ON = True
        got_into_cave = False
        print_pause("Excellent! Restarting the game ...")

    elif answer == "n":
        GAME_IS_ON = False
    else:
        play_again()


# This function is called whenever the user decides to open the house.
def defend():
    # These are the consequences that result from the user's choice of attack.
    first_defending_scenario = "You do your best...\nbut your rusty old " \
                               f"{wand_color} magic " \
                               f"wand is no match for the {CREATURE}.\nYou " \
                               "have been turned into a frog!"
    second_defending_scenario = f"Congrats! You have defeated the {CREATURE}"
    third_defending_scenario = "As the gorgon moves to cast a spell, you " \
                               "raise your new Wand of Ogoroth.\nThe " \
                               f"Wand of Ogoroth shines brightly in your hand"\
                               f" as you brace yourself for the spell.\n" \
                               f"But the {CREATURE} takes one look at your " \
                               f"shiny new wand and runs away!\nYou have " \
                               f"rid the town of the {CREATURE}. " \
                               "You are victorious!"
    
    answer = input_and_validate("Would you like to (1) cast a spell or (2) "
                                "run away?")
    if answer == "1":
        if not got_into_cave:
            print_pause(random.choice([first_defending_scenario,
                                       second_defending_scenario]))
        else:
            print_pause(third_defending_scenario)
        play_again()
    else:
        field()


# This boolean variable indicates whether the user has entered the cave or not.
got_into_cave = False


# This function is called when the user chooses to enter the cave,
# and afterwards, it is known that the user has entered the cave. using the
# variable got_into_cave
def cave():
    global got_into_cave
    # These are the events that take place in the cave. The first event occurs
    # if the user has not entered it before, while the second event occurs if
    # they have.
    first_cave_scenario = "You peer cautiously into the cave.\nIt turns out " \
                          "to be" \
                          " only a very small cave.\nYour eye catches a " \
                          "glint of " \
                          "metal behind a rock.\nYou have found the magical " \
                          "Wand" \
                          f" of Ogoroth!\nYou discard your rusty old" \
                          f" {wand_color} magic " \
                          "wand " \
                          "and take the Wand of Ogoroth with you.\nYou walk " \
                          "back out to the field."
    second_cave_scenario = "You peer cautiously into the cave.\nYou’ve " \
                           "been here " \
                           "before, and gotten all the good stuff. It’s " \
                           "just an " \
                           "empty cave now.\nYou walk back out to the field."

    if got_into_cave:
        print_pause(second_cave_scenario)
    else:
        print_pause(first_cave_scenario)
    got_into_cave = True
    house()


# This function is called when the user chooses to run away from the creature.
def field():
    print_pause("You run back into the field. Luckily, you don't seem to "
                "have been followed.\n ")
    house()


# This function is called in most cases, including at the start, when the
# user runs away, and when the user enters the cave.
def house():
    # String formatting is then utilized to add creature name to the house
    # scenario.
    first_house_scenario = f"You approach the door of the house.\nYou " \
                           f"are about " f"to " f"knock when the doo" \
                           f"r opens and out steps a {CREATURE}.\nEep" \
                           f"! This is the {CREATURE}’s house!\nThe " \
                           f"{CREATURE} finds " "you!\nYou ""feel a bit " \
                           "under-prepared for this, what with only " \
                           "having "f"a tiny, rusty old {wand_color} " \
                           f"magic wand."
    second_house_scenario = "You approach the door of the house.\nYou " \
                            "are about ""to knock when the door " \
                            "opens and out steps a "F"{CREATURE}.\nEep! " \
                            F"This is the {CREATURE}’s " "house!\nThe " \
                            ""F"{CREATURE} finds you!"
    print_pause(
        'Enter 1 to knock on the door of the house.\nEnter 2 '
        'to peer into the cave.'

    )
    answer = input_and_validate("What would you like to do?")
    if answer == "1":
        if got_into_cave:
            print_pause(second_house_scenario)
        else:
            print_pause(first_house_scenario)
        defend()
    else:
        cave()


# At the start of the story, could be used as a shorthand-function to refer to
# the beginning of the story.
def starter_function():
    text = "You find yourself standing in an open field, filled with grass " \
           "and yellow wildflowers.\nRumor has it that a pirate is somewhere "\
           "around here, and has been terrifying the nearby village.\nIn " \
           "front of you is a house.\nTo your right is a dark cave.\nIn your "\
           "hand you hold your trusty (but not very effective) rusty old " \
           f"{wand_color} magic wand."

    print_pause(text)

    house()


while GAME_IS_ON:
    starter_function()

time.sleep(2)
print("Thanks for playing! See you next time.")
