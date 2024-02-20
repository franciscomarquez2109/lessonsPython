class Person(object):
    def __init__(self) -> object:
        self.info = {
            'name': 'Francisco',
            'age': 30,
            'country': 'Venezuela',
            'email': 'francisco@gmail.com'
        }
    
    def __getitem__(self,i):
        return self.info[i]
    

person = Person()
print(person['country'])
