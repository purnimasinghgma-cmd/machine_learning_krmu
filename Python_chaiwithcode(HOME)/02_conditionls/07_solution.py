# order_size = "Medium"
# extra_shot = True   

# if order_size == "Medium" and extra_shot:
#     coffee = order_size + " with extra shot of expresso "
# else:
#     coffee = order_size + " coffee " 
# print("coffee:", coffee)


order_size = "small"
extra_shot = True

if order_size == "small" and extra_shot:
    coffee = order_size + " with extra_shot of expresso "
else:
    coffee = order_size + "coffee"
print("coffee", coffee)