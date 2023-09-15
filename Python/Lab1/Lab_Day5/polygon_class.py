# Create class and sub-class objects which represent different geometrical shapes, 
# such as Rectangles and Squares
# objects should have methods to display area and perimeter

class Shapes:
    def __init__(self,shapename,length, width):
        self.shapename = shapename
        self.length = length
        self.width = width

    def calcArea(self):#shapename, length, width):
        if self.shapename == 'square':
            calc_area =  self.length * self.width
            return(calc_area)
        elif self.shapename == 'rectangle':
            calc_area = self.length * self.width
            return(calc_area)
        else:
            exit

    def calcPerimeter(self):
        if self.shapename == 'square':
            calc_perim = 4*self.length
            return(calc_perim)
        elif self.shapename == 'rectangle':
            calc_perim = 2 * (self.length + self.width )
            return(calc_perim)
        else:
            exit

# main

#square
square = Shapes("square",2,2)
print('Area of square = ',square.calcArea())
print('Perimeter of square = ',square.calcPerimeter())

#rectangle
rectangle = Shapes("rectangle",2,4)
print('Area of Rectangle = ',rectangle.calcArea())
print('Perimeter of Rectangle = ',rectangle.calcPerimeter())

## End