age = 16
gender = "male"

if (age < 18):
    print("Umechimba bro")
else:
    print("Get an ID")

#compound /multiple conditions
if((age > 30) & (gender =="male")):
    print("You qualify for Hustler fund")
else:
    print("You don't qualify")

fav_colour="gray"
if((fav_colour == "gray") | (age <= 20)):
    print("You won't receive a present")
else:
    print("Happy birthday")


