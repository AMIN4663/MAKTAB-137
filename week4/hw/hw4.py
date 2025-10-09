def nested_sum(lst:list=[1,[2,3],[4,[5]]]):
    counter=0
    for i in lst:
        if type(i) is list:
            counter+=nested_sum(i)
        else:
            counter+=i
    return counter





nested_sum()