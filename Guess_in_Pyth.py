import random
# Created by me 

#Variables initialization
randnum = 0;
ug = 0;
guess = 0;

randnum = random.randint(1, 100);    # Generates Random Number between 1 to 100
# print(randnum);

# Main loop
while(ug!=randnum):

     ug = int(input("Enter your guesses :  ")) # User Input 

     if(ug == randnum):
      print("You won!!!!");
      print("Tries : ", guess)

     elif(ug != randnum):
      print("You Lose!!!!");
     guess+=1;

das = guess - 1;
with open("Score.txt", "w") as f:
    f.write(str(das));  # Creates a file with name Score.txt & pastes your score there 
    
