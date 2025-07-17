# Student Gradebook CLI App
# Add a new student with name and 3 subject marks
# Calculate total and average
# Assign grade (A/B/C/Fail)
# Display report

def student_gradebook():
    name = input("enter the sutudent name: ")
    sub1 = int(input("enter the marks of the first subject(?/100): "))
    sub2 = int(input("enter the marks of the second subject(?/100): "))
    sub3 = int(input("enter the marks of the third subject(?/100): ")) 

    mark_list = [sub1,sub2,sub3]
    total_marks = sub1+sub2+sub3
    avg_marks = total_marks/3
    print(f"the total marks are {total_marks},\nthe avg marks are {avg_marks}")

    if avg_marks <35:
        print("your results are: Fail")
    elif avg_marks ==35:
        print("your results are: Pass")
    elif avg_marks >35 and avg_marks<60:
        print("your results are: C")
    elif avg_marks >60 and avg_marks<80:
        print("your results are: B")
    elif avg_marks >80 and avg_marks<100:
        print("your results are: A")
    else:
        ("you have entered a wrong value please check")
    print(f"your marks are: {mark_list}")

    return (0)
student_gradebook()

choice = input("do you want try again(Yes/no): ")
if choice.lower() == "yes":
    student_gradebook()
else:
    print("Goodbye!")
