class Human:
    def general_characteristic(self):
        print("Human is helpful")

class Boys(Human):
    def __init__(self):
        self.section = 'A'
        self.color = 'Black'
        #self.general_characteristic()
        #print(f'Boys are {self.color}\nThey are in section {self.section}\n')

    def characteristics(self):
       print("Boys are Clumsy")
    
    def football(self):
        print("Boys Love Football")

class Girls(Human):
    def __init__(self):
        self.section = 'B'
        self.color = 'White'
        #self.general_characteristic()
        #print(f'Girls are {self.color}\nThey are in section {self.section}\n')

    def characteristics(self):
       print("Girlss are Organized")
    
    def gardening(self):
        print("Girls Love Gradening")

class ThirdGender(Boys,Girls):
    def begging(self):
        print("We can not but beg")
        

#Multiple Inheritance
jorina = ThirdGender()
jorina.begging()
jorina.football()
jorina.gardening()

