# 1
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

        
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("Tata", "Nexon")
# print(my_new_car.brand)
# print(my_new_car.model)

# 2
class User:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
                
    
my_user = User("Api", "v834nf")
print(my_user.brand)
print(my_user.model)
print(my_user.full_name())


# 3(Inheritance)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
print(my_tesla.model)
print(my_tesla.full_name())


    
       


        




