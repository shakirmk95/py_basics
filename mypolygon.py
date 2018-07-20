from swampy.TurtleWorld import *

def drawPolygon(pen, n, side, angle):
	for i in range(n) :
		fd(pen, side)
		lt(pen, angle)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.00001
drawPolygon(bob, 36000, 0.01, 0.01)

wait_for_user()
