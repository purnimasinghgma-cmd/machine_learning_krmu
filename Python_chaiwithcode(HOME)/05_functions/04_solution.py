# import math
 
# def circule_status(radious):
#     area = math.pi * radious ** 2
#     circumference = 2 * math.pi * radious
#     something_new = circumference + adddd(circumference)
#     return area, circumference, something_new

# def adddd(param_val):
#     return param_val + param_val
# ass = (adddd(1))
# print("nothing: ",ass)

# a, c, d = (circuoe_status(4))
# print('area:', round(c,2))
# print('circumference:', round(a, 2))
# print('something',round(d,2))

import math

def circul(radious):
    area = math.pi * radious ** 2
    circumfarence = 2 * math.pi * radious
    return (area, circumfarence)
a, b = (circul(5))
print("area: ",round(a, 2), "circumfarence: ", round(b,2))

def add(p1, p2):
    return(p1 + p2)
result = add(3, 5)
print("result: ", result)
