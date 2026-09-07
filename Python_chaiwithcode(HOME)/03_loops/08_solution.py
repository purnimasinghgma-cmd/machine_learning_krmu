
# number = 7
# is_prime = True

# if number > 1:
#     for i in  range (2,number):
#         if number % i == 0:
#             is_prime = False
#             break
#     print(is_prime)
    


number = 7
# is_prime = True  (it is writtrn because is_prime alway true but when the if condition satisfy it will flase otherwise is_prime "True")
if number > 1:
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
            break
    print(is_prime)
     

