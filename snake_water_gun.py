import random #imported an inbuilt random module in python
"""
Snake-Water-Gun Game 🎮
Developer: Jidnyasa Pawar
"""

def play_game(rounds= 5): # starting a function to play 5 rounds 
    yourDict = {"s" : 1, "w" : -1, "g" : 0}   # my dictionary
    reversedDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}  #reversed dictionary

    user_score = 0  # Initiated scores to zero
    computer_score = 0  #Initiated scores to zero

    print("🐍 Welcome to Snake–Water–Gun Game 🎮")
    print("Rules: s = Snake, w = Water, g = Gun")
    print(f"Best of {rounds} rounds! \n")

    for i in range(1, rounds + 1):
        print(f"\n ---- Round {i} ----")   
        
        #Computers input
        computer = random.choice([1 , -1 , 0])  # computer will choose randomly since we have used random module

        #Users input
        youstr =input("Enter your choice (s/w/g): ")  #Entering user choice
        if youstr not in yourDict:
            print("❌Invalid input!!!, Skipping this round")  #Skipping round since Given choice is not in dictionary
            continue
        you = yourDict[youstr]

        print(f"You choosed : {reversedDict[you]}")  
        print(f"computer choosed : {reversedDict[computer]}\n")

        #Check wins
        if computer == you: #Sinced both choosed same
            print("🤝It's a Draw!!")

        else: 
            if(computer == -1 and you == 1) or (computer ==0 and you == -1) or (computer ==1 and you == 0):
                print("✅YOU WIN THIS ROUND!!! \n Congratulations!!!")
                user_score += 1  

            else:
                print("❌COMPUTER WIN THIS ROUND! \n TRY AGAIN!")
                computer_score +=1


    
        print(f" \n  Score -->\n Your Score = {user_score}\n Computer Score = {computer_score}")

    #Final Result
    print("\n-----Final Result-----")
    if(computer_score>user_score):
        print("😢 You Lose!!!, Try again....")
    elif(computer_score<user_score):
        print("🎉You Won!!!, Congratulations....")
    else:
        print("🤝 It's an overall draw, play again")

## Main loop with replay option
while True:
    play_game(rounds=5)
    again = input("Do you want to play again : (y/n)  ").lower()
    if again != "y":
        print("Thanks for playing.. Goodbye")
        break


