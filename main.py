import turtle as tr
colors = ["#FF0018", "#FFA52C", "#FFFF41", "#008018", "#0000F9", "#86007D"]
tr.penup()
tr.setx(-700)
tr.speed(500)
tr.pensize(35)
tr.color("black")
tr.pendown()
for color in colors:
    tr.pencolor(color)

    tr.penup()
    for i in range(90):
        tr.fd(2)
        tr.rt(1)

    tr.pendown()
    for i in range(270):
        tr.fd(2)
        tr.rt(1)

    tr.left(90)
    tr.fd(350)

    for i in range(180):
        tr.fd(2)
        tr.rt(1)

    tr.rt(90)
    tr.fd(230)
    tr.rt(180)
    tr.fd(230)
    tr.rt(90)

    tr.fd(350)
    tr.lt(90)

    for i in range(270):
        tr.fd(2)
        tr.rt(1)

    tr.penup()

    for i in range(90):
        tr.fd(2)
        tr.rt(1)

while True:
    tr.rt(1)