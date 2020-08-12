import turtle
import os
import math
import random 
import time

wn = turtle.Screen()
wn.bgcolor("grey")
wn.title("Turtle")

# setting boundary
skk = turtle.Turtle() 
skk.speed(0)
skk.penup()
skk.forward(290)
skk.left(90)
skk.color('red')
skk.pensize(3)
skk.pendown()
skk.forward(290)
for i in range(4): 
    skk.left(90)
    skk.forward(290*2) 
skk.hideturtle()  

#  player

plr = turtle.Turtle()
plr.speed(0)
plr.shape('triangle')
plr.penup()
plr.setposition(0,-270)
plr.color('blue')
plr.setheading(90)

#Create Enemy

enemySpeed = 12

enemy = turtle.Turtle()
enemy.speed(0)
enemy.color('white')
enemy.shape('circle')
enemy.penup()
x = random.randint(-200,200)
y = random.randint(100, 250)
enemy.setposition(x,y)
enemy.setheading(90)

# bullets

bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setposition(plr.xcor(),plr.ycor()+10)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()


#define player movement, left and right only

playerSpeed = 15

def move_left():
    x = plr.xcor()
    x-=playerSpeed
    if x < -280:
        x = -280
    plr.setx(x)

def move_right():
    x = plr.xcor()
    x+=playerSpeed
    if x > 280:
        x = 280
    plr.setx(x)


bulletSpeed = 20 

bulletState = "ready"

def fireBullet():
    global bulletState
    #move the bullet above the player
    if bulletState == "ready":
        bulletState = "fire"
        x = plr.xcor()
        y = plr.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()


#collision Course

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance <20:
        return True
    else:
        return False

#keyboard bidding

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fireBullet, "space")


def erasableWrite(tortoise, name, font, align, reuse=None):
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser

score = 0
scr = turtle.Turtle()
scr.hideturtle()
scr.color('white')
scr.penup()
scr.setposition(250,200)
scr.write("Score :{} ".format(score), align='right',font=('Arial',20,'bold'))

# game_over = turtle.Turtle()
# game_over.hideturtle()
# game_over.color('red')
# game_over.penup()
# game_over.write('Game over!',align='center',font=('Arial',50,'bold'))
def game_over():
    game_over = turtle.Turtle()
    game_over.hideturtle()
    game_over.color('red')
    game_over.penup()
    for i in range(3):
        game_over.write('Game over!',align='center',font=('Arial',40,'bold'))
        # game_over.speed(0.001)
        time.sleep(0.5)
        game_over.clear()
        game_over.write('Game over!',align='center',font=('Arial',75,'bold'))
        game_over.clear()
    game_over.write('Game over!',align='center',font=('Arial',75,'bold'))
    scr.clear()
    scr.setposition(-50,-50)
    scr.write("Score :{} ".format(score),font=('Arial',20,'bold'))
    scr.write("                     ")
    scr.setposition(-100,-80)
    if score<6:
        # scr.newline()
        scr.write('Try again, u can do it',font=('Arial',15,'bold'))
    elif score < 11:
        scr.write('Good Try, go higher!',font=('Arial',15,'bold'))
    else:
        scr.write('U r a champion!!!',font=('Arial',15,'bold'))

if __name__ == "__main__":
    while True:
        #Move the enemy
        
        x = enemy.xcor()
        x += enemySpeed
        enemy.setx(x)


        if enemy.xcor()>280:
            y = enemy.ycor()
            y -= 40
            enemySpeed *= -1
            enemy.sety(y)

        if enemy.xcor()<-280:
            y = enemy.ycor()
            y -= 40
            enemySpeed *= -1
            enemy.sety(y)

        if bulletState == "fire":
            y = bullet.ycor()
            y += bulletSpeed
            bullet.sety(y)

        if bullet.ycor()>= 280:
            bullet.hideturtle()
            bulletState ="ready"

        #check for collision

        if isCollision(plr, enemy):
            plr.hideturtle()
            enemy.hideturtle()
            scr.clear()
            game_over()
            print("Game Over!!!")
            break

        if isCollision(bullet, enemy):
            #reset the bullet
            score+=1
            scr.clear()
            scr.write("Score :{} ".format(score), align='right',font=('Arial',20,'bold'))
            bullet.hideturtle()
            bulletState = "ready"
            bullet.setposition(0,-400)

            enemy.setposition(-200, 250)
            enemySpeed += 1

        

# w=input('s')
turtle.done() 
