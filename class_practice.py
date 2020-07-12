class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def draw(self):
        print('draw')
    def move(self):
        print('move')


point1=Point(10,20)
#point1.x=100

print(point1.x)

point1.draw()