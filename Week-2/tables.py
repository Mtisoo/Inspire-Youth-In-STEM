#import module
from tabulate import tabulate
#assign number
mydata = [
    ["Nikhil","Dehli"],
    ["Ravi","Kanpur"],
    ["Manish",
    "Ahmedabad"],
    ["Prince", "Bangalore"]
]
#create header
head=["Name","City"]
#display table
print(tabilate(mydata, headers=head,tablefmt="grid"))