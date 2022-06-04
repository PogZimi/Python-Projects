import random
from re import L

def game(comp, player1):
    if(comp == player1):
       return None;  # Tie 

    elif(comp == 's'):
       if(player1 == 'w'):
           return False;
       elif(player1 == 'g'):
           return True;
           
    elif(comp == 'w'):
         if(player1 == 'g'):
           return False;
         elif(player1 == 's'):
           return True

rend = random.randint(1, 3);

if(rend == 1):
   comp = 's';
elif(rend == 2):
   comp = 'w';
elif(rend == 3):
   comp = 'g';

print("   ARM_64X :  Snake(s) , Water(w) , or Gun(g) :: ");
player1 = input("  Your Turn : Snake(s) , Water(w) , or Gun(g) :: ");

a = game(comp , player1);
print(a);

if a == False:
     print("You Lose!!! ")
     print("Computer Chose :  ", comp);
     print("You Chose : ", player1);
         
elif a == None: 
     print("It's a Tie^^ ")
     print("Computer Chose :  ", comp);
     print("You Chose : ", player1);

elif a == True : 
     print("***You Won***");
     print("Computer Chose :  ", comp);
     print("You Chose : ", player1);
      