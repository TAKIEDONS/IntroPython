from abc import ABC, abstractmethod

class jsonify(ABC):
    @abstractmethod
    def to_json(self):
        pass


class graphicshape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_area(self):
        pass

# class circle (graphicshape):
#         def __init__(self, radius):
#             self._radius = radius
        
#         def calc_area(self):
#             return 3.14  * (self._radius **2)


class square(graphicshape, jsonify):
    def __init__(self, side):
         self._side = side

    def calc_area(self):
            return self._side * self._side

    def to_json(self):
        return f"{{ \"square\" : {str(self.calc_area())} }}"

# g = graphicshape()

# c= circle(10)
# print(c.calc_area())
s = square(12)
print("Square to Area is", s.calc_area())
print("Square to JSON is", s.to_json())