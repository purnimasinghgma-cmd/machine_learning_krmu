

# item = ["apple", "banana", "orange", "apple", "mango"]
# unique_item = set()

# for item in item:
#     if item in unique_item:
#         print("duplicate: ", item )
#         break
#     unique_item.add(item)



item = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set()
for items in item:
    if items in unique_item:
        print("duplicate: ", items)
        break
    unique_item.add(items)