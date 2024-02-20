class Person(object):
    name = ''
    age = ''

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def viewInfo(self):
        print(self.name,self.age)
    
#instancias
newClass = Person('Francisco',30)
newClass.viewInfo()


