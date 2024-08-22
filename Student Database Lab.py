# Initialize the lists with student information
student_names = ["Alice", "Bob", "Charlie", "Diana"]
hometowns = ["New York", "Los Angeles", "Chicago", "Houston"]
favorite_foods = ["Pizza", "Sushi", "Tacos", "Burger"]


def get_student_info():
    while True:
        try:
            # Prompt the user to enter a student number
            student_number = int(input(f"Enter a student number (1 to {len(student_names)}): "))

            # Validate if the number is within the valid range
            if 1 <= student_number <= len(student_names):
                # Adjust index to be zero-based
                index = student_number - 1

                # Print the student's name
                print(f"Student Name: {student_names[index]}")

                # Prompt for category
                while True:
                    category = input("Would you like to know their Hometown or Favorite Food? ").strip().lower()

                    if category == "hometown":
                        print(f"Hometown: {hometowns[index]}")
                        break
                    elif category == "favorite food":
                        print(f"Favorite Food: {favorite_foods[index]}")
                        break
                    else:
                        print("Invalid category. Please enter 'Hometown' or 'Favorite Food'.")

                # Ask if they want to know about another student
                again = input("Would you like to learn about another student? (yes/no): ").strip().lower()
                if again != 'yes':
                    print("Thank you for using the student information program.")
                    break
            else:
                print(f"Invalid number. Please enter a number between 1 and {len(student_names)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Start the program
get_student_info()
