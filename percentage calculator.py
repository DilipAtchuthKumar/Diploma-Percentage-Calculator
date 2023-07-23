first_sem_marks = float(input("Enter the marks obtained in 1st sem: "))
third_sem_marks = float(input("Enter the marks obtained in 3rd sem: "))
fourth_sem_marks = float(input("Enter the marks obtained in 4th sem: "))
fifth_sem_marks = float(input("Enter the marks obtained in 5th sem: "))
sixth_sem_marks = float(input("Enter the marks obtained in 6th sem: "))

Addition = first_sem_marks / 4 + third_sem_marks + fourth_sem_marks + fifth_sem_marks + sixth_sem_marks
Over_all_Percentage = Addition / 3250 * 100

print("Overall percentage of your diploma is:", Over_all_Percentage)