class Student:
    name = 'default'
    age = '18'
    language = 'default'

    def get_age(self,name,age,language):
        self.name = name
        self.age = age
        self.language = language

Steve = Student()
Steve.get_age("Steven Schultz", 23, "English")
print(f'Меня зовут {Steve.name},мне {Steve.age} лет , язык {Steve.language}')

Johnny = Student()
Johnny.get_age("Jonathan Rosenberg", 24, "Biology")
print(f'Меня зовут {Johnny.name},мне {Johnny.age} лет , язык {Johnny.language}')

Penny = Student()
Penny.get_age( "Penelope Meramveliotakis", 21, "Physics")
print(f'Меня зовут {Penny.name},мне {Penny.age} лет , язык {Penny.language}')