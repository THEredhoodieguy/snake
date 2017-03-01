#written for python 3.0+
#Matthew Pletcher 2017

from random import *

global UP, DOWN, LEFT, RIGHT
UP = 1
DOWN = 3
LEFT = 2
RIGHT = 4

class Snek(object):
    """the player object, a snek that grows as it eats"""

    global UP, DOWN, LEFT, RIGHT

    def __init__(self, startx, starty, startlen=1, startdir=UP):
        self.x = startx
        self.y = starty
        #how long the snek is, determines how many spaces in the tail array 
        self.length = startlen
        #dir represents the direction the snek is facing, 1 = up, 2 = left, 3 = down, 4 = right
        self.dir = startdir
        self.tail = list()


    def update(self):

        #update movement
        self.tail_update()
        if(self.dir == UP):
            self.y -= 1
        elif(self.dir == DOWN):
            self.y += 1
        elif(self.dir == LEFT):
            self.x -= 1
        elif(self.dir == RIGHT):
            self.x += 1


    def eat(self):
        """updates the length of the snek"""

        self.length += 1


    def tail_update(self):
        """updates the position of all tail segments"""

        prevx = self.x
        prevy = self.y
        current_dir = self.dir

        self.tail.insert(0, (prevx, prevy, current_dir))

        if len(self.tail) > self.length:
            self.tail.pop()

    def turn_left(self):
        #turns the snek left
        self.dir += 1
        if self.dir < 1:
            self.dir = 4
        if self.dir > 4:
            self.dir = 1

    def turn_right(self):
        #turns the snek right
            self.dir -= 1
            if self.dir < 1:
                self.dir = 4
            if self.dir > 4:
                self.dir = 1


class Fruit(object):
    """a fruit, has a position, and a type(as of yet, not sure what types there will be)"""

    def __init__(self, x, y, ftype=1):
        self.x = x
        self.y = y
        self.ftype = ftype 



class GameKeeper(object):
    """the game object, keeps track of score, gamestate, etc"""

    def __init__(self, xbound, ybound):
        self.xbound = xbound
        self.ybound = ybound
        self.snek = Snek(xbound // 2, ybound // 2)
        self.fruits = []
        self.score = 0
        
        #gamestate is either 0, 1, or 2
        #0 means the game has not started
        #1 is for a game in progress
        #2 is for a game that has ended
        self.gamestate = 0

        #add a fruit to the game
        #self.fruits.append(Fruit(randint(0, self.xbound), randint(0, self.ybound)))
        self.add_fruit()


    def update(self):
        #check to see if there are any fruits
        if(len(self.fruits) == 0):
            self.add_fruit()

        self.snek.update()

        #check for collision with snek and walls
        if(self.snek.x > self.xbound - 1 or self.snek.x < 0 or self.snek.y > self.ybound - 1 or self.snek.y < 0):
            self.game_over()
        #checking for collisions with snek and its tail
        for i in self.snek.tail:
            if self.snek.x == i[0] and self.snek.y == i[1]:
                self.game_over()
        #check for collisions with snek and fruit
        for i in self.fruits:
            if self.snek.x == i.x and self.snek.y == i.y:
                self.snek.eat()
                self.fruits.remove(i)
                self.score += 1


    def add_fruit(self):
        #add a fruit with a random location to the list of fruits
        randx = int(gauss(self.xbound // 2, self.xbound // 3.5))
        randy = int(gauss(self.ybound // 2, self.ybound // 3.5))
        
        #make sure the coordinates of the fruit are inside of the game's bounds
        if randx < 0: randx = 0
        if randx > self.xbound - 1: randx = self.xbound - 1
        if randy < 0: randy = 0
        if randy > self.ybound - 1: randy = self.ybound - 1

        # print()
        # print("add_fruit() called, coords generated:")
        # print(randx, randy)


        self.fruits.append(Fruit(randx, randy))
        #self.fruits.append(Fruit(randint(0, self.xbound), randint(0, self.ybound)))


    def start_game(self):
        """sets the gamestate to start"""
        self.gamestate = 1


    def game_over(self):
        """sets the gamestate as over"""
        self.gamestate = 2


    def new_game(self):
        self.snek = Snek(self.xbound // 2, self.ybound // 2)
        self.fruits = []
        self.score = 0
        self.gamestate = 1

        self.fruits.append(Fruit(randint(0, self.xbound), randint(0, self.ybound)))