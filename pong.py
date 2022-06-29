import pygame 
import random
def ball_animation():
    global ball_spd_x,ball_spd_y
    ball.x+=ball_spd_x
    ball.y+=ball_spd_y

    if ball.top<=0 or ball.bottom >= screen_height:
            ball_spd_y*=-1
    if ball.left<=0 or ball.right >= screen_width:
            ball_restart()

    if ball.colliderect(player) :
            ball_spd_x *= -1
    if ball.colliderect(opponent) :
            ball_spd_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <=0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height   

def opponent_animation():
    if opponent.top < ball.y :
        opponent.top += opponent_speed
    if opponent.bottom > ball.y :
        opponent.bottom -= opponent_speed
    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height  

def ball_restart():
    global ball_spd_x,ball_spd_y
    ball.center = (screen_height/2,screen_width/2)
    ball_spd_y *= random.choice((1,-1))
    ball_spd_x *= random.choice((1,-1))
pygame.init()
clock = pygame.time.Clock()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong game")

ball = pygame.Rect(screen_width/2-5,screen_height/2-5,10,10)
player = pygame.Rect(screen_width-20,screen_height/2-23,3,46)
opponent = pygame.Rect(10,screen_height/2-23,3,46)

bg_color = pygame.Color("grey12")
light_grey = (200,200,200)
ball_spd_x = 5 * random.choice((1,-1))
ball_spd_y = 5 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

z = True
while z:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            z = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed+=7
            if event.key == pygame.K_UP:
                player_speed-=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed-=7
            if event.key == pygame.K_UP:
                player_speed+=7

    ball_animation()
    player_animation()
    opponent_animation()
     

    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))


    pygame.display.flip()
    clock.tick(60)
            