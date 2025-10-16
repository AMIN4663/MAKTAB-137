class Person:
    def __init__(self,name:str,age:int,address:str):
        self.name=name
        self.age=age
        self.address=address
    
    def introduction(self):
        print(f'hi i am {self.name}:{self.age} years old')
    
    def change_address(self,new_addres):
        self.address=new_addres

