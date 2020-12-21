import turtle, math, random

#Problem A -- Simulating Gravity
class Lander(turtle.Turtle):
    '''
    Purpose:
    Instance Variables:
    Methods:
    '''
    def __init__(self, xpos, ypos, vx, vy):
        turtle.Turtle.__init__(self)
        self.vx = vx
        self.vy = vy
        self.fuel = 50
        self.setheading(90)
        self.penup()
        self.speed(0)
        self.setpos(xpos, ypos)
    def move(self):
        self.vy -= 0.0486
        newx = self.xcor() + self.vx
        newy = self.ycor() + self.vy
        self.setpos(newx, newy)
    def thrust(self):
        if self.fuel > 0:
            self.fuel -= 1
            angle = math.radians(self.heading())
            cosine = math.cos(angle)
            sine = math.sin(angle)
            self.vx += cosine
            self.vy += sine
            print(self.fuel)
        else:
            print('Out of fuel')
    def thrust_left(self):
        if self.fuel > 0:
            self.fuel -= 1
            self.left(10)
            print(self.fuel)
        else:
            pass
    def thrust_right(self):
        if self.fuel > 0:
            self.fuel -= 1
            self.right(10)
            print(self.fuel)
        else:
            pass
    def check_lander(self, other):
        dx = abs(self.xcor() - other.xcor())
        dy = abs(self.ycor() - other.ycor())
        if dx < 15 and dy < 15:
            return True
        else:
            return False

class Meteor(turtle.Turtle):
    '''
    Purpose:
    Instance Variables:
    Methods:
    '''
    def __init__(self, xpos, ypos, vx, vy):
        turtle.Turtle.__init__(self)
        self.vx = vx
        self.vy = vy
        self.color('red')
        self.shape('circle')
        self.speed(0)
        self.penup()
        self.setpos(xpos, ypos)
        self.animate()
    def animate(self):
        newx = self.xcor() + self.vx
        newy = self.ycor() + self.vy
        if newx < 0 or newx > 1000:
            newx = random.randint(0, 1000)
        if newy < 0 or newy > 1000:
            newy = 1000
            self.vy = random.uniform(-2,0)
        self.vy -= 0.1
        self.setpos(newx, newy)
        # turtle.Screen().ontimer(self.animate, 30)


class Game:
    '''
    Purpose:
    Instance Variables:
    Methods:
    '''
    def __init__(self):
        turtle.delay(0)
        turtle.setworldcoordinates(0, 0, 1000, 1000)
        self.player = Lander(random.randint(100,900), random.randint(500,900), random.uniform(-5,5), random.uniform(-5,0))
        self.player.turtlesize(2)
        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.thrust_left, 'Left')
        turtle.onkeypress(self.player.thrust_right, 'Right')
        self.mlist = []
        self.crash = False
        for i in range(15):
            xpos = random.randint(0, 1000)
            ypos = random.randint(0, 1000)
            vx = random.uniform(-2, 2)
            vy = random.uniform(-2, 2)
            self.mlist.append(Meteor(xpos, ypos, vx, vy))
        self.gameloop()
        turtle.listen()
        turtle.mainloop()
    def gameloop(self):
        self.player.move()
        for m in self.mlist:
            m.animate()
            if self.player.check_lander(m) == True:
                self.crash = True
            else:
                pass
        if self.crash == True:
            turtle.hideturtle()
            turtle.penup()
            turtle.setpos(500,500)
            turtle.color('red')
            turtle.write("You crashed!", move = False, align = 'center', font = ('Arial', 20, 'normal'))
        else:
            if self.player.ycor() < 10:
                if (self.player.vx >= -3 and self.player.vx <= 3) and (self.player.vy >= -3 and self.player.vy <= 3):
                    turtle.hideturtle()
                    turtle.penup()
                    turtle.setpos(500,500)
                    turtle.color('green')
                    turtle.write("Successful landing!", move = False, align = 'center', font = ('Arial', 20, 'normal'))
                else:
                    turtle.hideturtle()
                    turtle.penup()
                    turtle.setpos(500,500)
                    turtle.color('red')
                    turtle.write("You crashed!", move = False, align = 'center', font = ('Arial', 20, 'normal'))
            else:
                turtle.Screen().ontimer(self.gameloop, 30)

'''turtle.delay(0)
turtle.setworldcoordinates(0, 0, 1000, 1000)
for i in range(15):
    xpos = random.randint(0, 1000)
    ypos = random.randint(0, 1000)
    vx = random.uniform(-2, 2)
    vy = random.uniform(-2, 2)
    m = Meteor(xpos, ypos, vx, vy)'''
# turtle.mainloop()

Game()
#Problem B -- Turning
#Problem C -- Game Over
#Problem D -- Meteors
