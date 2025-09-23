#CREATE A CLASS CALED ORDER WHICH STORES ITEM & ITS PRICE.
#USE DUNDER FUNCTION __GT__() TO CONVEY THAT:
#     ORDER1>ORDER2 IF PRICE OF ORDER1>PRICE OF ORDER2

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,ord2):
        return self.price > ord2.price   
        
ord1=Order("chips",20)
ord2=Order("tea",15)
print(ord1>ord2)