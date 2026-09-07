# n = 6
# count_even = 0
# for i in range (1,n+1):
#     if i % 2 == 0:
#         count_even += 1
# print("count of even number is :", count_even)




n = [1, 2, 4, 5, 6, 7]
sum_even_num = 0
for i in n:
    if i % 2 == 0:
        sum_even_num = sum_even_num + 1
print(sum_even_num)

n = [1, 2, 4, 5, 6, 7]
sum_even_num = 0
for i in n:
    if i % 2 == 0:
        sum_even_num += i
print(sum_even_num)