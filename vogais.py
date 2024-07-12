# Example file showing a circle moving on screen
import pygame

from time import sleep

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0
corrida = False
shooting = False
Defesa = False
Nogoal = False
Golo = False

image_pos = pygame.Vector2(925, 160)
ball_pos = pygame.Vector2(960, 700)
Maignan_pos = pygame.Vector2(950, 160)
Over = pygame.image.load("over.png")

count = 0
jogador_n = 0


Crowd1 = pygame.image.load("Crowd.jpg")
Crowd1 = pygame.transform.scale(Crowd1, (660, 320))
Crowd2 = pygame.image.load("Crowd.jpg")
Crowd2 = pygame.transform.scale(Crowd2, (660, 320))
Crowd3 = pygame.image.load("Crowd.jpg")
Crowd3 = pygame.transform.scale(Crowd3, (660, 320))
frança = pygame.image.load("frança.png")
frança = pygame.transform.scale(frança, (100, 50))
portugal = pygame.image.load("portugal.png")
portugal = pygame.transform.scale(portugal, (100, 50))
vs = pygame.image.load("vs.png")
vs = pygame.transform.scale(vs, (50, 50))


Bola = pygame.image.load("bola.png")
Bola = pygame.transform.scale(Bola, (70,70))

baliza = pygame.image.load("BALIZA.png")
baliza = pygame.transform.scale(baliza, (1455, 580))

Jogador1 = pygame.image.load("Jogador1.png")
Jogador1 = pygame.transform.scale(Jogador1, (150, 300))
Jogador2 = pygame.image.load("Jogador2.png")
Jogador2 = pygame.transform.scale(Jogador2, (150, 300))
Jogador3 = pygame.image.load("Jogador3.png")
Jogador3 = pygame.transform.scale(Jogador3, (120, 300))
Jogador4 = pygame.image.load("Jogador4.png")
Jogador4 = pygame.transform.scale(Jogador4, (120, 300))
Jogador5 = pygame.image.load("Jogador5.png")
Jogador5 = pygame.transform.scale(Jogador5, (120, 300))
Jogador6 = pygame.image.load("Jogador6.png")
Jogador6 = pygame.transform.scale(Jogador6, (120, 300))
Jogador7 = pygame.image.load("Jogador7.png")
Jogador7 = pygame.transform.scale(Jogador7, (120, 300))
Jogador8 = pygame.image.load("Jogador8.png")
Jogador8 = pygame.transform.scale(Jogador8, (120, 300))
Jogador9 = pygame.image.load("Jogador9.png")
Jogador9 = pygame.transform.scale(Jogador9, (150, 300))
Jogador10 = pygame.image.load("Jogador10.png")
Jogador10 = pygame.transform.scale(Jogador10, (150, 300))
Jogador12 = pygame.image.load("Jogador12.png")
Jogador12 = pygame.transform.scale(Jogador12, (150, 300))
Jogador11 = pygame.image.load("Jogador13.png")
Jogador11 = pygame.transform.scale(Jogador11, (150, 300))
Jogador13 = pygame.image.load("Jogador1.png")
Jogador13 = pygame.transform.scale(Jogador13, (150, 300))

GOAL = pygame.image.load("GOAL.png")

Maignan = pygame.image.load("Maignan.png") 
Maignan = pygame.transform.scale(Maignan, (200, 300))

Maignan2 = pygame.image.load("Maignan2.xcf")
Maignan2 = pygame.transform.scale(Maignan2, (200, 300))

Alvo = pygame.image.load("alvo.png")
    
Alvo = pygame.transform.scale(Alvo, (70,70))

speed_x = 15
speed_y = 15

Maignanspeed_x = 8
Maignanspeed_y = 0

def reset():
    
    global ball_pos, image_pos, Maignan_pos, corrida, shooting, Defesa, Nogoal, Golo, count, jogador_n, speed_x, speed_y, Maignanspeed_x, Maignanspeed_y
    ball_pos = pygame.Vector2(960, 700)
    image_pos = pygame.Vector2(925, 160)
    Maignan_pos = pygame.Vector2(950, 160)
    corrida = False
    shooting = False
    Defesa = False
    Nogoal = False
    Golo = False
    count = 0
    jogador_n = 0
    speed_x = 15
    speed_y = 15
    Maignanspeed_x = 8
    Maignanspeed_y = 0

   

while running:

     

    
         
        
    if shooting:
        count = 0
        if count % 2 == 0 and ball_pos != image_pos:
            ball_pos.x += delta_x/30
            ball_pos.y += delta_y/30
    if corrida == True:
        count += 1
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    

    
    
    color = (0, 200, 0)
    screen.fill(color)
    
    screen.blit(Bola, ball_pos)


    color = (255,255,255)
    pygame.draw.rect(screen, color, pygame.Rect(500, 100, 960, 280))


    color = (0, 200, 0)
    pygame.draw.rect(screen, color, pygame.Rect(515, 115, 930, 365))

    imp = pygame.draw.ellipse(screen, (255, 255, 255), (965,730,60,40))
    
   
    screen.blit(Crowd1,(0,0))
    
    screen.blit(Crowd2,(660,0))
    
    screen.blit(Crowd3,(1320,0)) 

    screen.blit(baliza, (383, -10 ))

    color = (255, 255, 255)
    
    pygame.draw.rect(screen, color, pygame.Rect(0, 380, 1920, 15))
    buttons = pygame.mouse.get_pressed(num_buttons=3)
    if (buttons[0]):
        delta_x = image_pos.x - ball_pos.x
        delta_y = image_pos.y - ball_pos.y
        corrida = True
        speed_x = 0
        speed_y = 0
    if count % 5 == 0 and corrida:
        jogador_n += 1
    if jogador_n == 0:
        screen.blit(Jogador1, (820, 750))
    if jogador_n == 1:
        screen.blit(Jogador2, (825, 725))
    if jogador_n == 2:
        screen.blit(Jogador3, (830, 700))
    if jogador_n == 3:
        screen.blit(Jogador4, (835, 675))
    if jogador_n == 4:
        screen.blit(Jogador5, (840, 650))
    if jogador_n == 5:
        screen.blit(Jogador6, (845, 625))
    if jogador_n == 6:
        screen.blit(Jogador7, (850, 600))
    if jogador_n == 7:
        screen.blit(Jogador8, (855, 575))
    if jogador_n == 8:
        screen.blit(Jogador9, (860, 550))
    if jogador_n == 9:
        screen.blit(Jogador10, (860, 550))
    if jogador_n == 10:
        screen.blit(Jogador11, (860, 550))
    if jogador_n == 11 :
        screen.blit(Jogador13, (860, 550))
    if jogador_n > 11:
        shooting = True
        screen.blit(Jogador13, (860, 550))
    
   
    direction = 1
    image_pos.x += speed_x
    image_pos.y += speed_y
    if image_pos.x <= 0 or image_pos.x +70 >= 1920:
        direction *= -1
        speed_x = -speed_x

    if image_pos.y +70 >= 380 or image_pos.y <= 0:
        direction *= -1
      
        speed_y = -speed_y

    image_pos.x += speed_x
    image_pos.y += speed_y
   

    direction2 = 1
    if Maignan_pos.x <= 515 or Maignan_pos.x -70 >= 1220:
        direction2 *= -1
        Maignanspeed_x = -Maignanspeed_x

    Maignan_pos.x += Maignanspeed_x
    Maignan_pos.y += Maignanspeed_y
    maignan_rect = pygame.Rect(Maignan_pos.x, Maignan_pos.y ,200, 300)
    ball_rect = pygame.Rect(ball_pos.x, ball_pos.y, 70,70)

    if pygame.Rect.colliderect(maignan_rect, ball_rect):
        Defesa = True
        screen.blit(Maignan2, (Maignan_pos.x, Maignan_pos.y))
    
    if ball_pos == image_pos and  ball_pos.x >= 515 and ball_pos.x <= 515 + 925 and ball_pos.y <= 115 +  365 and ball_pos.y >= 115 and Defesa == False:
        Golo = True
        speed_x = +5
        speed_y = +5

    if shooting and (ball_pos.x < 515 or ball_pos.x > 515 + 925 or ball_pos.y <= 115 or Defesa == True):
        Nogoal = True


    if Nogoal == True:
        not screen.blit (Maignan2, Maignan_pos)
        not screen.blit (Bola, ball_pos)
        not screen.blit (Alvo, image_pos)
        screen.blit(Over, (800, 300))

    else :
        screen.blit (Maignan, Maignan_pos)
        screen.blit (Bola, ball_pos)
        screen.blit (Alvo, image_pos)

    if Defesa == True:
        screen.blit (Maignan2,Maignan_pos)


    if Golo == True :
        screen.blit(GOAL, (1200, 500))
        screen.blit(GOAL, (100, 500))
        ball_pos.x =960
        ball_pos.y =700

    if Nogoal == True:
        ball_pos.x =960
        ball_pos.y =700
        

    screen.blit(portugal,(150, 100))
    screen.blit(frança,(300, 100 ))
    screen.blit(vs,(250, 100)) 
    
 

    # flip() the display to put your work on screen
    pygame.display.flip()

    if Nogoal == True :
        sleep(2)
        reset()

    if Golo == True:
        
        sleep(2)
        reset()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
 

