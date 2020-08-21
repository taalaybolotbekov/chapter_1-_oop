class Shop:
    name = 'name'
    is_open = 'is_open'
    products_list = 'products_list'
    buy = 'buy'
    def add_products(self,name,is_open,products_list):
        self.name = name
        self.is_open = is_open
        self.products_list = products_list
    # def is_avaible(self,product):
    #     self.product = product
    def buy_product(self,buy):
        self.buy = buy

a = Shop()
a.add_products(name=input('name:'),is_open=True,products_list=int(input()))
# a.buy_product(buy = int(input('сколько хотите купить? ')))
# a.is_avaible(product(products_list))

if a.products_list > 0:
  a.is_open = True 
#   buy - products_list
else:
  a.is_open = False
# print('buy_product: ',a.buy_product)
# print('is_avaible:',a.is_avaible)
print(f'Название магазина {a.name},и {a.is_open}')

