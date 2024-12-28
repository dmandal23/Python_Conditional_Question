score = int(input("Enter Score"))

if score >= 101:
    print("Please verify your score again")
    exit()


if score >= 80:
    grade = "A"

elif score >= 70:
    grade = "B"    

elif score >= 60:
    grade = "B" 

elif score >= 50:
    grade = "C"

else:
    grade = "D"    
         
print("Grade: ",grade)         