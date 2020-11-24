#Problem A
def mms(counts):
    '''
    Purpose: uses dictionary of all the M&M colors and responds whether Muriel will eat the M&Ms depending on the conditions
    Input Parameter(s): counts -- dictionary, each key is a string representing the M&M color, and the value is an integer of the number count of M&Ms
    Return Value: Response to whether Muriel will eat them, Type String. Either "Yes" or "No"
    '''
    if (counts['yellow'] > counts['blue']) and (counts['green'] % 3 == 0) or (counts['green'] % 5 == 0):
        response = 'Yes'
    else:
        response = 'No'
    return response

#Problem B
def choice(text,optionA,optionB,optionC):
    '''
    Purpose: Take in four string values, one is the prompt, and the other three are possible options. Prompt user to pick one of the choices
    Input Parameter(s): All string type. First, text, is the prompt. Next three are the options that the user can choose from.
    Return Value: The one character string that the user decides, which corresponds to the option. If no choice, this defults to option A.
    '''
    dict1 = {"A": optionA, "B": optionB, "C": optionC}

    print(text)
    print()
    print("A. " + dict1["A"])
    print("B. " + dict1["B"])
    print("C. " + dict1["C"])

    answer = input("Choose A, B, or C: ")

    if answer in dict1:
        return answer
    else:
        print("Invalid option, defaulting to A")
        answer = "A"
        return answer

#Problem C
def adventure():
    '''
    Purpose: To give the user a sequence of choices, leading to one of several endings
    Input Parameter(s): None. Use the "choice" function from the last problem
    Return Value: a boolean value, True if the user reaches a good ending, False if the user reaches a bad ending
    '''
    decision = choice("\nYou're at Dinkytown McDonalds. It's 2AM. You're plastered. What do you order?",
                    "Chicken Nuggets",
                    "McChicken and McDouble",
                    "Big Mac")
    state = 1
    if state == 1:
        if decision == "B":
            print("\nYou made a terrible mistake. You instantly get the runs and sprint to the bathroom to salvage your underwear. You spend the rest of the night in agony.\n")
            return False
        elif decision == "A":
            print("\nReasonable choice. They are a little overpriced and unsatisfying, though, so you look for more food.\n")
            state = 2
        elif decision == "B":
            print("\nCongrats, you made the right decision. You saved money and are extremely satisfied. Time to go home.\n")
            state = 4

    decision2 = choice("\nOn your stroll down Dinkytown, you find yourself at a fork in the road. Where do you go next?",
                    "Insomnia Cookies",
                    "Blarney's Pub & Grille",
                    "Home")
    if state == 2:
        if decision2 == "C":
            print("\nYou're so responsible. Your liver, wallet, and stomach thank you. Keep marching on!\n")
            state = 3
        elif decision2 == "B":
            print("\nWow. Why on God's green earth did you decide to drink MORE?? Well, as the story goes, you're blacked out and puking on the bartop. However, you made new friends and had a fun photoshoot. Smile for the picture!\n")
            return True
        elif decision2 == "A":
            print("\nWoof! Those double chocolate chunks just hit the spot. Expensive, but always worth it. The drunchies never stop, so you continue your expedition.\n")
            state = 3

    decision3 = choice("\nAh, the warm, welcoming hue of the Frank & Andrea's pizza sign. You almost walk in, but notice shouting coming from the bars behind you. What's your next move?",
                    "F*** it, you're only in college once!!",
                    "Gotta call it a night.",
                    "Eh, I could eat. Gimme some mac & cheese pizza, please.")

    if state == 3:
        if decision3 == "B":
            print("\nGreat choice. You avoided further disturbance to your digestive tract and your bank account. Let's get to bed.\n")
            state = 4
        elif decision3 == "C":
            print("\nWell, if there was ever time to get some delicious pizza, it would be now. Dig in!\n")
            return True
        elif decision3 == "A":
            print("\nDude, are you serious? You made it this far withou...nevermind. Obviously you get outrageously drunk, make it on barstoolsports, and become a legend. Morning's gonna be tough, though...\n")
            return False

    decision4 = choice("\nYou're here. The holy grail. Defeated the final boss. You are going to head up to bed, but you hear two groups in the background, one laughing and having fun upstairs, the other partying hard outside. What are you going to do?",
                    "It's way past my bedtime. Let's end the night on a good note.",
                    "Duty calls! Let the party rage on.",
                    "I do love seeing my friends and don't have the energy to move. Seems like a great compromise!")

    if state == 4:
        if decision4 == "A" or decision4 == "C":
            print("\nFinally. You're in bliss. What a wonderful adventure you had today.\n")
            return True
        elif decision4 == "B":
            print("\nSO CLOSE. IN YOUR HOUSE. ALMOST IN YOUR ROOM. Something about those white claws is just irresistable. Enjoy your splitting headache in the morning, and don't forget to mix in a water!\n")
            return False
