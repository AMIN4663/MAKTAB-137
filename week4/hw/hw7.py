def sum_counts(number_1,number_2,/):
    return f'{number_1}+{number_2}:{number_1+number_2}'

def deta(*,name,age):
    return f'name:{name}\tage:{age}'


def calut(num1,num2,/,*,re):
    if re=="/":
        return f'{num1}/{num2}={num1/num2}'
    elif re=="*":
        return f'{num1}*{num2}={num1*num2}'
    elif re=="+":
        return f'{num1}+{num2}={num1+num2}'
    else:
        return f'{num1}-{num2}={num1-num2}'


sum=sum_counts(3,4)
print(sum)

deta_user=deta(name="ali",age=70)
print(deta_user)

rusult=calut(3,3,re='+')
print(rusult)