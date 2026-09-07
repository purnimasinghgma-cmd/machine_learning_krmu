# user_name = "chiawithcode"

# def flo(): 
#     user_name = "chai"
#     print(user_name)
# flo()
# print(user_name)
 

x = 20

# def fun2(y):
#     z = x + y
#     return z
  
# result = fun2(3)
# print("result: ",result)
 
# print(fun2(3))

# def fun3():
#     global x 
#     x = 12
#     print(x)
 
# print(x)

# print(fun3())
# print(x)


# def f1():
#     x = 9
#     def f2():
#         print(x)
#     f2()
# f1()


def chaicode(num):
    def actual(x):
        return x ** num
    return actual

g = chaicode(2)
# h = actual(4) actual ake function hai par call karna ho to ham chaicode ko karenge ???
h = chaicode(3)

# print(g)
# print(h)
print(g(3))
print(h(3))

