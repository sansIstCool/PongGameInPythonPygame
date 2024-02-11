import pygame as dev , sys , time

dev.init()
dev.mixer.init()

clock = dev.time.Clock()

WIDTH = 600
HEIGHT = 400
score = 0
gameState = ""

window = dev.display.set_mode((WIDTH,HEIGHT))
dev.display.set_caption("cool game")

hitSound = dev.mixer.Sound("hit.wav")


icon = dev.image.load("sans.png")
dev.display.set_icon(icon)

ball = dev.Rect(0,0,30,30)
ball.center = (WIDTH/2 , HEIGHT/2)

cpu = dev.Rect(0 , 0 , 20 , 100)
cpu.centery = HEIGHT / 2

player = dev.Rect(0 , 0 , 20 , 100)
player.midright = (WIDTH , HEIGHT/2)

font = dev.font.Font("Karma Future.otf" , 32)


ballSpeedX = 6
ballSpeedY = 6
playerSpeed = 0
cpu_speed = 6

while True:
    for event in dev.event.get():
        if event.type == dev.QUIT:
             sys.exit()
        if event.type == dev.KEYDOWN:
            if event.key == dev.K_UP:
                playerSpeed = -6
            if event.key == dev.K_DOWN:
                playerSpeed = 6
        if event.type == dev.KEYUP:
            if event.key == dev.K_UP:
                playerSpeed= 0
            if event.key == dev.K_DOWN:
                playerSpeed = 0
    ball.x += ballSpeedX
    ball.y += ballSpeedY
    
    player.y += playerSpeed
    cpu.y += cpu_speed
    
    if ball.bottom >= HEIGHT or ball.top <= 0:
        ballSpeedY *= -1
    if ball.right >= WIDTH or ball.left <= 0:
        ballSpeedX *= -1
    if player.y <= 0 :
        player.y = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
    if cpu.y <= 0 :
        cpu.y = 0
        cpu_speed = 6
    if cpu.bottom >= HEIGHT:
        cpu.bottom = HEIGHT
        cpu_speed = -6
    if ball.colliderect(player):
        score += 1
        ballSpeedX = -6
        ballSpeedY = -6
        hitSound.play()
    if ball.colliderect(cpu):
        score += -1
        ballSpeedX = 6
        ballSpeedY = 6
        hitSound.play()
    
        
        
    window.fill("black")
    
    wintext = font.render(gameState ,False , 'white' )
    txt = font.render("score:"+str(score) ,False , 'white')
    
    
    
    dev.draw.aaline(window , "white" , (WIDTH / 2 , 0) , (WIDTH /2  ,HEIGHT ))
    dev.draw.ellipse(window , "white" , ball)
    dev.draw.rect(window , "white" , cpu)
    dev.draw.rect(window , "white" , player)
    window.blit(txt , (WIDTH / 2 - 50 , 50))
    window.blit(wintext , (WIDTH / 2 -50, HEIGHT /2 - 50))
    if(score == 5):
        score = 0
        gameState = "You Win"
        
        
       
    if(score == -5):
        score = 0
        gameState = "You Lose"
    if(gameState == "You Win" or gameState == "You Lose"):
        time.sleep(0.2)
        sys.exit()
   
    
    
    dev.display.update()
    clock.tick(60)
dev.quit()
