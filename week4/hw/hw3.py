def number_tekrar(list_number:list=['amin','amir','reza','reza',123,343,343,343]):
    count=0
    num=0

    while count<len(list_number):
            for i in list_number:
                count_list=list_number.count(i)
                if count_list>num:
                    num=count_list
                count+=1
    return f"num:{num}"
            
            
number=number_tekrar()
print(number)