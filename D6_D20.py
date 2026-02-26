import random
dnd_dice = [4,6,8,10,12,20]
print(f"Rolling Dice Good Luck")

while True:
    choise = input("press ENTER to roll all dice or type a number: ")
    
    # Mode 1: To Roll all dice
    if choise == "":
        for sides in dnd_dice:
            print(f"--- d{sides} Roll ---")
            result = random.randint(1, sides)
            print(f"Result: {result}")
            if sides == 20:
                if result == 20:
                    print(">> CRITICAL SUCCESS! <<")
                elif result == 1:
                    print(">> CRITICAL failure!<<")
            print("-" * 18 + "\n")
            
        # Mode 2: To Roll a specific die
    elif choise.isdigit():
        sides = int(choise)
        if sides in dnd_dice:
            print(f"--- d{sides} Roll ---")
            result = random.randint(1, sides)
            print(f"Result: {result}")
            if sides == 20:
                if result == 20:
                    print(">> CRITICAL SUCCESS! <<")
                elif result == 1:
                    print(">> CRITICAL failure!<<")
            print("-" * 18 + "\n")
        else:
            print(f"Invalid die! Choose from: {dnd_dice}")
            
    # Option to quit
    elif choise.lower() == 'exit':
        break
      
