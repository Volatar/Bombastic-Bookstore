import sqlite3

def create_database():
    try:
        # Connect to SQLite database (creates it if it doesn't exist)
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Create a table
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            email TEXT NOT NULL
                        )''')

        # Commit changes
        conn.commit()
        print("Database created successfully!")

    except sqlite3.Error as e:
        print("Error creating database:", e)

def create_table(table_name, columns):
    try:
        # Connect to SQLite database
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Create a new table
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        cursor.execute(query)

        # Commit changes
        conn.commit()
        print(f"Table '{table_name}' created successfully!")

    except sqlite3.Error as e:
        print("Error creating table:", e)

def remove_table(table_name):
    try:
        # Connect to SQLite database
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Remove the table
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

        # Commit changes
        conn.commit()
        print(f"Table '{table_name}' removed successfully!")

    except sqlite3.Error as e:
        print("Error removing table:", e)

def insert_data_from_file(table_name, file_name):
    try:
        # Connect to SQLite database
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Read data from file and insert into the table
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                cursor.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?)", data)

        # Commit changes
        conn.commit()
        print("Data inserted successfully!")

    except sqlite3.Error as e:
        print("Error inserting data:", e)

def display_table_contents(table_name):
    try:
        # Connect to SQLite database
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Retrieve data from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Display data
        print(f"Contents of table '{table_name}':")
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print("Error displaying table contents:", e)

if __name__ == "__main__":
    create_database()
    create_table("books", "id INTEGER PRIMARY KEY, title TEXT, author TEXT")
    insert_data_from_file("books", "books_data.txt")
    display_table_contents("books")