# {}
# key value pair
# indexing er sujog nie
# key gulo obossoi immumtable hote hobe

a = {'Rahim': 12, 'Karim': 14, 'Fahim': 78, 1:[1,2,3,4], 2:{3,4,5}}

print(type(a))
for i in a:
    print(i)

print("-----")    
for i in a.values():
    print(i)

print(a.keys(), a.values())

print("-------")

for k,v in a.items():
    print(f"Key name : {k}, Values {v}")

print ("-------")

a = [1, 2, 3]
b = ["Mango", "Banana", "Apple"]

#{1 : "Mango", 2: "Banana", 3: "Apple"}
c = dict(zip(b,a))
print(dict(zip(a,b)))

print(c["Mango"])

