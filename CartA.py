
from random import random,randint,randrange
class EKart:
    Products={'iphone':5,'iMac':3,'iWatch':2,'iPad':4}
    print(Products)
    Price={'iphone':800,'iMac':2400,'iWatch':3000,'iPad':3500}
    print(Price)
    def __init__(self,name,Add,Email,Balance):
        if Balance <10000:
            raise ValueError('Minimum Amount Should Be 10000')
        else:
            self.name=name
            self.Add=Add
            self.Email=Email
            self.Cart=[]
            self.Balance=Balance
    def Add_Balance(self,Amount):
        if Amount>1000:
            self.Balance+=Amount
        else:
            raise ValueError('Amount Should Be Greater Than (999)')
    def add(self,item):
        if EKart.Products[item]>0:
            self.Cart.append(item)
            EKart.Products[item]-=1
        else:
            print('Out Of Stock')
    def remove(self,Item):
        if Item in self.Cart:
            self.Cart.remove(Item)
            EKart.Products[Item]+=1
        else:
            raise ValueError('Item is not In Cart')
    def Checkout(self):
        Total_Amount=0
        for Item in self.Cart:
            if Item in EKart.Price:
                Total_Amount+=EKart.Price[Item]
        if Total_Amount>self.Balance:
            raise ValueError('You Have Infussient Balance')
        elif len(self.Cart)<=0:
            raise ValueError('Your Cart Is Empty')
        else:
            print('*'*10)
            print(f'Total Amount Of Your Cart Is: {Total_Amount}')
            print(f'Delivery Charges Of Yours Is: {Total_Amount/100*2.5}')
            print('*'*20)
            print(f'Your Total Amount Is: {Total_Amount+Total_Amount/100*2.5}') 
            print(f'Your Payment Sucessfull ')
            print(f'Your Item Delivered In {randint(5,7)} Days')           
            self.Balance=self.Balance-(Total_Amount+Total_Amount/100*2.5)
            print(self.Balance)
                


class EKartSeller():
    Products={'iphone':5,'iMac':3,'iWatch':2,'iPad':4}
    Price={'iphone':800,'iMac':2400,'iWatch':3000,'iPad':3500}
    def __init__(self,name,Add,Email):
        self.name=name
        self.Add=Add
        self.Email=Email
    def Add_Products(self,Product,Pr,No):
        self.Product=Product
        self.Price=Pr
        self.No=No
        if Product not in EKartSeller.Products:
            EKartSeller.Products[self.Product]=self.No
            EKartSeller.Price[self.Product]=self.Price
        else:
            EKartSeller.Products[self.Product]=EKartSeller.Products[self.Product]+self.No
    def Change_Price(self,Product,New_Price):
        self.Product=Product
        self.New_Price=New_Price
        if Product not in EKartSeller.Products:
            raise ValueError("Product Doesn't Present")
        else:
            EKartSeller.Price[self.Product]=New_Price
    def Remove_Product(self,Product):
        if Product in EKartSeller.Products:
          EKartSeller.Products.pop(Product)
          EKartSeller.Price.pop(Product)
        else:
            raise ValueError("Product Doesn't Present") 
    def View_Prduct(self):
        print(EKartSeller.Products,EKartSeller.Price)
        
        
class EKartSellerBuy(EKart,EKartSeller):
    def __init__(self,name,Add,Email,Balance="0"):
        self.name=name
        self.Add=Add
        self.Email=Email
        self.Cart=[]
        self.Balance=Balance
        
        
class EKartMembership(EKart):
    def __init__(self,name,Add,Email,Balance):
        if Balance<5000:
            raise ValueError("Minimum Amount Should Be 5000")
        else:
            self.name=name
            self.Add=Add
            self.Email=Email
            self.Cart=[]
            self.Balance=Balance
    def Checkout(self):
        Total_Amount=0
        for Item in self.Cart:
            if Item in EKart.Price:
                Total_Amount+=EKart.Price[Item]
        if Total_Amount>self.Balance:
            raise ValueError('You Have Infussient Balance')
        elif len(self.Cart)<=0:
            raise ValueError('Your Cart Is Empty')
        else:
            print('*'*10)
            print(f'Total Amount Of Your Cart Is: {Total_Amount}')
            print(f'Delivery Charges Of Yours Is: {Total_Amount/100}')
            print('*'*20)
            print(f'Your Total Amount Is: {Total_Amount+Total_Amount/100}')
            print('Transaction Sucessful')


class EKartVip(EKartMembership):
    def __init__(self,name,Add,Email,Balance):
        self.name=name
        self.Add=Add
        self.Email=Email
        self.Cart=[]
        self.Balance=Balance
    def Checkout(self):
        Total_Amount=0
        for Item in self.Cart:
            if Item in EKart.Price:
                Total_Amount+=EKart.Price[Item]
        if Total_Amount>self.Balance:
            raise ValueError('You Have Infussient Balance')
        elif len(self.Cart)<=0:
            raise ValueError('Your Cart Is Empty')
        else:
            print('*'*10)
            print(f'Total Amount Of Your Cart Is: {Total_Amount}')
            print(f'Delivery Charges Of Yours Is: {0}')
            print('*'*20)
            print(f'Your Total Amount Is: {Total_Amount}')
            print('Transaction Sucessful')   
    
    
        
            
            
        
c7=EKartMembership('jhsi','hla','agjviahva@gmail.com',5000)
c8=EKartVip('bdks','kjhe','bkcsk@gmail.com',3000)
c8.add('iphone')
c8.Checkout()        
c6=EKartSellerBuy('sj','Ku','gvka@gmail.com')
print(c6.__dict__)   
c5=EKartSeller('jkd','Bombay','efhgf3435@gmail.com')
c5.Add_Products('Power Rangers',4000,4)
print(EKartSeller.Products,EKartSeller.Price)
c5.Change_Price('iphone',40000) 
print(EKartSeller.Products,EKartSeller.Price)
c5.Change_Price('iMac',40000)
c5.Remove_Product('Power Rangers')
print(EKartSeller.Products,EKartSeller.Price)
c1=EKart('Steve','Kalyan','575@gmail.com',10000)
c3=EKart('Svegh','Rhane','efhg5@gmail.com',10000)
c2=EKart('Ryhi','Pune','57wrd5@gmail.com',20000)
c1.add("iphone")
c1.add('iMac')
c1.add('iWatch')
c2.add('iWatch')
c2.add('iPad')
print(c1.Cart)
print(c2.Cart)
print(EKart.Products)
c2.add('iWatch')
c2.remove('iWatch')
print(c2.Cart)
print(EKart.Products)
