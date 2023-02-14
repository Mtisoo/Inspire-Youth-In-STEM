names=["Jamoh","collo","Anita","Shem","Levis"]
#accessing items on a list
print(names)
print(names [0])
print(names [-1])
print(names [0:3])



fruits=["banana","grapes","pomegranate","pawpaw","kiwi"]
print(fruits[0:-1])
print(fruits[3])
print("my favourite fruit is ",fruits [2].upper())
#adding two lists
vegetables=["kales","spinach","managu","carrots","cabbage"]
stationery=["pens","pencil","sharpener","scissors"]
shopping=vegetables + stationery
print(shopping)
print(shopping [5])
for vegetable in vegetables:
    print (vegetable)
for shopping in shopping:
    print (shopping)
print ("My name is name is " + names[2]+ " and my favoutrie fruit is " +fruits[3])