class students:
    def __abs__(self,name,contact,gender,level):
        self.name = name
        self.contact = contact
        self.gender = gender
        self.level = level

    def getdata(self):
        print("Accepting data from all sources ")
        self.name = input("Please enter your name ")
        self.contact = input("Please enter your contact ")
        self.gender = input("Please enter gender ")
        self.level = input("Which level are you? ")

    def putdata(self):
        print('This is:'+self.name,'this is your contact:'+self.contact,'you are:'+self.gender,'you are also level: '+self.level, 'student')

class scincestudent(students):
    def __abs__(self,age):
        self.age = age

    def science(self):
        print("I am a science student")

Rockson = scincestudent()
Rockson.science()
Rockson.getdata()
Rockson.putdata()
