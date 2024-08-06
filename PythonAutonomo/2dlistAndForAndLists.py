mylist = [
    [2,4,8],
    [3,6,12],
    [4,8,16]
]

print(mylist[2][1])
for lists in mylist:
    for row in lists:
        print(row)


mydict = {
    "name": "Fran",
    "age": 19,
    "IsStrong?": False,
    "lista": [1,2,3,4,5]

}

print(mydict["name"])
print(mydict["IsStrong?"])
print(mydict["lista"][3])

numeros = [1, 2, 3, 40, 50, 70]

for i in numeros :
    print(i)
    if i == 50:
        break

e = 0
for e in range(4, 10):
    print(e)