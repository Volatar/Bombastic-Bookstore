from flask import Flask, render_template
import sqlite3
import matplotlib
matplotlib.use('Agg')  # Set Matplotlib backend to 'Agg' to avoid GUI warning
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

def execute_query(query):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        return cursor.fetchall()
    finally:
        conn.close()

def monthly_sales_trend():
    sales_data = execute_query(
        "SELECT strftime('%Y-%m', purchase_date) AS Sale_Day, SUM(amount) AS Total_Sales "
        "FROM purchases "
        "GROUP BY Sale_Day "
        "ORDER BY Sale_Day"
    )
    days = [row['Sale_Day'] for row in sales_data]
    total_sales = [row['Total_Sales'] for row in sales_data]

    plt.figure(figsize=(10, 6))
    plt.plot(days, total_sales, marker='o', color='orange', linestyle='-')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Day')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return plot_url

def sales_by_state():
    sales_data = execute_query(
        "SELECT state, SUM(amount) AS total_sales "
        "FROM purchases "
        "GROUP BY state "
        "ORDER BY total_sales DESC"
    )
    states = [row['state'] for row in sales_data]
    total_sales = [row['total_sales'] for row in sales_data]

    plt.figure(figsize=(10, 6))
    plt.bar(states, total_sales, color='skyblue')
    plt.title('Sales Amount by State')
    plt.xlabel('State')
    plt.ylabel('Total Sales Amount')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return plot_url

def top_selling_authors():
    author_data = execute_query("""
    SELECT b.author, SUM(p.amount) AS total_sales
    FROM purchases p
    INNER JOIN books b ON p.isbn = b.isbn
    GROUP BY b.author
    ORDER BY total_sales DESC
    LIMIT 10
    """)
    authors = [row['author'] for row in author_data]
    total_sales = [row['total_sales'] for row in author_data]

    plt.figure(figsize=(10, 6))
    plt.bar(authors, total_sales, color='green')
    plt.title('Top Selling Authors')
    plt.xlabel('Author')
    plt.ylabel('Total Sales Amount')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return plot_url


def plot_books_quantity_pie():
    # Fetch quantities of books in different categories
    categories_data = execute_query("""
    SELECT 
        SUM(CASE WHEN quantity < 5 THEN 1 ELSE 0 END) AS less_than_5,
        SUM(CASE WHEN quantity BETWEEN 6 AND 25 THEN 1 ELSE 0 END) AS between_6_and_25,
        SUM(CASE WHEN quantity BETWEEN 26 AND 40 THEN 1 ELSE 0 END) AS between_26_and_40,
        SUM(CASE WHEN quantity >= 41 THEN 1 ELSE 0 END) AS more_than_40
    FROM books
    """)

    # Extract counts of books in each category
    categories = categories_data[0]
    less_than_5 = categories['less_than_5']
    between_6_and_25 = categories['between_6_and_25']
    between_26_and_40 = categories['between_26_and_40']
    more_than_40 = categories['more_than_40']

    # Calculate percentages
    total_books = less_than_5 + between_6_and_25 + between_26_and_40 + more_than_40
    percentages = [
        less_than_5 / total_books * 100,
        between_6_and_25 / total_books * 100,
        between_26_and_40 / total_books * 100,
        more_than_40 / total_books * 100
    ]

    # Categories labels
    labels = ['Less than 5', '6-25', '26-40', 'More than 40']

    # Plotting
    plt.figure(figsize=(8, 8))
    plt.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Books Quantity Inventory')

    # Save plot to bytesIO and convert to base64
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return plot_url

def top_selling_books():
    title_data = execute_query("""
    SELECT b.title, SUM(p.amount) AS total_sales
    FROM purchases p
    INNER JOIN books b ON p.isbn = b.isbn
    GROUP BY b.title
    ORDER BY total_sales DESC
    LIMIT 10
    """)
    authors = [row['title'] for row in title_data]
    total_sales = [row['total_sales'] for row in title_data]

    plt.figure(figsize=(10, 6))
    plt.bar(authors, total_sales, color='green')
    plt.title('Top Selling Books')
    plt.xlabel('Title')
    plt.ylabel('Total Sales Amount')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return plot_url

if __name__ == "__main__":
    app.run(debug=True)
