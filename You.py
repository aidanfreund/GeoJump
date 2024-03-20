from graphics import *

class You:
    def __init__(self, win: GraphWin):
        ##Build a ball object in the bottom center of window
        self.rad = 15
        self.win = win
        self.x = win.getWidth() // 2
        self.y = win.getHeight() - self.rad - 100
        self.ball = Circle(Point(self.x, self.y), self.rad)
        self.dy = 0  #change in y value for the bounce
        self.alive = True
        self.bouncing = False
        self.falling = False
        self.grounded = True

    def drawYou(self, win: GraphWin):
        #Draws the ball in the win canvas
        self.ball.setFill("Green")
        self.ball.draw(win)

    def roll(self, direction):
        #window size 0-800
        if direction == "Right" and self.x < 800 - self.rad:   
            self.ball.move(4, 0)
            self.x += 4
        if direction == "Left" and self.x > 0 + self.rad:
            self.ball.move(-4, 0)
            self.x -= 4

    
    def jump(self, win:GraphWin, bounce:bool):
        """Will initiate a jump/bounce if true is passed for bounce.
         otherwise, will move ball up or down in time with enemys"""
        if bounce:
            self.dy = 16     #will jump an additional 136 pixels
            self.bouncing = True
            self.falling = False
            self.grounded = False
        if self.bouncing:
            self.ball.move(0, -self.dy)    
            self.y -= self.dy
            self.dy -= 1
            if self.dy == 0:
                self.bouncing = False
                self.falling = True

        #fall
        if self.falling:
            self.dy += 1
            self.ball.move(0, self.dy)    
            self.y += self.dy
            #terminal velocity
            if self.dy == 11:
                self.dy = 10    # terminal velocity
            if self.y >= 385:       #ground = 500(win height) - 100 - self.rad
                self.falling = False
                self.grounded = True
                self.dy = 0
                
    def die(self):
        print("dead")
        del self
def test():
    win = GraphWin("Test Window", 800, 500)
    r = Rectangle(Point(800, 400), Point(0, 500))
    r.setFill("Brown")
    r.draw(win)
    u = You(win)
    u.drawYou(win)

if __name__ == '__main__':
    test()