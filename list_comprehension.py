a = [1, 10, 23, 24, 26, 90]

result = []

# Normal way
# print(10/3)
# print(10//3)

# # 3)10(3
# #    9
# # -------
# #     1  

# print(10%3) 

for i in a:
    if i % 2 ==0:
        result.append(i)

print(result)


# List comprehension way

new_result = [i for i in a if i % 2 == 0]
print(new_result)


b = [1, 2, 3, 4, 5] #---> [1, 4, 3, 16, 5]

# for i in b:
#     if i%2 == 0:
#         i**2
#     else:
#         i    

b_new = [i**2 if i%2==0 else i for i in b ]
print(b_new)
