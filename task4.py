class Person:
    name = 'default'
    lastname = 'default'
    age = '18'

    def get_age(self,name,lastname,age):
        self.name = name
        self.lastname = lastname
        self.age = age

alex = Person()
alex.get_age('Алекс','Том',21)
print(f'Меня зовут {alex.name},{alex.lastname},мне {alex.age} лет')

aito = Person()
aito.get_age('Aito','Bak',18)
print(f'Меня зовут {aito.name},{aito.lastname},мне {aito.age} лет')
