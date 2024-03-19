import psycopg2

# Define connection parameters to connect to the PostgreSQL database
conn_params = {
    'dbname': 'students', # Name of the databas
    'user': 'your_username', # Username used to authenticate
    'password': 'your_password!', # Password used to authenticate
    'host': 'localhost' # Database server address e.g., localhost or an IP address
}

def getAllStudents():

    # Connects to the PostgreSQL database and retrieves all student records

    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM students;') # Executes SQL query
            for record in cur.fetchall(): # Fetches all rows of a query result
                print(record) # Prints each student record


def emailExists(email):

    # Checks if the given email already exists in the database

    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT email FROM students WHERE email = %s;', (email,))
            return cur.fetchone() is not None # Returns True if email exists

def studentIdExists(student_id):

     # Checks if the given student ID exists in the database

    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT student_id FROM students WHERE student_id = %s;', (student_id,))
            return cur.fetchone() is not None # Returns True if student ID exists

def addStudent(first_name, last_name, email, enrollment_date):

    # Adds a new student to the database if the email is not already used

    if not emailExists(email):
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);',
                            (first_name, last_name, email, enrollment_date))
                print("Student added successfully.")
    else:
        print("Error: A student with this email already exists.")

def updateStudentEmail(student_id, new_email):

    # Updates the email of an existing student if the student ID exists and the new email is not already in use

    if studentIdExists(student_id) and not emailExists(new_email):
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute('UPDATE students SET email = %s WHERE student_id = %s;',
                            (new_email, student_id))
                print("Email updated successfully.")
    else:
        if not studentIdExists(student_id):
            print("Error: No student found with the given ID.")
        else:
            print("Error: The new email is already in use.")

def deleteStudent(student_id):

    # Deletes a student from the database if the student ID exists

    if studentIdExists(student_id):
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute('DELETE FROM students WHERE student_id = %s;', (student_id,))
                print("Student deleted successfully.")
    else:
        print("Error: No student found with the given ID.")

# Example usage
# Main section to demonstrate the functionality of the functions above
if __name__ == '__main__':
    # Demonstrates the functionality of adding, updating, and deleting student records
    #addStudent('Alice', 'Wonderland', 'alice@example.com', '2023-10-01')
    #updateStudentEmail(1, 'new.john.doe@example.com')
    deleteStudent(2)
    #getAllStudents()