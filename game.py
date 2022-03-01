import pygame as pg
from time import sleep
from random import randint

gameStage = 'Testing'
gameName = 'Hard Survival Strategie'
gameVersion = 'v0.0.2'

runBool = True
debugScreen = False
sizeX = 640
sizeY = 480
renderX = sizeX/2.5
renderY = sizeY/2.5
randX = -250
randY = 0
life = 100
hunger = 100.5
thirst = 100.5
stamina = 100
qLoad = pg.image.load

models = {
    1: 'icon.png',
    2: 'logo.png',
    3: 'models/player/frontidle.png',
    4: 'models/player/backwardsidle.png',
    5: 'models/player/leftidle.png',
    6: 'models/player/rightidle.png',
    7: 'models/enviroment/tree.png'
}

pg.init()
####### PLAYER STATES #######
idleFrontPlayer = qLoad(models[3])
idleBackwardsPlayer = qLoad(models[4])
idleLeftPlayer = qLoad(models[5])
idleRightPlayer = qLoad(models[6])
playerState = idleFrontPlayer
playerSpeed = 0.03
####### MODELS #######
tree = qLoad(models[7])
####### INITIAL MODULES #######
logo = qLoad(models[2])
render = pg.display.set_mode((sizeX, sizeY))
pg.display.set_caption(gameStage + ' - ' + gameName + ' - ' + gameVersion)
pg.display.set_icon(qLoad(models[2]))
font = pg.font.SysFont('fonts/PressStart2P.ttf', 14)
render.blit(logo, (sizeX/4, sizeY/4))
pg.display.update()
sleep(3)
###############################

def worldGeneration():
    render.blit(tree, (randX, randY))

def playerStatus():
    render.blit(playerState, (renderX, renderY))

def HUD():
    pg.draw.rect(render, (0, 0, 0), [sizeX/32, sizeY*0.75, 210, 100])
    pg.draw.rect(render, (255, 0, 0), [sizeX/25, sizeY*0.8, life*2, 15])
    render.blit((font.render(str(int(life)), True, (30, 30, 30))), (sizeX/5.5, sizeY*0.806))
    pg.draw.rect(render, (255, 128, 0), [sizeX/25, sizeY*0.84, hunger*2, 15])
    render.blit((font.render(str(int(hunger)), True, (30, 30, 30))), (sizeX/5.5, sizeY*0.846))
    pg.draw.rect(render, (0, 77, 230), [sizeX/25, sizeY*0.88, thirst*2, 15])
    render.blit((font.render(str(int(thirst)), True, (30, 30, 30))), (sizeX/5.5, sizeY*0.886))
    pg.draw.rect(render, (0, 255, 0), [sizeX/25, sizeY*0.92, stamina*2, 15])
    render.blit((font.render(str(int(stamina)), True, (30, 30, 30))), (sizeX/5.5, sizeY*0.926))

def debug():
    if debugScreen == True:
        render.blit((font.render(gameName + ' (' + gameStage + ') - ' + gameVersion, True, (0, 0, 0))), (10, 10))
        render.blit((font.render('X: ' + str(int(renderX)) + ' Y: ' + str(int(renderY)), True, (0, 0, 0))), (10, 20))

while runBool:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runBool = False
        if event.type == pg.KEYUP:
            if event.key == pg.K_F3:
                debugScreen = not debugScreen

    kInput = pg.key.get_pressed()
    kMods = pg.key.get_mods()
    if kInput[pg.K_w]:
        renderY -= playerSpeed
        playerState = idleFrontPlayer
    if kInput[pg.K_s]:
        renderY += playerSpeed
        playerState = idleBackwardsPlayer
    if kInput[pg.K_a]:
        renderX -= playerSpeed
        playerState = idleLeftPlayer
    if kInput[pg.K_d]:
        renderX += playerSpeed
        playerState = idleRightPlayer
    if stamina <= 100:
        stamina += 0.001
    if stamina >= 100:
        stamina = 100
    if stamina >= 0.1:
        if kInput[pg.K_w] and kInput[pg.K_LSHIFT]:
            renderY -= playerSpeed
            playerState = idleFrontPlayer
            stamina -= 0.007
            hunger -= 0.000005
            thirst -= 0.0001
        if kInput[pg.K_s] and kInput[pg.K_LSHIFT]:
            renderY += playerSpeed
            playerState = idleBackwardsPlayer
            stamina -= 0.007
            hunger -= 0.000005
            thirst -= 0.0001
        if kInput[pg.K_a] and kInput[pg.K_LSHIFT]:
            renderX -= playerSpeed
            playerState = idleLeftPlayer
            stamina -= 0.007
            hunger -= 0.000005
            thirst -= 0.0001
        if kInput[pg.K_d] and kInput[pg.K_LSHIFT]:
            renderX += playerSpeed
            playerState = idleRightPlayer
            stamina -= 0.007
            hunger -= 0.000005
            thirst -= 0.0001
    if hunger <= 0:
        hunger = 0
        life -= 0.003
    if thirst <= 0:
        thirst = 0
        life -= 0.004
    if life <= 0:
        life = 0
        runBool = False

    if renderX <= -32:
        randX = randint(10, sizeX-70)
        randY = randint(10, sizeY-70)
        renderX = sizeX
    elif renderX >= sizeX+1:
        randX = randint(10, sizeX-70)
        randY = randint(10, sizeY-70)
        renderX = -31
    if renderY <= -48:
        randX = randint(10, sizeX-70)
        randY = randint(10, sizeY-70)
        renderY = sizeY
    elif renderY >= sizeY+1:
        randX = randint(10, sizeX-70)
        randY = randint(10, sizeY-70)
        renderY = -47
    hunger -= 0.000008
    thirst -= 0.00005

    render.fill((20, 100, 10))
    playerStatus()
    worldGeneration()
    HUD()
    debug()
    pg.display.update()
