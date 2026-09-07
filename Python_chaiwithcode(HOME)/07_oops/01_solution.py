# encapsulation privet karke usko getter method se use karna
# inheriance 
# polymorphism
# static method (self ki jarurat matlab object nahi chahie  direct class se assess hai (decorectors kehete hai )
# property decoretor (jab  change nahi karna ho )
# isinstance function
# mutipul inheritance

class Car:
    total_car = 0
    def __init__(self, brand, model):
       self.__brand = brand
       self.__model = model
       Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
            return ("petrol", "diesel")
    
    @staticmethod
    def general_descripstion():
        return "car are means of transport"
     
    @property
    def model(self):
        return(self.__model)  

    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return ("electric charge")

# my_tesla = ElectricCar("Tesla", "Model s", "90kwh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

 
# # print(my_tesla.full_name())
# # print(my_tesla.__brand)
# # print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

# safari = Car("Tata", "Safari")
# safaritwo = Car("tata", "nexon") 
# print(safari.fuel_type())
# print(Car.total_car)
# # safari.model = "city"
# print(safari.model)

# # print(safari.general_descripstion()) 
# # print(Car.general_descripstion()) 
# # print(safari.model) 

# # my_car = Car("Toyota", "Corolla")
# # # print(my_car.brand)
# # print(my_car.get_brand())
# # # print(my_car.full_name())

# # my_new_car = Car("Tata", "safari")
# # print(my_new_car.model)

class Battery:
    def battry_info(self):
        return("this is battry")

class Engine:
    def engine_info(self):
        return("info of engine")   

class ElectricCartwo(Battery, Engine, Car):
    pass

my_car = ElectricCartwo("tesla","model s")
print(my_car.engine_info())
print(my_car.battry_info())