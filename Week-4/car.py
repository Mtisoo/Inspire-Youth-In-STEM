class car:
    def __init__(self,model,make,year,engine_capacity):
        self.model = model
        self.make = make
        self.year = year
        self.engine_capacity = engine_capacity

    def get_model(self):
        return self.model

    def get_make(self):
        return self.make

    def get_year(self):
        return self.year

    def get_engine_capacity(self):
        return self.engine_capacity

#setters
def set_model(self,model):
    self.model = model

def set_make(self,model):
    self.model = model

def set_year(self,year):
    self.year = year_of_man



car_1 = car("Passo", "Toyota", 2018, 1300)
car_2 = car("Hilux", "Toyota", 2008, 2300)
car_3 = car("Outbsck", "Subaru", 2022, 1300)


print(car_1.get_make())
print(car_1.get_year())
print(car_1.get_engine_capacity())


print(car_3.get_make())
print(car_3.get_year())
print(car_3.get_engine_capacity())

print(car_2.get_make())
print(car_2.get_year())
print(car_2.get_engine_capacity())