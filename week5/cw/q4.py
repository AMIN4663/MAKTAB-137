class Smartphone:
    def __init__(self,brand:str,model:str,battery:int,storage:int,camera_megapixels:str,os:str):
        self.brand=brand
        self.model=model
        self.battery=battery
        self.storage=storage
        self.camera_megapixels=camera_megapixels
        self.os=os
    
    def show_info(self):
        print(f'brand:{self.brand}\nmodel:{self.model}\nstorge:{self.storage}\nos:{self.os}')
    
    def make_call(self,number):
        print(f"{number} tamas ba shoma bargrar shod")
    
    def check_battery(self):
        if self.battery>=80:
            print(f"{self.battery}:not charge")
        elif self.battery<=15:
            print (f'{self.battery}:you need charge')
        else:
            print('normal')
        
    def install_app(self,app_name:str,new_app:list):
        if app_name not in new_app:
            new_app.append(app_name)
            print(f'{app_name}:instal app...')
        else:
            print(f'{app_name}:instaled app')
            
            
    def take_photo(self):
        if self.camera_megapixels>50:
            print(f"is good take photo")
        elif self.camera_megapixels<30:
            print("not take photo")
        else:
            print('allow take photo')


        
    