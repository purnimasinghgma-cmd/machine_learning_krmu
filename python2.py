# # class Demo:
# #     def __init__(self, a, b):
# #         self.a = a
# #         self.b = b
# #     def sums(self):
# #         return self.a + self.b
# # ob = Demo(12, 6) 
# # print(ob.sums()) 


# # class Demo:
# #     def __init__ (self):
# #         pass
# #     def add(self, a, b):
# #         print("The sum is", a+b)
# # ob = Demo()
# # (ob.add(2,5))

# class Numbers:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def large(self):
#         if self.a > self.b and self.a > self.c:
#             return self.a
#         elif self.b > self.a and self.b > self.c:
#             return self.b
#         else:
#             return self.c

# ob = Numbers(12, 6, 20)

# print(ob.large())

# Linear Regression
from colorsys import hsv_to_rgb


class MylinearReg: 
    def __int__(self, lr = 0.1, epoch = 1000):  #(lr = learing rate(0.1)(kitni jaldi kaam hora hai)) #(epoch = repated time work (kitni bar repet hora hai))
        self.lr = lr
        self.epoch = epoch
        self.m = 0
        self.c = 0
    def fit(self, x , y):     # (x= feature and y = leable out come)
        for _ in range (self.epoch):
            y_pred = self.m * x + self.c
            error = y-y_pred
            dm = (-2/n) * sum(x * error)
            dc = (-2/n) * sum (error)