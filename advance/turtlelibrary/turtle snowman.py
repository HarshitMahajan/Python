import turtle
 
t = turtle.Turtle()
 
def draw_circle(color, radius, x, y):
  t.penup()
  t.fillcolor(color)
  t.goto(x,y)
  t.pendown()
  t.begin_fill()
  t.circle(radius)
  t.end_fill()
 
#Below three statements for drawing snowman body
draw_circle("#ffffff", 30, 0, -40)
draw_circle("#ffffff", 40, 0, -100)
draw_circle("#ffffff", 60, 0, -200)
 
draw_circle("#ffffff", 2, -10, -10) #Drawing left eye
draw_circle("#ffffff", 2, 10, -10) #Drawing right eye
draw_circle("#FF6600", 3, 0, -15) #Drawing nose
 
#Below three statements for drawing buttons
draw_circle("#ffffff", 2, 0, -35)
draw_circle("#ffffff", 2, 0, -45)
draw_circle("#ffffff", 2, 0, -55)
 
#Code for drawing left arm
t.penup()
t.goto(-15,-35)
t.pendown()
t.pensize(5)
t.goto(-75, -50)
#Code for drawing right arm
t.penup()
t.goto(15,-35)
t.pendown()
t.pensize(5)
t.goto(75, -50)
 
#Code for drawing hat
t.penup()
t.goto(-35, 8)
t.color("black")
t.pensize(6)
t.pendown()
t.goto(35, 8)
 
t.goto(30, 8)
t.fillcolor("black")
t.begin_fill()
t.left(90)
t.forward(15)
t.left(90)
t.forward(60)
t.left(90)
t.forward(15)
t.end_fill()
