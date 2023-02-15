import random
import turtle

screen = turtle.Screen()
screen.bgpic('background.gif')
screen.tracer(0)
screen.setup(600,600)
screen.addshape('pikachu_direita.gif')
screen.addshape('pikachu_esquerda.gif')
screen.addshape('pokebola.gif')
screen.addshape('balao.gif')
screen.addshape('nuvens.gif')

pikachu = turtle.Turtle()
pikachu.shape('pikachu_direita.gif')
pikachu.penup()
pikachu.goto(0,-100)

bordaD = turtle.Turtle()
bordaD.penup()
bordaD.goto(300,0)
bordaD.shape('nuvens.gif')

bordaE = turtle.Turtle()
bordaE.penup()
bordaE.goto(-300,0)
bordaE.shape('nuvens.gif')

screen.update()

pokebola = turtle.Turtle()
pokebola.left(90)
pokebola.shape('pokebola.gif')
pokebola.penup()
pokebola.goto(random.randint(-150, 150), 500)

balao = turtle.Turtle()
balao.left(90)
balao.shape('balao.gif')
balao.penup()
balao.goto(random.randint(-150, 150), 500)

label = turtle.Turtle()
label.hideturtle()
label.penup()
label.goto(-50,230)
label.color('black')

distance = 0
stamina = 30

def movimentar_pikachu_esquerda():
    if pikachu.xcor() >= -150:
        pikachu.shape('pikachu_esquerda.gif')
        x = pikachu.xcor()
        x += -8
        pikachu.setx(x)

def movimentar_pikachu_direita():
    if pikachu.xcor() <= 150:
        pikachu.shape('pikachu_direita.gif')
        x = pikachu.xcor()
        x += 8
        pikachu.setx(x)

def mover_personagem():
    screen.onkeypress(movimentar_pikachu_direita, 'd')
    screen.onkeypress(movimentar_pikachu_esquerda, 'a')
    screen.listen()

def start():
    global stamina
    global distance

    distance = 0
    stamina = 30

    label.clear()
    screen.update()

    pikachu.goto(0,-100)
    balao.goto(random.randint(-150, 150), 500)
    pokebola.goto(random.randint(-150, 150), 500)
    
    turtle.ontimer(atualizar_com_fps, 1000//60)

def mover_objetos():

    global stamina

    balao.back(3)
    pokebola.back(5)

    if balao.ycor() <= -500:
        balao.goto(random.randint(-150, 150), 500)

    if pokebola.ycor() <= -500:
        pokebola.goto(random.randint(-150, 150), 500)

    if pokebola.ycor() + 20 >= pikachu.ycor() - 20 and pokebola.ycor() - 20 <= pikachu.ycor() + 20 and pikachu.xcor() + 20 >= pokebola.xcor() - 20 and pikachu.xcor() - 20 <= pokebola.xcor() + 20:
        turtle.done()

    if balao.ycor() + 20 >= pikachu.ycor() - 20 and balao.ycor() - 20 <= pikachu.ycor() + 20 and pikachu.xcor() + 20 >= balao.xcor() - 20 and pikachu.xcor() - 20 <= balao.xcor() + 20:
        balao.goto(random.randint(-150, 150), 500)
        stamina += 10

def atualizar_placar_score():
    global distance
    global stamina

    stamina -= 0.07
    distance += 0.05

    if stamina <= 0:
        turtle.done()

    label.clear()
    label.write(f'DISTANCE: {int(distance)}\nSTAMINA: {int(stamina)}',font=('arial', 12, 'bold'))

    if pikachu.xcor() >= 150: 
        turtle.done()

    if pikachu.xcor() <= -150:  
        turtle.done()
    
def atualizar_com_fps():

    atualizar_placar_score()
    mover_objetos()
    mover_personagem()

    screen.update()
    turtle.ontimer(atualizar_com_fps, 1000//60)

turtle.onkeypress(start,'space')
screen.listen()

screen.mainloop()