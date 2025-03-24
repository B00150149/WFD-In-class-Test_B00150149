import unittest

# Assuming Phone and SmartPhone classes are defined in PartA.py
from PartA import Phone, SmartPhone

class TestPhoneMethods(unittest.TestCase):
    def setUp(self):
    #Initialising the object
        self.phone = Phone("Apple", "iPhone 13", 2021, 999, "Black")
        self.smartphone = SmartPhone("Samsung", "Galaxy S21", 2021, 799, "Phantom Gray", "Android", 128)

    #B2: Test if an object is an instance of a class
    def testInstanceOfClass(self):
        self.assertIsInstance(self.phone, Phone)
        self.assertIsInstance(self.smartphone, SmartPhone)

    #B3: Test if an object is not an instance of a class
    def testNotInstanceOfClass(self):
        self.assertNotIsInstance(self.phone, SmartPhone)
        #self.assertNotIsInstance(self.smartphone, Phone)
        self.assertEqual(type(self.smartphone), SmartPhone)

    #B4: If two objects are identical
    def testObjectsIdentical(self):
        anotherPhone = Phone("Apple", "iPhone 13", 2021, 999, "Black")
        self.assertEqual(self.phone, anotherPhone)
     

    #B5: Unit tests to test if update methods work correctly
    def testUpdateMethods(self):
        self.phone.updateBrand("Oppo")
        self.assertEqual(self.phone.brand, "Oppo")

        self.smartphone.updateOs("iOS")
        self.assertEqual(self.smartphone.os, "iOS")

#B6: Main function to run the tests of tasks B2 to B5
def main():
    unittest.main()

if __name__ == "__main__":
    main()
