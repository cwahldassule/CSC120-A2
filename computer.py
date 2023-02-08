class computer:
    name: str
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    def __init__(self, name, descrip, pro_type, hard_drive_cap, memory, OpSy, year_made, price) -> None:
        self.name = name
        self.description = descrip
        self.processor_type = pro_type
        self.hard_drive_capacity = hard_drive_cap
        self.memory = memory
        self.operating_system = OpSy
        self.year_made = year_made
        self.price = price
    
    def updateprice(self, amt) -> bool:
        self.price = amt
        return True
    
    def updateOS(self, newOS) -> bool:
        self.operating_system = newOS
        return True
    
    def print_details(self) -> None:
        print("\nDescription:",self.description)
        print("Processor:",self.processor_type)
        print( "Hard Drive:",self.hard_drive_capacity)
        print("Memory:", self.memory)
        print("Operating System:", self.operating_system )
        print("Year Made:",self.year_made)
        print("Price:", self.price)

#def main():
#    DoeVoid = computer("DoeVoid", "Mac Pro (Late 2013)",
#                        "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, 
#                        "macOS Big Sur", 2013, 1500)
#    DoeVoid.print_details()
#    DoeVoid.updateprice(1700)
#    DoeVoid.print_details()
#    DoeVoid.updateOS("FlipFlop2")
#    DoeVoid.print_details()
#main()