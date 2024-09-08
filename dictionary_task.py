# 1) find and display in the console all keys whose length does not match the value of this key
# 2) delete pairs of values from the dictionary where the key length and the value of this key do not match
# 3) make a new list from the deleted words
# 4) output the modified dictionary and the list of deleted words to the console
# 4) make a new list from the keys obtained in task 1
# 5. Delete these keys and their values from the dictionary


dict2 = {
    'apple': 5,
    'banana': 7,
    'orange': 6,
    'watermelon': 10,
    'grape': 5,
    'kiwi': 8,
    'mandarine': 5,
    'strawberry': 9
}

new_list = []
# output all keys that do not match the value with length
for i in dict2:
    if len(i) != dict2[i]:
        print(i)
        dict2[i] = len(i)
        new_list.append(i) #deleted words into a new list
print(f'{new_list}\n')
# remove from the dictionary pairs of values where the length does not match the value 
for i in new_list:
    del dict2[i]

for i in dict2:
    print(f"{i}: {dict2[i]}")