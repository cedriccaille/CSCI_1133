import turtle
import random
turtle.speed(0)
turtle.delay(0)
dict1 = {1:0, 2:90, 3:180, 4:270}
for i in range(201):
  randint = random.randint(1,4)
  turtle.setheading(dict1[randint])
  turtle.forward(20)
