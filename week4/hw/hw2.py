def str_vorodi(func):
    def wrapper(vorodi):
        str_vo=str(vorodi)
        result=func(str_vo)
        return result
    return wrapper

def len_kalme(func):
    def wrapper(kalame):
        func(kalame)
        len_result=len(kalame)
        return f"len:{len_result}"
    return wrapper


@str_vorodi 
@len_kalme
def vo_ro_di(kalame):
    return f'string kalme:\t{kalame}'

user=input('enter vorodi:')
result=vo_ro_di(user)
print(result)



        
