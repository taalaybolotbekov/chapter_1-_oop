class Child:
    name = 'default'
    apples = 0
    def names(self,name,apples):
        self.name = name
        self.apples = apples 

taalay = Child()
taalay.names('Алекс', 8)
aito = Child()
aito.names('Аманда',9)
print('Количество яблок: ',aito.apples+taalay.apples,'\nИмена: ',taalay.name,aito.name)
