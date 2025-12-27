age = int(input("enter your age"))

if age < 18:
    print("your a minor")
elif age > 18 and age < 60:  
    print("your are an adult")
else:
    print("your are old")
