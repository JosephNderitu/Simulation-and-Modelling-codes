# -*- coding: utf-8 -*-
class Automobile:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    def get_make(self): return self.__make
    def get_model(self): return self.__model
    def get_mileage(self): return self.__mileage
    def get_price(self): return self.__price

class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        super().__init__(make, model, mileage, price)
        self.__doors = doors
    def get_doors(self): return self.__doors

class Truck(Automobile):
    def __init__(self, make, model, mileage, price, drive_type):
        super().__init__(make, model, mileage, price)
        self.__drive_type = drive_type
    def get_drive_type(self): return self.__drive_type

class SUV(Automobile):
    def __init__(self, make, model, mileage, price, pass_cap):
        super().__init__(make, model, mileage, price)
        self.__pass_cap = pass_cap
    def get_pass_cap(self): return self.__pass_cap
