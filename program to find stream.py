#program to find grade of given marks
percentage=int(input("enter percentage="))
if percentage>80:
    print("eligible for science")
elif percentage<80 and percentage>=70:
    print("he is elligble for commerce")
else:
    print("he is elligible for arts")
