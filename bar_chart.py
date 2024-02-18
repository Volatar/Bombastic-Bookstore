import sqlite3
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generate_bar_chart():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("SELECT Quantity, ISBN FROM books LIMIT 10")  # Limiting to the first 10 books
    data = c.fetchall()
    quantities = [record[0] for record in data]
    isbns = [record[1] for record in data]
    conn.close()

    plt.barh(isbns, quantities, color='skyblue')
    plt.xlabel('Quantity')
    plt.ylabel('ISBN')
    plt.title('Quantity of First 10 Books by ISBN')
    plt.grid(True)
    for i in range(len(isbns)):
        plt.text(quantities[i], isbns[i], str(quantities[i]), va='center')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    graph_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return graph_data
