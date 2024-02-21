import sqlite3
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def generate_bar_chart(page=1, items_per_page=25):
    offset = (page - 1) * items_per_page
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute(f"SELECT Quantity, Title FROM books LIMIT {items_per_page} OFFSET {offset}")
    data = c.fetchall()
    quantities = [int(record[0]) for record in data]
    titles = [record[1] for record in data]
    conn.close()

    plt.figure(figsize=(13, 10))
    bars = plt.barh(titles, [q if q >= 5 else (q * 0.96) for q in quantities], color='gray')
    plt.xlabel('Quantity')
    plt.ylabel('Title')
    plt.title('Quantity of Books by Title')
    plt.grid(True)
    plt.xticks(range(0, max(quantities) + 5, 5))
    plt.ylim(-1, items_per_page)

    for bar, quantity in zip(bars, quantities):
        plt.text(bar.get_width() - 1, bar.get_y() + bar.get_height() / 2, str(quantity), va='center', fontweight='bold', color='white')

    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    graph_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return graph_data
