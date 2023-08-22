# Imported libraries
import random

# Function Definitions
def rps(choice):
    ai_num = random.randint(1,3)

    # Below logic represents whether the selected choice wins(1), loses(-1) or results in a draw(0)
    rock_logic = {
        1 : 0,
        2 : -1,
        3 : 1
    }
    paper_logic = {
        1 : 1,
        2 : 0,
        3 : -1
    }
    scissors_logic = {
        1 : -1,
        2 : 1,
        3 : 0
    }
    game_logic = [rock_logic, paper_logic, scissors_logic]

    decision = game_logic[choice-1].get(ai_num)
    rpsMessage(choice,ai_num,decision)

def rpsNames(choice):
    names = {
        1 : "Rock",
        2 : "Paper",
        3 : "Scissors"
    }
    return names.get(choice)

def rpsMessage(choice,ai_num,decision):
    print(f"\nYour Choice: {rpsNames(choice)} or {choice}")
    print(f"AI Choice: {rpsNames(ai_num)} or {ai_num}")
    
    results ={
        1 : "Won",
        0 : "Tied",
        -1 : "Lost"
    }

    if(decision == 1):
        global player_score 
        player_score += 1
    elif(decision == -1):
        global ai_score
        ai_score += 1

    print(f"Player {results.get(decision)} against AI!\n")

# Main Logic
player_name = str(input("Enter your name: "))
player_choice = 0

player_score = 0
ai_score = 0

while(player_choice != 4):
    print("Choose an option: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    player_choice = int(input())

    if(player_choice not in range(1,5)):
        print("Enter correct option!")
    
    if(player_choice != 4):
        rps(player_choice)

print("\n- Scorecard -")
print(f"{player_name} {player_score}")
print(f"AI \t{ai_score}\n")

if(player_score > ai_score):
    print(f"{player_name} won!")
elif(player_score < ai_score):
    print(f"AI won!")
else:
    print(f"{player_name} and AI had a draw!")