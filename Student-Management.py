
import sqlite3

DB_NAME = "student.db"


def create_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        print("✅ Database connected successfully.")
        return conn
    except sqlite3.Error as e:
        print("❌ Database connection failed:", e)
        return None


def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT,
            marks INTEGER
        )
        """)
        conn.commit()
        print("✅ Table ready.")
    except sqlite3.Error as e:
        print("❌ Error creating table:", e)


def add_student(conn):
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        marks = int(input("Enter marks: "))

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO student (name, age, course, marks) VALUES (?, ?, ?, ?)",
            (name, age, course, marks)
        )
        conn.commit()
        print("✅ Student added successfully.")
    except ValueError:
        print("❌ Invalid input! Age and marks must be numbers.")
    except sqlite3.Error as e:
        print("❌ Error inserting student:", e)


def view_students(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()

        if not rows:
            print("No records found.")
        else:
            print("\n--- Student Records ---")
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print("❌ Error fetching data:", e)


def update_marks(conn):
    try:
        student_id = int(input("Enter student ID to update: "))
        new_marks = int(input("Enter new marks: "))

        cursor = conn.cursor()
        cursor.execute(
            "UPDATE student SET marks = ? WHERE id = ?",
            (new_marks, student_id)
        )
        conn.commit()

        if cursor.rowcount == 0:
            print("⚠ Student not found.")
        else:
            print("✅ Marks updated successfully.")
    except ValueError:
        print("❌ Invalid input.")
    except sqlite3.Error as e:
        print("❌ Error updating record:", e)


def delete_student(conn):
    try:
        student_id = int(input("Enter student ID to delete: "))

        cursor = conn.cursor()
        cursor.execute("DELETE FROM student WHERE id = ?", (student_id,))
        conn.commit()

        if cursor.rowcount == 0:
            print("⚠ Student not found.")
        else:
            print("✅ Student deleted successfully.")
    except ValueError:
        print("❌ Invalid input.")
    except sqlite3.Error as e:
        print("❌ Error deleting record:", e)


def main():
    conn = create_connection()
    if conn is None:
        return

    create_table(conn)

    while True:
        print("""
========= Student Management =========
1. Add Student
2. View Students
3. Update Marks
4. Delete Student
5. Exit
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(conn)
        elif choice == "2":
            view_students(conn)
        elif choice == "3":
            update_marks(conn)
        elif choice == "4":
            delete_student(conn)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

    conn.close()
    print("Database connection closed.")


if __name__ == "__main__":
    main()
