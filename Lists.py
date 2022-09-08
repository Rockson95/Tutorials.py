# names =['Rockson','John','Yaw']
# print(names)


class students:
    def __abs__(self,name,contacts):
        self.name = name
        self.contacts = contacts

    def getdata(self):
         print('Accepting data from all source')
         self.name = input('Enter name')
         self.contacts = input('Enter contacts')

    def putdata(self):
        print('The name is',+self.name, 'This is the',+self.contacts)

Rockson = students()
Rockson.getdata()
Rockson.putdata()
