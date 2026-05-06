'''

Stone 0 
paper 1
Scissors -1 

'''

import random

print("=== Stone Paper Scissors ===\n")
print("s = Stone")
print("p = Paper")
print("sc = Scissors\n")

# Mapping
choices = {'s': 0, 'p': 1, 'sc': -1}
reverse = {0: "Stone", 1: "Paper", -1: "Scissors"}

computer = random.choice([0, 1, -1])

youstr = input("Enter your choice (s/p/sc): ").strip().lower()

if youstr not in choices:
    print("❌ Invalid input! Please enter s, p or sc")
else:
    you = choices[youstr]
    
    print(f"\nYou chose     : {reverse[you]}")
    print(f"Computer chose: {reverse[computer]}")
    
    if computer == you:
        print("🤝 It's a Draw!")
    elif (computer == 1 and you == 0) or \
         (computer == -1 and you == 1) or \
         (computer == 0 and you == -1):
        print("😔 You Lose!")
    else:
        print("🎉 You Win!")
