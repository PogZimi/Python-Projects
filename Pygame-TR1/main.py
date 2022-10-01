import pygame 

# PN --> My this is just a joke not an actual game , i am learning pygame ( trying to create small projects from them by myself this is one of them ) 

# Intiazlize module 
pygame.init()

# Window settings 
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('rocket.png')

pygame.display.set_caption("SpaceCraZ")
pygame.display.set_icon(icon)

# Enemy settings 
pX = 370
pY = 400
p_change = 0
p_change2 = 0

# Player Settings 
pX1 = 374.79999999997835
pX2 = 32.900000000000496
p3 = 0
p4 = 0

# Importing Images 
pimage = pygame.image.load('monst.png')
pimage2 = pygame.image.load('player.png')

# Setting up our player images,co-ordinates 
def player(x,y, x1,x2):
     screen.blit(pimage2, (x1,x2))
     screen.blit(pimage, (x,y))

# Main loop
running = True 
while running:

    # Set bg Colour ( rgb )
    screen.fill((0, 0, 0))

    # Closing Window 
    for event in pygame.event.get():
         if(event.type == pygame.QUIT):
               running = False 
         
         # Key input mechanism for Enemy
         if(event.type == pygame.KEYDOWN):
             if(event.key == pygame.K_LEFT):
                   p_change = -0.1
             elif(event.key == pygame.K_RIGHT):
                   p_change = 0.1 
             if(event.key == pygame.K_UP):
                   p_change2 = -0.1
             elif(event.key == pygame.K_DOWN):
                   p_change2 = 0.1        

         if(event.type == pygame.KEYUP):
             if(event.key == pygame.K_LEFT):
                   p_change = 0
             elif(event.key == pygame.K_RIGHT):
                   p_change = 0
             elif(event.key == pygame.K_UP):
                   p_change2 = 0
             elif(event.key == pygame.K_DOWN):
                   p_change2 = 0
         
         # Key Input mechanism for our player 
         if(event.type == pygame.KEYDOWN):
             if(event.key == ord('a')):
                   p3 = -0.1
             elif(event.key == ord('d')):
                   p3 = 0.1 
             if(event.key == ord('w')):
                   p4 = -0.1
             elif(event.key == ord('s')):
                   p4 = 0.1                 

         if(event.type == pygame.KEYUP):
             if(event.key == ord('a')):
                   p3 = 0
             elif(event.key == ord('d')):
                   p3 = 0
             elif(event.key == ord('w') ):
                   p4 = 0
             elif(event.key == ord('s')):
                   p4 = 0

           
    # Making the boundaries 
    if(pX <= 0):
         pX = 0
    elif(pX >= 736):
         pX = 0
    if(pY <= 0):
         pY = 0
    elif(pY >= 536):
         pY = 0
    if(pX1 <= 0):
         pX1 = 0
    elif(pX1 >= 736):
         pX1 = 0
    if(pX2 <= 0):
         pX2 = 0
    elif(pX2 >= 536):
         pX2 = 0
    
    # Updating Co-ordinates of both players 
    pX += p_change
    pY += p_change2
    
    pX1 += p3 
    pX2 += p4 



    # Creating Player 
    player(pX, pY,pX1,pX2)
    
    # Updating screen
    pygame.display.update()

