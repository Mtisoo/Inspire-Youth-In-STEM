# Advanced datatypes

#mutable vs immutable

#mutable are datatypes that can change /edited during program life cycle.
#immutable --. datatypes that canoot be edited during progamming

# 1) list(Mutable)

Friends = ["shem","Levis", "Anita" ,"Hannah"]
# or friends = [] for empty lists
#add --> addpend(), extend()
# to remove --> pop()
students = ["Marie","Agnes"]
Friends.extend(students)
Friends.append("James")
Friends.sort()
Friends.reverse()
# 2)Tuples (immutable)
# Type of list that are immutable

stationeries= ("pens","ink","sharpener")
for stationery in stationeries:
    print(stationery)

numbers = (1,2,3,4,5,6,7,8,9,10)

# 3) Dictionaries aka dict

# uses key and value pair
student = {"name" : "Bob", "age" : 24, "Gender" : "male", "height" : "is_tall"}

print(student["name"])
print(student["Gender"])
print(student["age"])
print(student["height"])
# 4) Sets 