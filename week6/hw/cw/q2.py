from typing import Any


class Config:
    new_istance=None
    def __new__(cls,*arg,**kwarg):
        if cls.new_istance is None:
            cls.new_istance=object.__new__(cls)
            return cls.new_istance
    def __init__(self,theme="dark",language="english"):
        self.theme=theme
        self.language=language
        print("ok")
    

c1=Config()
c2=Config()

class File:
    def __new__(cls, *args, **kwargs):
        print("start")
        self = object.__new__(cls)
        return self
    
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        try:
            self.file = open(self.file_name, self.mode)
            print(f"file {self.file_name} opened succesfully.")
        except FileNotFoundError:
            print(f"file {self.file_name} not found.")
    
    def __del__(self):
        if self.file:
            self.file.close()
            print(f"file was delete from ram.")


class CustomDict(dict):
    def __setitem__(self,key,value):
        if isinstance(value,int):
            return super().__setitem__(key,value*2)
        return super().__setitem__(key,value)
    def __str__(self)
    
    
   



dct1=CustomDict({"ALI":2})
dct1["s"]=4
print(dct1)




    

    

        