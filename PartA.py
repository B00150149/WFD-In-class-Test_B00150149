#A2: Class with provided initialisation attributes
class Phone:
    def __init__(self, brand, model, year, price, colour):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour

    #A3: Method to print all  initialisation attributes
    def show_phone_details(self):
        print("Brand", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Price:", self.price)
        print("Colour:", self.colour)


    #A4: Method inside the class to update attribute
    def updateBrand(self, new_brand):
            self.brand = new_brand
        
    def updateModel(self, new_model):
            self.model = new_model
       
    def updateYear(self, new_year):
            self.year = new_year

    def updatePrice(self, new_price):
            self.price = new_price
        
    def updateColour(self, new_colour):
            self.colour = new_colour
        

#A5 
#Overrides innit method
class SmartPhone(Phone):
    def __init__(self, brand, model, year, price, colour, os, storage):
        super().__init__(brand, model, year, price, colour)
        self.os = os
        self.storage = storage

    #A6: Method to print all attributes 
    def show_phone_details(self):
        super().show_phone_details()
        print(f"OperatingS System: {self.os}, Storage: {self.storage}")

    #A7: Methods to update extra attributes
    def updateOs(self, new_os):
            self.os = new_os


    def updateStorage(self, new_storage):
            self.storage = new_storage

#To comapre the attributes of since they have same attributes
    def __eq__(self, other):
        return (
            isinstance(other, SmartPhone) and
            super().__eq__(other) and
            self.os == other.os and
            self.storage == other.storage
        )  

if __name__ == "__main__":
    #Instance of Phone
    phone = Phone("Apple", "iPhone 13", 2021, 999, "Black")
    phone.show_phone_details()
    
    print(" ")
    #Instance of SmartPhone
    smartphone = SmartPhone("Samsung", "Galaxy S21", 2021, 799, "Phantom Gray", "Android", 128)
    smartphone.show_phone_details()
