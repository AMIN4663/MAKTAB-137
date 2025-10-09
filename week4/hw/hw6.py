def comparison_str(string_1,string_2):
    count=0
    for s1,s2 in zip(string_1,string_2):
            if s1 == s2:
                count+=1
    return f'comparison_str:{count}'

result=comparison_str("aBcD","ABcdd")
print(result)