#geo jump

from Enemy import *
from You import *   #Difference between 'from you import *' and 'import time'???
import time

def newEnemy(win: GraphWin, list:list):   

    if Box.count == 0:  
        type = 1

    else:
        type = random.randint(1, 3)

    if type == 1:
        x = Box(win)
        list.append(x)
    if type == 2:
        x = Cone(win)
        list.append(x)      
    if type == 3:
        x = Sphere(win)
        list.append(x)
    
    x.draw(win)  


def main():
    #Create window and background
    win = GraphWin("Test Window", 800, 500)
    r = Rectangle(Point(800, 400), Point(0, 500))
    r.setFill("Brown")
    r.draw(win)

    #create player character
    u = You(win)
    u.drawYou(win)

    #Create instance of each type of enemy to start
    s = Sphere(win)
    t = Cone(win)
    b = Box(win)
    Box.count = 1

    nmeList = [b, t, s]  

    for nme in nmeList:
        nme.draw(win)
    #Run game Condition
    while u.alive:
        #Enemy actions            
        #Run through list of each enemy and move
        for nme in nmeList:
            nme.charge()
            if 750<= nme.getX() or nme.getX() <= 0:   
                nme.flip()
            if Circle.testCollision_CircleVsRectangle(u.ball, nme.hitbox):
                nme.hit()
                nme.undraw()
                if nme.health > 0:
                    nme.draw(win)
                else:
                    nmeList.remove(nme)
                    newEnemy(win, nmeList)
                    if len(nmeList) < 6:
                        newEnemy(win, nmeList)
                u.jump(win, True)
            if Circle.testCollision_CircleVsRectangle(u.ball, nme.killbox):
                u.alive = False

                
        #Player actions
        key = win.checkKey()

        if key == "Up" and not u.bouncing and u.grounded:
            u.jump(win, True)

        u.jump(win, False)
        if key == "Left" or key == "Right":
           u.roll(key)      

        time.sleep(0.01)
        win.setBackground("White")
    win.setBackground("Red")
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
