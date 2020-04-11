import turtle
wn=turtle.Screen()

def rectangle():
  for i in range(2):
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

def rectangle2():
  for i in range(2):
    turtle.forward(320)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

def rectangle3():
  for i in range(2):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)

def rectangle4():
  for i in range(2):
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

def change():
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)

def germany_flag():
    turtle.fillcolor('black')
    turtle.begin_fill()
    rectangle()
    turtle.end_fill()
    change()
    turtle.fillcolor('red')
    turtle.begin_fill()
    rectangle()
    turtle.end_fill()
    change()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    rectangle()
    turtle.end_fill()
    turtle.hideturtle()



def poland_flag():
  turtle.fillcolor('red')
  rectangle2()
  turtle.right(90)
  turtle.forward(100)
  turtle.left(90)
  turtle.begin_fill()
  rectangle2()
  turtle.end_fill()
  turtle.hideturtle()

def french_flag():
  turtle.fillcolor('blue')
  turtle.begin_fill()
  rectangle3()
  turtle.end_fill()
  turtle.forward(100)
  rectangle3()
  turtle.forward(100)
  turtle.fillcolor('red')
  turtle.begin_fill()
  rectangle3()
  turtle.end_fill()

def bulgaria_flag():
  rectangle()
  change()
  turtle.fillcolor('green')
  turtle.begin_fill()
  rectangle()
  turtle.end_fill()
  change()
  turtle.fillcolor('red')
  turtle.begin_fill()
  rectangle()
  turtle.end_fill()


def dhabi_flag():
  for i in range(1):
    turtle.color("red")
    turtle.begin_fill()
    rectangle3()
    turtle.end_fill()
    turtle.forward(100)
    turtle.color("green")
    turtle.begin_fill()
    rectangle()
    turtle.end_fill()
    change()
    rectangle()
    change()
    turtle.fillcolor('black')
    turtle.begin_fill()
    rectangle()
    turtle.end_fill()


while True:
  choice=input("Which flag would you like? 1 for Germany, 2 for Poland, 3 for France, 4 for Bulgaria,5 for Abu Dhabi:")
  speed=int(input("What speed wuld you like it to go? (1 - 100)"))

  if choice== 1:
    turtle.speed(speed)
    germany_flag()
  elif choice == 2:
    turtle.speed(speed)
    poland_flag()
  elif choice == 3:
    turtle.speed(speed)
    french_flag()
  elif choice == 4:
    turtle.speed(speed)
    bulgaria_flag()
  elif choice == 5:
    turtle.speed(speed)
    dhabi_flag()
  else:
    print("Sorry, we don't have that flag yet!")
