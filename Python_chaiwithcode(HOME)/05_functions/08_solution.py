def print_kwarge(**kwarge):
    for key, value in kwarge.items():
        print(f"{key}: {value}")


print_kwarge(name = "sima", power = "smart")
print_kwarge(name = "sima")
print_kwarge(name = "sima", power = "smart", enemy = "angar")  

# # def print_kwarge(key, value):
#     print("key:", key, "value:", value)

# print_kwarge("sima", "asd")