import pygame
import random

pygame.init()

screen_w = 600
screen_h = 500
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Space War')

def write(text, x=5, y=5):
    black = (225, 225, 255)
    font = pygame.font.SysFont(None, 55)
    a = font.render(text, True, black)
    screen.blit(a, [x, y])

def image(img, x, y):
    while y>0:
        screen.blit(img, (x, y))
        pygame.display.update()
        y-=1

def rand():
    pass
    

# Images
startup = pygame.image.load('Images\startup.jpg').convert_alpha()
background = pygame.image.load('Images\\background.png').convert_alpha()
player = pygame.image.load('Images\\player.png').convert_alpha()
bullet = pygame.image.load('Images\\bullet.png').convert_alpha()
enmy_1 = pygame.image.load('Images\\enmy_1.png').convert_alpha()
enmy_2 = pygame.image.load('Images\\enmy_2.png').convert_alpha()
enmy_3 = pygame.image.load('Images\\enmy_3.png').convert_alpha()
enmy_4 = pygame.image.load('Images\\enmy_4.png').convert_alpha()
enmy_5 = pygame.image.load('Images\\enmy_4.png').convert_alpha()


def gameloop():
    # Veriables
    player_x = 250
    player_y = 400
    bullet_y = 380
    enmy_1_x = 500
    enmy_1_y = 10
    enmy_2_x = 250
    enmy_2_y = 10
    enmy_3_x = 100
    enmy_3_y = 10
    enmy_4_x = 400
    enmy_4_y = 10
    enmy_5_x = 50
    enmy_5_y = 10
    a = 0
    heart = 3
    score = 0

    with open('Hi_score.txt') as f:
        hi_score = int(f.read())


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()

                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RIGHT:
                                    player_x+=50
                                    a = 0.1
                                
                                elif event.key == pygame.K_LEFT:
                                    player_x-=50
                                    a = -0.1

                                elif event.key == pygame.K_RETURN:
                                    heart+=1

                                elif event.key == pygame.K_UP:
                                    pygame.mixer.music.load('Sounds\shoot02wav-14562.mp3')
                                    pygame.mixer.music.play()
                                    image(bullet, player_x+42, bullet_y)
                                    if abs (enmy_1_x - player_x)<50 and (enmy_1_y - bullet_y)<20:
                                        enmy_1_x = random.randint(0,10)
                                        if enmy_1_x == 0:
                                            enmy_1_x = 0
                                        elif enmy_1_x == 1:
                                            enmy_1_x = 50
                                        elif enmy_1_x == 2:
                                            enmy_1_x = 100
                                        elif enmy_1_x == 3:
                                            enmy_1_x = 150
                                        elif enmy_1_x == 4:
                                            enmy_1_x = 200
                                        elif enmy_1_x == 5:
                                            enmy_1_x = 250
                                        elif enmy_1_x == 6:
                                            enmy_1_x = 300
                                        elif enmy_1_x == 7:
                                            enmy_1_x = 350
                                        elif enmy_1_x == 8:
                                            enmy_1_x = 400
                                        elif enmy_1_x == 9:
                                            enmy_1_x = 450
                                        elif enmy_1_x == 10:
                                            enmy_1_x = 500
                                        # rand(enmy_1_x)
                                        enmy_1_y = -100
                                        score+=1

                                    if abs (enmy_2_x - player_x)<50 and (enmy_2_y - bullet_y)<20:
                                        enmy_2_x = random.randint(0,10)
                                        if enmy_2_x == 0:
                                            enmy_2_x = 0
                                        elif enmy_2_x == 1:
                                            enmy_2_x = 50
                                        elif enmy_2_x == 2:
                                            enmy_2_x = 100
                                        elif enmy_2_x == 3:
                                            enmy_2_x = 150
                                        elif enmy_2_x == 4:
                                            enmy_2_x = 200
                                        elif enmy_2_x == 5:
                                            enmy_2_x = 250
                                        elif enmy_2_x == 6:
                                            enmy_2_x = 300
                                        elif enmy_2_x == 7:
                                            enmy_2_x = 350
                                        elif enmy_2_x == 8:
                                            enmy_2_x = 400
                                        elif enmy_2_x == 9:
                                            enmy_2_x = 450
                                        elif enmy_2_x == 10:
                                            enmy_2_x = 500
                                        enmy_2_y = -100
                                        score+=1

                                    if abs (enmy_3_x - player_x)<50 and (enmy_3_y - bullet_y)<20:
                                        enmy_3_x = random.randint(0,10)
                                        if enmy_3_x == 0:
                                            enmy_3_x = 0
                                        elif enmy_3_x == 1:
                                            enmy_3_x = 50
                                        elif enmy_3_x == 2:
                                            enmy_3_x = 100
                                        elif enmy_3_x == 3:
                                            enmy_3_x = 150
                                        elif enmy_3_x == 4:
                                            enmy_3_x = 200
                                        elif enmy_3_x == 5:
                                            enmy_3_x = 250
                                        elif enmy_3_x == 6:
                                            enmy_3_x = 300
                                        elif enmy_3_x == 7:
                                            enmy_3_x = 350
                                        elif enmy_3_x == 8:
                                            enmy_3_x = 400
                                        elif enmy_3_x == 9:
                                            enmy_3_x = 450
                                        elif enmy_3_x == 10:
                                            enmy_3_x = 500
                                        enmy_3_y = -100
                                        score+=1

                                    if abs (enmy_4_x - player_x)<50 and (enmy_4_y - bullet_y)<20:
                                        enmy_4_x = random.randint(0,10)
                                        if enmy_4_x == 0:
                                            enmy_4_x = 0
                                        elif enmy_4_x == 1:
                                            enmy_4_x = 50
                                        elif enmy_4_x == 2:
                                            enmy_4_x = 100
                                        elif enmy_4_x == 3:
                                            enmy_4_x = 150
                                        elif enmy_4_x == 4:
                                            enmy_4_x = 200
                                        elif enmy_4_x == 5:
                                            enmy_4_x = 250
                                        elif enmy_4_x == 6:
                                            enmy_4_x = 300
                                        elif enmy_4_x == 7:
                                            enmy_4_x = 350
                                        elif enmy_4_x == 8:
                                            enmy_4_x = 400
                                        elif enmy_4_x == 9:
                                            enmy_4_x = 450
                                        elif enmy_4_x == 10:
                                            enmy_4_x = 500
                                        enmy_4_y = -100
                                        score+=1

                                    if abs (enmy_5_x - player_x)<50 and (enmy_5_y - bullet_y)<20:
                                        enmy_5_x = random.randint(0,10)
                                        if enmy_5_x == 0:
                                            enmy_5_x = 0
                                        elif enmy_5_x == 1:
                                            enmy_5_x = 50
                                        elif enmy_5_x == 2:
                                            enmy_5_x = 100
                                        elif enmy_5_x == 3:
                                            enmy_5_x = 150
                                        elif enmy_5_x == 4:
                                            enmy_5_x = 200
                                        elif enmy_5_x == 5:
                                            enmy_5_x = 250
                                        elif enmy_5_x == 6:
                                            enmy_5_x = 300
                                        elif enmy_5_x == 7:
                                            enmy_5_x = 350
                                        elif enmy_5_x == 8:
                                            enmy_5_x = 400
                                        elif enmy_5_x == 9:
                                            enmy_5_x = 450
                                        elif enmy_5_x == 10:
                                            enmy_5_x = 500
                                        enmy_5_y = -100
                                        score+=1

                        enmy_1_y+=0.15
                        enmy_2_y+=0.2
                        enmy_3_y+=0.1
                        enmy_4_y+=0.2
                        enmy_5_y+=0.18
                        player_x+=a
                        screen.blit(background, (0,0))
                        screen.blit(player, (player_x, player_y))
                        screen.blit(enmy_1, (enmy_1_x,enmy_1_y))
                        screen.blit(enmy_2, (enmy_2_x,enmy_2_y))
                        screen.blit(enmy_3, (enmy_3_x,enmy_3_y))
                        screen.blit(enmy_4, (enmy_4_x,enmy_4_y))
                        screen.blit(enmy_5, (enmy_5_x,enmy_5_y))

                        if abs (enmy_1_y > screen_w):
                            enmy_1_y = 0
                            enmy_1_x = random.randint(1,600)
                            heart-=1
                            pygame.mixer.music.load('Sounds\\blast-flamethrower-cooldown-7142.mp3')
                            pygame.mixer.music.play()
                            
                        if abs (enmy_2_y > screen_w):
                            enmy_2_y = 0
                            enmy_2_x = random.randint(1,600)
                            heart-=1
                            pygame.mixer.music.load('Sounds\\blast-flamethrower-cooldown-7142.mp3')
                            pygame.mixer.music.play()
                            
                        if abs (enmy_3_y > screen_w):
                            enmy_3_y = 0
                            enmy_3_x = random.randint(1,600)
                            heart-=1
                            pygame.mixer.music.load('Sounds\\blast-flamethrower-cooldown-7142.mp3')
                            pygame.mixer.music.play()
                            
                        if abs (enmy_4_y > screen_w):
                            enmy_4_y = 0
                            enmy_4_x = random.randint(1,600)
                            heart-=1
                            pygame.mixer.music.load('Sounds\\blast-flamethrower-cooldown-7142.mp3')
                            pygame.mixer.music.play()
                            
                        if abs (enmy_5_y > screen_w):
                            enmy_5_y = 0
                            enmy_5_x = random.randint(1,600)
                            heart-=1
                            pygame.mixer.music.load('Sounds\\blast-flamethrower-cooldown-7142.mp3')
                            pygame.mixer.music.play()
                            

                        if abs (player_x < 0):
                            a = 0.1

                        if abs (player_x > screen_h):
                            a = -0.1

                        if score>hi_score:
                            with open('Hi_score.txt', 'w') as g:
                                g.write(str(score))
                        
                        if heart<1:
                            gameloop()

                        write(f'Heart: {heart}                        Score: {score}')
                        pygame.display.update()

        screen.blit(startup, (0,0))
        write(f'Hi-score: {hi_score}')
        pygame.display.update()

gameloop()    