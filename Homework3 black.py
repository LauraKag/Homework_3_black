# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 22:53:26 2018

@author: laura
"""
#%%
#2.3 Black Belt
#Migrate the music store program we created to an OOP approach. You
#can use classes for modelling products, services, customer tier, the shopping
#cart. .
 
# Products have name and price.
# Services have price.
# Customer tier have a discount.
# Shopping cart has:
 
# a non empty list of products and services
# and a method to add new products or services
# a checkout method that receives a customer tier and calculates the price

class Products:
    
    def __init__(self,name,price):
        self.name=name
        self.price=price   

class Services:
    
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Costumertier:
    
    def __init__(self,name,discount):
        self.name=name
        self.discount=discount      
        
class Shoppingcart:
    
   def __init__(self):
       self.items = []

   def add_item(self, item):
       self.items.append(item)
        
   def checkout(self,costumertier):
       costproducts=0
       costservices=0
       if self.items==[] or self.items==["Insurance","Priority mail"] or self.items==["Priority mail", "Insurance"]:
           return "Please add something to your shoopingcart before checkout"
       else:
           for item in self.items:
               if self.items.count("Insurance") > 1 or self.items.count("Priority mail")>1:
                   return "You cant add more the one Insurance and Priority mail"
               elif isinstance(item,Products):
                   costproducts+=item.price
               elif isinstance(item,Services):
                   costservices+=item.price
                  
           finalcost=costproducts+costservices
 
           if costumertier== silver:
               costproducts=costproducts-costumertier.discount*costproducts
               finalcost=costproducts+costservices
           elif costumertier== golden:
               finalcost=costproducts+costservices
               finalcost=finalcost-costumertier.discount*finalcost
           elif costumertier==normal:
               finalcost=costproducts+costservices
           
           return "Your cost is: " + "$" + str(finalcost)
    
               
Guitar=Products("Guitar",1000)
Insurance=Services("Insurance",5)
golden=Costumertier("golden",0.05)
silver=Costumertier("silver",0.02)
normal=Costumertier("silver",1)

cart=Shoppingcart()

cart.add_item(Guitar)

cart.add_item(Insurance)       
               
cart.checkout(silver)             
               


    
    
            
            
        
        