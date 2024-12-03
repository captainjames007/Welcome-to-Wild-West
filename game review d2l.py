# Chapter 1: Into Dry Creek
def chapter_1():
    print("Chapter 1: Into Dry Creek")
    print("Jake rides into the dusty town of Dry Creek, knowing the sheriff isn't far behind.")

    choice = input("Do you want to (A) Fight your way out of town or (B) Sneak away? ")

    # Only accept 'A' for fighting your way out
    if choice == "A":
        print("You fight your way out of town, gaining weapons and reputation. Look at you, tough as nails!")
        return "fight_outcome"
    else:
        print("Invalid choice. Try again, cowboy! Only 'A' will do.")
        return chapter_1()  # Retry the chapter if the input is invalid


# Chapter 2: Mountain Hideout
def chapter_2():
    print("Chapter 2: Mountain Hideout")
    print("Jake and his gang retreat to a mountain hideout, where they prepare for the heist.")

    choice = input("Do you want to (A) Stay and defend the hideout or (B) Leave to get to the train early? ")

    # Only accept 'A' for staying and defending
    if choice == "A":
        print("You stay to defend the hideout. Some gang members fall, but you hold strong. You’re basically the sheriff now...sort of.")
        return "defend_hideout"
    else:
        print("Invalid choice. Come on, partner! Pick 'A' to fight!")
        return chapter_2()  # Retry the chapter if the input is invalid


# Chapter 3: The Gold Train
def chapter_3():
    print("Chapter 3: The Gold Train")
    print("Jake’s gang prepares to ambush the gold train in a narrow canyon. The sheriff is also on his way.")

    choice = input("Do you want to (A) Set up the ambush and stop the train or (B) Fight with the guards aboard the train to get to the gold? ")

    # Only accept 'A' for setting up the ambush
    if choice == "A":
        print("You set up the ambush and stop the train, securing the gold. But man, the sheriff’s men are close!")
        return "ambush_outcome"
    else:
        print("Invalid choice. Come on, you can’t rob a train without picking 'A'!")
        return chapter_3()  # Retry the chapter if the input is invalid


# Chapter 4: The Chase
def chapter_4():
    print("Chapter 4: The Chase")
    print("With the gold in hand, Jake's crew tries to escape, but the sheriff isn’t far behind.")

    choice = input("Do you want to (A) Cross the dangerous mountains or (B) Head across the open desert? ")

    # Only accept 'A' for crossing the mountains
    if choice == "A":
        print("You cross the mountains, gaining some distance but losing gang members to exhaustion. At least you’re not in the desert, right?")
        return "mountain_outcome"
    else:
        print("Invalid choice. Choose 'A' for mountains!")
        return chapter_4()  # Retry the chapter if the input is invalid


# Chapter 5: The Final Showdown
def chapter_5():
    print("Chapter 5: The Final Showdown")
    print("Jake and Sheriff Hartman meet face-to-face in a Western standoff. This is the final test.")

    choice = input("Do you want to (A) Negotiate with Hartman or (B) Fight Hartman? ")

    # Only accept 'A' for negotiating
    if choice == "A":
        print("You try to negotiate with Hartman. If you’ve been good to your gang, he might strike a deal. Otherwise, he’ll just shoot you.")
        return "negotiate_outcome"
    else:
        print("Invalid choice. It's showdown time, partner! Pick 'A' to talk!")
        return chapter_5()  # Retry the chapter if the input is invalid


# Main game function to control the game flow
def main_game():
    print("Welcome to 'Outlaw's Last Ride'! The wild west awaits!")

    result = chapter_1()  # Start the game with Chapter 1

    if result == "fight_outcome":
        print("You now move on to Chapter 2: Mountain Hideout with more resources. Look at you, all prepared and stuff.")
        chapter_2()  # Call chapter_2 after chapter_1
    else:
        print("Unexpected error. Maybe the cowboy gods are mad at you. Try again.")

    result = chapter_3()  # Proceed to Chapter 3
    if result == "ambush_outcome":
        print("You set up the ambush and the gold is yours, but the sheriff is closer now. Let’s see how this plays out!")
        chapter_4()  # Call chapter_4 after chapter_3
    else:
        print("Unexpected error. This ain’t no time for messing up! Try again.")

    result = chapter_4()  # Proceed to Chapter 4
    if result == "mountain_outcome":
        print("The mountain escape was tough, but you gained some distance. Now, to face the sheriff once and for all.")
        chapter_5()  # Call chapter_5 after chapter_4
    else:
        print("Unexpected error. Guess the sheriff caught up with you. Try again.")

    result = chapter_5()  # Proceed to the final showdown
    if result == "negotiate_outcome":
        print("You successfully negotiated with Hartman and escaped with the gold. But who can trust an outlaw?")
    else:
        print("Unexpected error. Maybe the west is just too wild for you. Try again.")


# Start the game by calling the main_game function
if __name__ == "__main__":
    main_game()
