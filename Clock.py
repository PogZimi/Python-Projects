# Packages needed
from os import system, name
from time import sleep

hr = 0;  # Hours
sec = 0; # Seconds
mi = 0;  # Minutes

# Clear Function , Avoid this stuff
def clear():
    if name == 'nt':
        _ = system('cls')
  
while(True):
      
      clear();
      print(":: Milo's Timer ::")
      print(" \n");
      print("--------------")
      print( hr , " : " , mi , " : " , sec , "| " )
      print("--------------")
      sec+=1;
      sleep(1);
       
      if(sec == 60):
         mi+=1;
         sec = 0;
      if(mi == 60):
         hr+=1;
         min = 0;

                  #    -Milo
