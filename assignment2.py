students_db = {}  
user = None  


def register():
    print("\n--- Student Registration ---")
    username = input("Enter Username: ")

    if username in students_db:
        print("Username already exists! Try another.")
        return

    password = input("Enter Password: ")
    name = input("Enter Full Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    course = input("Enter Course: ")
    year = int(input("Enter Year of Study: "))
    roll_no = input("Enter Roll Number: ")

    students_db[username] = {
        "password": password,
        "name": name,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone,
        "address": address,
        "course": course,
        "year": year,
        "roll_no": roll_no
    }
    print("Registration successful!\n")


def login():
    global user
    print("\n--- Student Login ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in students_db and students_db[username]["password"] == password:
        user = username
        print(f"Welcome, {students_db[username]['name']}!\n")
    else:
        print("Invalid username or password!\n")


def show_profile():
    global user
    if user:
        print("\n--- Student Profile ---")
        for key, value in students_db[user].items():
            if key != "password":
                print(f"{key.capitalize()}: {value}")
        print()
    else:
        print("Please login first!\n")


def update_profile():
    global user
    if user:
        print("\n--- Update Profile ---")
        for key in students_db[user]:
            if key != "password":  # don't show password for editing
                new_value = input(f"Enter new {key.capitalize()} (press Enter to skip): ")
                if new_value.strip() != "":
                    students_db[user][key] = new_value
        print("Profile updated successfully!\n")
    else:
        print("Please login first!\n")


def logout():
    global user
    if user:
        print(f"Goodbye, {students_db[user]['name']}!\n")
        user = None
    else:
        print(" logged out successfully.. \n")
def terminate():
    exit()


def main():
    while True:
        print("===== WELCOME TO LNCTS =====")
        print("1. Register")
        print("2. Login")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5. Logout")
        print("6. Main Menu")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            show_profile()
        elif choice == "4":
            update_profile()
        elif choice == "5":
            logout()
        elif choice == "6":
            print("welcome to Main Menu!")
            main()
        elif choice == "7":
             terminate()
        else:
            print("Invalid choice! Select correct option from menu.\n")

main()
