import sqlite3

# 1. Collect information from user
user = {
    "name": input("Enter your name: "),
    "age": int(input("Enter your age: ")),
    "email": input("Enter your email: ")
}

# 2. Connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# 3. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")

# 4. Store dictionary data in database
cursor.execute("""
INSERT INTO users (name, age, email)
VALUES (:name, :age, :email)
""", user)

# 5. Save changes
conn.commit()


# run this code after the previous code to close the database connection

conn.close()


print("User information stored successfully!")