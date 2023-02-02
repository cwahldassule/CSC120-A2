from computer import *
class ResaleShop:

    # What attributes will it need?
    inventory = []
    profits = 0.0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory, profits):
        self.inventory = inventory
        self.profits = profits

    def update_inventory(self, action):
        if action == 'buying':
            self.inventory + self
        if action == 'selling':
            self.inventory - self
    
    def buycomp(self, name, price, OS):
        pass
    
    def refursbish(self, new_price, new_OS):
        self.updateOS(new_OS)
        self.updateprice(new_price)
        self.update_inventory("selling")



def main():
    pass

main()