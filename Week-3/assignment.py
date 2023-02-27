# create an empty list of favourite mucisians
# add using for loop 5 new mucisians and copy the list to a new list called select
# sort the list pop out two selects from the list
# count the remaining selects from the list

mucisians = []

for x in range(5):
    y = input("Enter a mucicians name : ")
    mucisians.append(y)

print(mucisians)
celebrities = mucisians.copy()
print(celebrities)
celebrities.sort()
print(celebrities)
celebrities.pop()
celebrities.pop()
print(celebrities)
print(len(celebrities))



