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

def read_book_info(file_path):
    book_info = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ', 1)
            book_info[key] = value
    return book_info

def create_table_if_not_exists(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        title TEXT,
                        author TEXT,
                        genres TEXT,
                        publisher TEXT,
                        publish_date TEXT,
                        isbn TEXT,
                        price TEXT
                    )''')

def insert_book_info(cursor, book_info):
    cursor.execute('''INSERT INTO books VALUES (
                        :title, :author, :genres,
                        :publisher, :publish_date, :isbn, :price
                    )''', book_info)

file_path = 'search_open_library.txt'  # Replace 'book_info.txt' with the path to your text file

# Read book info from the text file
book_info = read_book_info(file_path)

# Connect to SQLite database
conn = sqlite3.connect('books.db')  # Connect to or create if not exists the database
cursor = conn.cursor()

# Create table if not exists
create_table_if_not_exists(cursor)

# Insert book info into the database
insert_book_info(cursor, book_info)

# Commit changes
conn.commit()

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
    display_table_contents("books")