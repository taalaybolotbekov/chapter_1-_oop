class Employee:
    name = 'name'
    lastname = 'lastname'
    position = 'pos'
    salary = 'sal'

    def get_info(self,name,lastname,position,salary):
        self.name = name
        self.lastname = lastname
        self.position = position
        self.salary = salary

taalay = Employee()
taalay.get_info(name = input('имя: '),lastname = input('фамилия: '),position = input('должность: '),salary = int(input('зарплата: ')))
print(taalay.name,taalay.lastname,'работает на должности ',taalay.position,'и получает зарплату в размере ',taalay.salary,'сом')
