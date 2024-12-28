#  Questions On Conditionals

'''
Age group categorization steps
> Calasify a person's age group
> child(<13)
> teenager(13-19)
> adult(20-59)
>senior(60+)

'''

age = int(input("Enter age"))


if age < 13:
    print("child")

elif age < 20:
    print("teenager")

elif age < 60:
    print("adult")    

else:
    print("senior")
