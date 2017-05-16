import pygame
import time
import random
pygame.init()

# Colors

white = (255,255,255)
black = (0,0,0)


red = (200,0,0,100)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)
blue = (0,0,255)

#that's canvas size

display_width = 800
display_height  = 600

game_cont = False

#setting the display

gameDisplay = pygame.display.set_mode((display_width,display_height))

#setting Icon , title

pygame.display.set_caption('Sneat')
icon = pygame.image.load("image/snake.png")
pygame.display.set_icon(icon)

#setting image

img = pygame.image.load("image/snake.png")
appleimg = pygame.image.load("image/0.gif")
appleimg1 = pygame.image.load("image/1.gif")
appleimg2 = pygame.image.load("image/2.gif")
appleimg3 = pygame.image.load("image/3.gif")
appleimg4 = pygame.image.load("image/4.gif")
appleimg5 = pygame.image.load("image/5.gif")
appleimg6 = pygame.image.load("image/6.gif")
appleimg7 = pygame.image.load("image/7.gif")
appleimg8 = pygame.image.load("image/8.gif")
appleimg9 = pygame.image.load("image/9.gif")
appleimg10 = pygame.image.load("image/10.gif")
appleimg11 = pygame.image.load("image/11.gif")
appleimg12 = pygame.image.load("image/12.gif")
applimages = [appleimg,appleimg1,appleimg2,appleimg3,appleimg4,appleimg5,appleimg6,appleimg7,appleimg8,appleimg9,appleimg10,appleimg11,appleimg12]

clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 10

#that my font,font-size

bigfont = pygame.font.Font("font/fill.ttf",25)
smallfont = pygame.font.Font("font/fill.ttf", 40)
medfont = pygame.font.Font("font/fill.ttf", 70)
largefont = pygame.font.Font("font/fill.ttf", 100)
bfont = pygame.font.Font("font/fill.ttf", 200)

scores = 0
text = smallfont.render("score: "+str(scores),True,black)

def score(score):
    global scores, text
    scores += 5
    text = smallfont.render("score: "+str(scores),True,black)

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    if size == "big":
        textSurface = bigfont.render(text, True, color)
    if size == "b":
        textSurface = bfont.render(text, True, color)         

    return textSurface, textSurface.get_rect()


def text_to_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size = "small"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
    gameDisplay.blit(textSurf , textRect) 

def message_to_screen(msg,color,y_displace=0,size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
  
    textRect.center = (int(display_width/2),int(display_height/2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color,action = None):
    global game_cont
    global game_mode
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(cur)


    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "Quit":
                snake_eat.play()
                
                pygame.quit()
               

            if action == "Modes":
                game_mode = True
                game_cont = True
                snake_eat.play()
            if action == "play":
                pygame.mixer.music.pause()
                snake_eat.play()

                

                timer()
              
            if action == "main_menu":
                snake_eat.play()
               
                game_intro()       

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,red,x,y,width,height)                 

        
    
def timer():

    
    gameDisplay.fill(white)
    gm_msg = ["Go", "Steady", "Ready"] 
    for i in range(3, 0, -1):

      
      

        message_to_screen(str(i), black, size="large")


        message_to_screen(gm_msg[i - 1],red,y_displace = -100,size="large")
      
        
      
        pygame.display.update()
        gameDisplay.fill(white)
        time.sleep(1)
    gameLoop()    
        
def pause():
    if paused == True:
    	message_to_screen("paused",black,-100,size="large")
    	messedage_to_screen("press C to continue or Q to quit",black,25)
        
    
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event .key == pygame.K_c:
                    gameLoop()
                elif event.key == pygame.K_q:
                    pygame.quit()
      

        
        clock.tick(5)
                

def randAppleGen():
    randAppleX = round(random.randrange(60, display_width-60))#/10.0)*10.0
    randAppleY = round(random.randrange(60, display_height-60))
    return randAppleX,randAppleY
    
def game_intro():

    intro = True
    speed = 5
    
    while intro:
        for event in pygame.event.get():
            print event             
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                	timer()

                            

        gameDisplay.fill(green)
        
     
        message_to_screen("welcome to Sneat",black,-100,"large")
        message_to_screen("Press c to continue",black,220,"big")
        
  
  
        pygame.display.update()

def snake(block_size, snakelist):
    if snake_state == "right":
        head = pygame.transform.rotate(img, 270)

    if snake_state == "left":
        head = pygame.transform.rotate(img, 90)

    if snake_state == "up" or snake_state == "default":
        head = img

    if snake_state == "down":
        head = pygame.transform.rotate(img, 180)
        
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])


def gameLoop():
    global FPS,colors, snake_state,scores, text,go_to_menu
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    snake_state = "default"

    lead_x_change = 0
    lead_y_change = 0
 

    snakeList = []
    snakeLength = 1
    timer = False
    paused = False
    randAppleX,randAppleY = randAppleGen()#/10.0)*10.0
    
    
    while not gameExit:

        while gameOver:

            button("play", 150,500,100,50, blue, light_green,action="play" )
            button("Quit", 550,500,100,50, red, light_red,action="Quit")                
            pygame.display.update()
            clock.tick(15)
        
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_state != "right":
                    lead_x_change = -block_size
                    lead_y_change = 0
                    snake_state = "left"
                
                elif event.key == pygame.K_RIGHT and snake_state != "left":
                    lead_x_change = block_size
                    lead_y_change = 0
                    snake_state = "right"
                elif event.key == pygame.K_UP and snake_state != "down":
                    lead_y_change = -block_size
                    lead_x_change = 0
                    snake_state = "up"
                elif event.key == pygame.K_DOWN and snake_state != "up":
                    lead_y_change = block_size
                    lead_x_change = 0
                    snake_state = "down"


                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_u:
                	paused = False
                        

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(white)

        AppleThickness = 30
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            
            gameOver = True
            scores = 0
            text = smallfont.render("score: "+str(scores),True,black)


        gameDisplay.blit(appleimg7,(randAppleX,randAppleY))
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
    
        if len(snakeList) > snakeLength:
            del snakeList[0]
        
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
                scores = 0
                text = smallfont.render("score: "+str(scores),True,black)
                message_to_screen("oh no you  run into you self",black,y_displace= 70,size = "large")
                FPS = 10

        
        snake(block_size, snakeList)
        gameDisplay.blit(text,[0,0])
        pygame.display.update() 

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1
                score(5)
                FPS *= 1.02
                pygame.display.update()
             
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1
                score(5)
                FPS *= 1.02
                pygame.display.update()
              
                  
        pygame.display.update()

        clock.tick(FPS)
        
    pygame.quit()
    quit()
game_intro()    
gameLoop()    







          




