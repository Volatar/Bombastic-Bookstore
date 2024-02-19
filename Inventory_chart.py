"""
    Colabrators
    Stefan inentory structor for the data
"""

import sqlite3
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generate_bar_chart():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("SELECT Quantity, ISBN FROM books LIMIT 10")  # Limiting to the first 10 books to see all data put 40
    data = c.fetchall()
    quantities = [int(record[0]) for record in data]  # Ensure quantities are integers
    isbns = [record[1] for record in data]
    conn.close()

    plt.barh(isbns, [q if q >= 5 else (q * 0.96) for q in quantities], color='skyblue')
    plt.xlabel('Quantity')
    plt.ylabel('ISBN')
    plt.title('Quantity of First 10 Books by ISBN')
    plt.grid(True)
    plt.xticks(range(0, 31, 5), [0, 5, 10, 15, 20, 25, 30])  # Set x-axis to go up to 30 with increments of 5
    for i in range(len(isbns)):
        plt.text(quantities[i], isbns[i], str(quantities[i]), va='center')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)


    graph_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return graph_data
