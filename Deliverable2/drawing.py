"""""
Created by Iver Rannug Fossan and Oscar Wiersdalen Thunold

Task 1
"""""

# Class pulled from lecture notebook 8
class Rectangle:
    def __init__(self, lower_left, upper_right):
        self._ll = lower_left
        self._width = upper_right[0] - lower_left[0]
        self._height = upper_right[1] - lower_left[1]

    # Method to calculate area of the rectangle
    def area(self):
        return self._width * self._height
    
    # Method to return information about the rectangle
    def info(self):
        return f"Rectangle: lower left {self._ll}, upper right {self._ll[0] + self._width, self._ll[1] + self._height}"
    
if __name__ == "__main__":
    print(Rectangle((1,2), (4,6)).info()) # Prints: Rectangle: lower left (1, 2), upper right (4, 6)