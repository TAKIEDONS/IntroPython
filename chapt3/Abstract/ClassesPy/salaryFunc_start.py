# TODO: Classes are defined using the class keyword

class Salary:
    def __init__(self, sal_id, empname, position, sal_bal):
          self._sal_id = sal_id
          self._empname= empname
          self._position= position
          self._sal_bal= sal_bal

# Using getter on python class

    @property
    def title(self):
        return self._sal_id
    @property
    def title(self):
        return self._empname
    @property
    def title(self):
        return self._position
    @property
    def title(self):
        return self._sal_bal
    
# using setter on python class
    @title.setter
    def title(self, value):
        self._sal_id= value

    @title.setter
    def title(self, value):
        self._empname= value

    @title.setter
    def title(self, value):
        self._position= value

    @title.setter
    def title(self, value):
        self._sal_bal= value

    # TODO: create an instance of the class
sal_1 = Salary("001", "Takalani", "Junior Software Developer", 35.900)

print(sal_1._sal_id, sal_1._empname)