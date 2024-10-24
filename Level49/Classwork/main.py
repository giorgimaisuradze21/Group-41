# def main():
#     students = {}
    
#     while True:
#         name = input("Enter student's name (or type 'done' to finish): ")
#         if name.lower() == 'done':
#             break
        
#         try:
#             raviabaiyos = input(f"Enter marks for {name} separated by spaces: ")
#             wesit_marks = list(map(float, raviabaiyos.split()))
            
#             if not wesit_marks:
#                 print("No marks entered. Please try again.")
#                 continue
            
#             average = sum(wesit_marks) / len(wesit_marks)
#             students[name] = average
            
#         except ValueError:
#             print("Invalid input. Please enter numeric values for marks.")
    
#     if students:
#         best_student = max(students, key=students.get)
#         print(f"Average marks of students:")
#         for student, avg in students.items():
#             print(f"{student}: {avg}")
        
#         print(f"The best student is {best_student} with an average mark of {students[best_student]}.")
#     else:
#         print("No students were entered.")

# if __name__ == "__main__":
#     main()
        
        
        
        
        
        
def process_grades(grades):
    if not grades:
        return None, None, None

    maximum = max(grades)
    minimum = min(grades)
    average = sum(grades) / len(grades)

    return maximum, minimum, average

# სტუდენტების ქულების სია
grades = [85, 90, 78, 92, 88, 76]

# პროგრამის გაწვდვა
maximum, minimum, average = process_grades(grades)

print(f"{maximum}")
print(f"{minimum}")
print(f" {average:.2f}")