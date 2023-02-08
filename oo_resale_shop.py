from computer import *
class ResaleShop:

    # What attributes will it need?
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    def buy(self, c):
        print(f"\nBuying {c.name}...")
        self.inventory.append(c)
        print("Done :)")

    def sell(self, c):
        if c in self.inventory:
            print(f"\nSelling {c.name}...")
            self.inventory.remove(c)
            print("Done :)")
        else:
            print("Error! Item not in inventory :()")

    def refurbish(self, c,new_OS):
        if c in self.inventory:
            print(f"\nRefurbishing {c.name}...")
            if c.year_made < 2000:
                c.updateprice(0)
                print(f"{c.name} is too old to sell, donation only")
            elif c.year_made < 2012:
                c.updateprice(250)
                print(f"{c.name} is 10+ years old, heavily-discounted")
            elif c.year_made < 2018:
                c.updateprice(550)
                print(f"{c.name} is 4 to 10 years old, discounted")  
            elif c.year_made < 2018:
                c.updateprice(1000)
                print(f"{c.name} is recent")
            if new_OS is not None:
                c.updateOS(new_OS)
            print("Done :)")
        else:
            print(f"\n{c.name} is not in inventory :()")            
    
    def print_store(self) -> None:
        if self.inventory == []:
            print("\nNo Inventory :()")
        else:
            print("\nInventory:")
            for i in self.inventory:
                i.print_details()

def main():
    print('--Welcome to Resale Shop!--\n')
    DoeVoid = computer("DoeVoid", "Mac Pro (Late 2013)",
                        "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, 
                        "macOS Big Sur", 2013, 1500)
    ResaleShop.buy(ResaleShop, DoeVoid)
    ResaleShop.print_store(ResaleShop)
    ResaleShop.refurbish(ResaleShop, DoeVoid,"FlipFlop2")
    ResaleShop.print_store(ResaleShop)
    ResaleShop.sell(ResaleShop, DoeVoid)
    ResaleShop.print_store(ResaleShop)


main()