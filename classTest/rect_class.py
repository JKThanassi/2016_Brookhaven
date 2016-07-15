import matplotlib.pyplot as plt

class ShapeCoords:
    def __init__(self, point1, point2, plt):
        """
        This is the constructor for the shapeCoords object
        :param point1: a list containing two variables in the format of [x, y] which represents a point
        :type point1: list
        :param point2: a list containing two variables in the format of [x, y] which represents a point
        :type point2: list
        :param plt: a pyplot object
        :type plt: matplotlib.pyplot
        """
        self.point1 = point1
        self.point2 = point2
        self.plt = plt

    def point_dist(self, axisName):
        """
        finds the distance between two points on the same axis
        :param axisName: input should be "x" or "y"
        :type axisName: str
        :return: distance between two points
        """
        assert type(axisName) is str
        assert axisName.lower() == 'x' or axisName.lower() == 'y'

        point_dist = 0

        if axisName.lower() == 'x':
            point_dist = self.point2[1] - self.point1[1]
        else:
            point_dist = self.point2[0] - self.point1[0]

        return point_dist

    def find_perim(self):
        """
        This function finds the perimeter of the shape defined by the two points
        :return: perimeter
        """

        y_axis_dist = self.point_dist('y')
        x_axis_dist = self.point_dist('x')

        return abs((x_axis_dist + y_axis_dist) * 2)

    def is_square(self):
        """
        checks if the defined shape is a square
        :return: True if square, False otherwise
        """

        y_axis_dist = self.point_dist('y')
        x_axis_dist = self.point_dist('x')

        return y_axis_dist == x_axis_dist

    def draw_shape(self):
        self.plt.hlines(self.point1[1], self.point1[0], self.point2[0])
        self.plt.hlines(self.point2[1], self.point1[0], self.point2[0])
        self.plt.vlines(self.point1[0], self.point1[1], self.point2[1])
        self.plt.vlines(self.point2[0], self.point1[1], self.point2[1])
        self.plt.show()



def main():
    class_test = ShapeCoords([0, 92], [30, 30], plt)

    print("perimeter: " + str(class_test.find_perim()))
    print("is it a square? " + str(class_test.is_square()))
    class_test.draw_shape()


main()
