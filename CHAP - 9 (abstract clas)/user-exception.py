class TeaHotexception(Exception):
    def __init(self, arg):
        self.msg = arg

class TeaColdexception(Exception):
    def __init(self, arg):
        self.msg = arg


class Tea:
    def __init(self, temperature):
        self.__temperature = temperature
    
    def drink_tea(self):
        if self.__temperature > 85:
            raise TeaHotexception raise TeaException("Tea is HOT")
        elif self.__temperature < 65:
             raise TeaException("Tea is too old")
        else:
            print("Tea OK to Drink")
    