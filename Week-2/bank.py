#Write a program that calculates 16% tax ranging btwn 10k - 150k

#19%tax income if btwn 150k - 300k
#30%tax if income is above 300k
#5% tax if income is less than 10k

#print gross income and net income
gross_income=int(input("Enter your gross income:"))
if (gross_income <= 10000):
    net_income=(gross_income-(5*gross_income)/100 )
    print("Since your gross income is {} your net income is {}".format(gross_income,net_income) )
elif (gross_income >=10000) & (gross_income < (150000)):
    net_income = (gross_income -(16*gross_income)/100 )
    print("Since your gross income is {} your net income is {}".format(gross_income,net_income) )
elif (gross_income >= int(150000)) & (gross_income < 300000):
    net_income =( gross_income - ((19/100)*gross_income))
    print("Since your gross income is {} your net income is {}".format(gross_income,net_income) )
else :
    net_income = (gross_income - ((30/100)*gross_income))
    print("Since your gross income is {} your net income is {}".format(gross_income,net_income) )