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
# class User:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"
                
    
# my_user = User("Api", "v834nf")
# print(my_user.brand)
# print(my_user.model)
# print(my_user.full_name())


# 3. (Inheritance)
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def full_name(self):
#         return f"{self.brand} {self.model}"
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size


# my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
# print(my_tesla.model)
# print(my_tesla.full_name())

# 4. (Encapsulation)

# class Car1():
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model

#     def get_brand(self):
#         return self.__brand + "!"
    
#     def full_name(self):
#         return f"{self.__brand} {self.model}"
    

# my_car = Car1("Toyota", "Corolla")
# # print(my_car.__brand)    
# print(my_car.get_brand)  
# print(my_car.model)

# 5. (Polymorphism)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Disel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electirc charge"




my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")
print(my_tesla.fuel_type())
my_tata = Car("Nexon", "5gtr",)
print(my_tata.fuel_type())
        









    
       


        




