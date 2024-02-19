import sqlite3
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def generate_bar_chart():
    limit = 40
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute(f"SELECT Quantity, ISBN FROM books LIMIT {limit}")  # Limiting to the specified number of books
    data = c.fetchall()
    quantities = [int(record[0]) for record in data]  # Ensure quantities are integers
    isbns = [record[1] for record in data]
    conn.close()

    plt.figure(figsize=(18, 15))  # Set the figure size to width by height
    bars = plt.barh(isbns, [q if q >= 5 else (q * 0.96) for q in quantities], color='gray')
    plt.xlabel('Quantity')
    plt.ylabel('ISBN')
    plt.title('Quantity of First 10 Books by ISBN')
    plt.grid(True)
    plt.xticks(range(0, 31, 5), [0, 5, 10, 15, 20, 25, 30])  # Set x-axis to go up to 30 with increments of 5

    # Set y-axis limit to the limit variable don't change
    plt.ylim(-1, limit)

    for bar, quantity in zip(bars, quantities):
        plt.text(bar.get_width() - 1, bar.get_y() + bar.get_height() / 2, str(quantity), va='center', fontweight='bold', color='white')

    plt.tight_layout()  # Adjust layout to remove whitespace
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    graph_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return graph_data
