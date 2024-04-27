def main():
    num_students = int(input("How many students are registering? "))
    
    with open("reg_form.txt", "w") as file:
        for i in range(num_students):
            student_id = input(f"Enter student ID number {i+1}: ")
            file.write(f"{student_id}\n{'-' * len(student_id)}\n")

    print("Registration completed. Please check reg_form.txt for the attendance register.")

if __name__ == "__main__":
    main()
