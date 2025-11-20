import json
import random
import datetime
import os

# --- File Definitions ---
STUDENTS_FILE = 'students.json'
QUIZZES_FILE = 'quizzes.json'
SCORES_FILE = 'scores.json'

# --- Global Databases ---
students_db = {}
quizzes_db = {}
scores_db = []
current_user = None  # Stores the username of the logged-in user
current_role = None  # Stores the role (student or admin)

# --- Data Handling Functions ---
def load_data():
    """Loads all data from .json files into memory."""
    global students_db, quizzes_db, scores_db
    
    # Load students
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, 'r') as f:
            try:
                students_db = json.load(f)
            except json.JSONDecodeError:
                students_db = {}
    
    # If admin doesn't exist (or file was empty), create default admin
    if not students_db or "admin" not in students_db:
        students_db["admin"] = {
            "password": "admin123",
            "name": "Administrator",
            "email": "admin@school.com",
            "phone": "1234567890",
            "branch": "Admin",
            "year": 0,
            "roll_no": "A001",
            "role": "admin"
        }
        save_data(STUDENTS_FILE, students_db)

    # Load quizzes
    if os.path.exists(QUIZZES_FILE):
        with open(QUIZZES_FILE, 'r') as f:
            try:
                quizzes_db = json.load(f)
            except json.JSONDecodeError:
                quizzes_db = {}
    else:
        # Create default quizzes if file doesn't exist
        quizzes_db = {
            "DSA": [
                {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "answer": "O(log n)"},
                {"question": "Which data structure uses LIFO?", "options": ["Queue", "Stack", "Array", "Linked List"], "answer": "Stack"},
                {"question": "A graph with no cycles is called?", "options": ["Tree", "Complete Graph", "Bipartite Graph", "Directed Graph"], "answer": "Tree"},
                {"question": "What is the worst-case time complexity of Quicksort?", "options": ["O(n log n)", "O(n)", "O(n^2)", "O(log n)"], "answer": "O(n^2)"},
                {"question": "Which of the following is not a sorting algorithm?", "options": ["Merge Sort", "Dijkstra's", "Bubble Sort", "Insertion Sort"], "answer": "Dijkstra's"}
            ],
            "DBMS": [
                {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Simple Query Language", "Standard Query Language", "Sequential Query Language"], "answer": "Structured Query Language"},
                {"question": "Which command is used to remove a table from the database?", "options": ["DELETE", "REMOVE", "DROP TABLE", "TRUNCATE"], "answer": "DROP TABLE"},
                {"question": "What is a primary key?", "options": ["A unique identifier for a record", "A key to open the database", "The first key in a table", "A foreign key"], "answer": "A unique identifier for a record"},
                {"question": "Which normal form deals with transitive dependency?", "options": ["1NF", "2NF", "3NF", "BCNF"], "answer": "3NF"},
                {"question": "The 'SELECT' statement is used to...", "options": ["Update data", "Query data", "Delete data", "Insert data"], "answer": "Query data"}
            ],
            "PYTHON": [
                {"question": "What keyword is used to define a function in Python?", "options": ["func", "def", "function", "define"], "answer": "def"},
                {"question": "Which data type is immutable in Python?", "options": ["List", "Dictionary", "Set", "Tuple"], "answer": "Tuple"},
                {"question": "How do you start a single-line comment in Python?", "options": ["//", "/*", "#", "<!--"], "answer": "#"},
                {"question": "What does 'pip' stand for?", "options": ["Python Installation Package", "Pip Installs Python", "Preferred Installer Program", "Python Internal Packages"], "answer": "Preferred Installer Program"},
                {"question": "Which method is used to get the length of a list?", "options": ["size()", "length()", "len()", "count()"], "answer": "len()"}
            ]
        }
        save_data(QUIZZES_FILE, quizzes_db)

    # Load scores
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            try:
                scores_db = json.load(f)
            except json.JSONDecodeError:
                scores_db = []
    else:
        scores_db = []
        save_data(SCORES_FILE, scores_db)

def save_data(file_name, data):
    """Saves a given data structure to a .json file."""
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)

# --- Core Functions ---
def register():
    global students_db
    print("\n--- Student Registration ---")
    username = input("Enter Username: ")
    if username in students_db:
        print("Username already exists! Try another.")
        return
    password = input("Enter Password: ")
    name = input("Enter Full Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    branch = input("Enter Branch (e.g., CSE, ME, ECE): ")
    try:
        year = int(input("Enter Year of Study (1-4): "))
    except ValueError:
        print("Invalid year. Setting to 1.")
        year = 1
    roll_no = input("Enter Roll Number (Enrollment): ")
    
    students_db[username] = {
        "password": password,
        "name": name,
        "email": email,
        "phone": phone,
        "branch": branch,
        "year": year,
        "roll_no": roll_no,
        "role": "student"  # All new registrations are students
    }
    save_data(STUDENTS_FILE, students_db)
    print("Registration successful!\n")

def login():
    global current_user, current_role
    print("\n--- Login ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    if username in students_db and students_db[username]["password"] == password:
        current_user = username
        current_role = students_db[username]["role"]
        print(f"\nWelcome, {students_db[username]['name']}! ({current_role.capitalize()})")
        
        if current_role == 'student':
            student_menu()
        elif current_role == 'admin':
            admin_menu()
    else:
        print("Invalid username or password!\n")

def logout():
    global current_user, current_role
    if current_user:
        print(f"\nGoodbye, {students_db[current_user]['name']}!")
        current_user = None
        current_role = None
    else:
        print("You are not logged in.")

# --- Student Menu Functions ---
def student_menu():
    while current_user:
        print("\n--- Student Menu ---")
        print("1. Attempt Quiz")
        print("2. View My Scores")
        print("3. View Profile")
        print("4. Update Profile")
        print("5. Logout")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            attempt_quiz()
        elif choice == '2':
            view_my_scores()
        elif choice == '3':
            show_profile()
        elif choice == '4':
            update_profile()
        elif choice == '5':
            logout()
            break
        else:
            print("Invalid choice. Please try again.")

def attempt_quiz():
    print("\n--- Attempt Quiz ---")
    print("Select a category:")
    categories = list(quizzes_db.keys())
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")
        
    try:
        choice = int(input("Enter category number: "))
        if 1 <= choice <= len(categories):
            selected_category = categories[choice - 1]
            run_quiz(selected_category)
        else:
            print("Invalid category number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def run_quiz(category):
    global scores_db
    questions = list(quizzes_db[category])  # Make a copy
    random.shuffle(questions)
    
    # Let's use 5 questions per quiz
    num_questions = min(len(questions), 5)
    selected_questions = questions[:num_questions]
    
    score = 0
    print(f"\n--- Starting {category} Quiz ---")
    print(f"You will be asked {num_questions} questions.\n")
    
    for i, q in enumerate(selected_questions):
        print(f"Q{i+1}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"   {j+1}. {option}")
            
        try:
            user_ans_num = int(input("Your answer (number): "))
            user_ans = q['options'][user_ans_num - 1]
        except (ValueError, IndexError):
            user_ans = ""
            print("Invalid option. Marked as incorrect.")
            
        if user_ans == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was: {q['answer']}\n")
            
    print(f"--- Quiz Finished ---")
    print(f"Your final score: {score} / {num_questions}")
    
    # Save the score
    score_entry = {
        "username": current_user,
        "enrollment": students_db[current_user]["roll_no"],
        "category": category,
        "score": f"{score}/{num_questions}",
        "datetime": datetime.datetime.now().isoformat()
    }
    scores_db.append(score_entry)
    save_data(SCORES_FILE, scores_db)
    print("Your score has been saved.")

def view_my_scores():
    print("\n--- My Scores ---")
    user_scores = [s for s in scores_db if s['username'] == current_user]
    
    if not user_scores:
        print("You have not attempted any quizzes yet.")
        return
        
    # Sort by date, newest first
    user_scores.sort(key=lambda x: x['datetime'], reverse=True)
    
    print(f"{'Datetime':<26} | {'Category':<10} | {'Score':<10} | {'Enrollment':<15}")
    print("-" * 70)
    for s in user_scores:
        dt = datetime.datetime.fromisoformat(s['datetime']).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{dt:<26} | {s['category']:<10} | {s['score']:<10} | {s['enrollment']:<15}")

def show_profile():
    if not current_user:
        print("Please login first!")
        return
        
    print("\n--- Student Profile ---")
    user_data = students_db[current_user]
    print(f"Username: {current_user}")
    print(f"Full Name: {user_data.get('name', 'N/A')}")
    print(f"Email:    {user_data.get('email', 'N/A')}")
    print(f"Phone:    {user_data.get('phone', 'N/A')}")
    print(f"Branch:   {user_data.get('branch', 'N/A')}")
    print(f"Year:     {user_data.get('year', 'N/A')}")
    print(f"Roll No:  {user_data.get('roll_no', 'N/A')}")
    print(f"Role:     {user_data.get('role', 'N/A')}")

def update_profile():
    if not current_user:
        print("Please login first!")
        return
        
    print("\n--- Update Profile ---")
    print("Enter new value or press Enter to skip.")
    user_data = students_db[current_user]
    
    # Fields to update: name, email, phone (contact), branch, year
    fields_to_update = ['name', 'email', 'phone', 'branch', 'year']
    
    for key in fields_to_update:
        current_value = user_data.get(key, 'N/A')
        new_value = input(f"Enter new {key.capitalize()} (current: {current_value}): ")
        if new_value.strip() != "":
            if key == 'year':
                try:
                    user_data[key] = int(new_value)
                except ValueError:
                    print("Invalid year. Skipping update for this field.")
            else:
                user_data[key] = new_value
                
    save_data(STUDENTS_FILE, students_db)
    print("Profile updated successfully!\n")

# --- Admin Menu Functions ---
def admin_menu():
    while current_user:
        print("\n--- Admin Menu ---")
        print("1. View All Scores")
        print("2. View All Users")
        print("3. Manage Quizzes (Not Implemented)")
        print("4. Logout")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_all_scores()
        elif choice == '2':
            view_all_users()
        elif choice == '3':
            print("Quiz management is not yet implemented.")
        elif choice == '4':
            logout()
            break
        else:
            print("Invalid choice. Please try again.")

def view_all_scores():
    print("\n--- All Student Scores ---")
    if not scores_db:
        print("No quizzes have been attempted by any student.")
        return
        
    # Sort by date, newest first
    all_scores = sorted(scores_db, key=lambda x: x['datetime'], reverse=True)
    
    print(f"{'Datetime':<26} | {'Username':<15} | {'Category':<10} | {'Score':<10} | {'Enrollment':<15}")
    print("-" * 85)
    for s in all_scores:
        dt = datetime.datetime.fromisoformat(s['datetime']).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{dt:<26} | {s['username']:<15} | {s['category']:<10} | {s['score']:<10} | {s['enrollment']:<15}")

def view_all_users():
    print("\n--- All Registered Users ---")
    print(f"{'Username':<20} | {'Name':<25} | {'Role':<10} | {'Roll No':<15}")
    print("-" * 75)
    for username, data in students_db.items():
        print(f"{username:<20} | {data.get('name', 'N/A'):<25} | {data.get('role', 'N/A'):<10} | {data.get('roll_no', 'N/A'):<15}")

# --- Main Application Loop ---
def main():
    load_data()  # Load all data on startup
    while True:
        print("\n===== WELCOME TO LNCTS QUIZ PORTAL =====")
        print("1. Register (New Student)")
        print("2. Login (Student / Admin)")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Select a correct option from the menu.\n")

if __name__ == "__main__":
    main()
