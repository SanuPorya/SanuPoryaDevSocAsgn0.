import pygame,sys,random

# game restart system
def ball_restart():
    ball.center=(width/2,height/2)
    ball_speed_y *=random.choice((1,-1))
    ball_speed_x *=random.choice((1,-1))

#general setup 

pygame.init()
clock = pygame.time.Clock()

#sreen setup

width = 1280 
height = 900
screen = pygame.display.set_mode((width , height))  # yaha mein galti kardi thi yaha tuple nahi dala tha 
pygame.display.set_caption('ANIRBAN')

# game drawing 

ball = pygame.Rect((width /2)-5,(height /2)-5,10,10)
player = pygame.Rect(width-10,(height/2)-100,10,200)
opponent = pygame.Rect(0,(height/2)-100,10,200)

bg_colour = pygame.Color('grey12')
light_grey=(200,200,200)
ballcolour= (220,220,220)

# ball movement 
ball_speed_x = 7   ##yaha change karna hai to make the game difficult 
ball_speed_y = 7

# game restart 
def ball_restart():
    ball.center = (width/2,height/2)



while True :

    for event in pygame.event.get():
        if event.type == pygame.quit:   # yaha meine Game.quit likh diya tha kyuki i felt that yeah hamare se banayi gayi conditionn hai , Latter on I realize that it is just a pygame feature 
            pygame.quit()
            sys.exit()

            # ball movement is here 
    ball.x +=ball_speed_x
    ball.y +=ball_speed_y

    # key pressing commands 
    if event.type ==pygame.KEYDOWN:
        if event.key ==pygame.K_DOWN:
            player.y +=7
        elif event.key ==pygame.K_UP:
            player.y -=7

    #stop palyer andd opponent from leaving the screen 
    if player.top <=0:
        player.top = 0
    if player.bottom >=height  :
        player.bottom =height
    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >=height  :
        opponent.bottom =height
    
    # opponent movement 
    if ball.left <= (width/2):
        if opponent.top >= ball.top:  
            opponent.y -= 12
        if opponent.bottom<= ball.bottom:
            opponent.y += 12
    else :
        if opponent.top<=(height/2-50):
            opponent.y += 5
        if opponent.bottom >= (height/2 +50):
            opponent.y -= 5 

    # ball collide with screen 
    if (ball.top <=0 or ball.bottom >=height):
        ball_speed_y *=-1
    if ( ball.left <= 0 or ball.right >= width ):
        if (ball.left<=0):
            ball_restart()
        elif (ball.right>=width ):
            ball_restart()
    


    if (ball.colliderect(player)or (ball.colliderect(opponent))):
        ball_speed_x *=-1  # here i can change something to increase the speeed so the gaem will increase in difficulty over time 
        ball_speed_x +=0.2
        ball_speed_y +=0.2


    screen.fill(bg_colour)
    pygame.draw.rect(screen,light_grey,player)  # yeh sare visual s hai or bas entities kesi dikhengi woh dikhata hai matlab makeup 
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,ballcolour,ball)
    pygame.draw.aaline(screen , light_grey, ((width/2),0),((width/2),height))
    pygame.display.flip()
    clock.tick(60)