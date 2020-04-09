import turtle

turtle.forward(100)
turtle.pencolor('blue')

turtle.forward(100)

turtle.reset()

# for i in range(100):
#     turtle.fd(i)
#     turtle.left(95)

colors = ['red', 'blue', 'orange', 'green']

names = ['Fibi', 'Flytiger', 'Tedo', 'Ketty']
for i in range(100):
    turtle.pencolor(colors[i % 4])
    turtle.penup()
    turtle.fd(i * 4)
    turtle.pendown()
    turtle.write(names[i%4], font=('Arial', int((i+4)/4), 'bold'))
    turtle.left(95)

turtle.done()