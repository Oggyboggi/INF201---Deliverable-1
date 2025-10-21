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
        
    def area(self):
        return self._width * self._height
    

if __name__ == "__main__":
    