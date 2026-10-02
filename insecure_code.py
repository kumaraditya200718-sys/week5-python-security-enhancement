import sqlite3

def login(username, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

    cursor.execute(query)
    result = cursor.fetchone()

    connection.close()

    if result:
        print("Login successful")
    else:
        print("Invalid username or password")


username = input("Enter username: ")
password = input("Enter password: ")

login(username, password)