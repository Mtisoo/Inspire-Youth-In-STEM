    #write a program to list all the odd numbers from 1-100,even,prime numbers
#write a program to write arithmetic progresion of numbers from 1-100
even_nums = [6]

for num in range(20):
    if(num % 2 == 0):
        even_nums.append(num)

for i in even_nums:
    print(even_nums[i])