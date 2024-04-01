import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg (non-interactive) mode also use for not crashing the server
import sqlite3
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from collections import OrderedDict

# Global variables for caching
MAX_CACHE_SIZE = 100  # Maximum number of cached chart images
chart_cache = OrderedDict()  # Ordered dictionary to store cached chart images


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

    # Cache the generated chart image
    cache_key = f'{page}_{items_per_page}'
    cache_chart(cache_key, graph_data)

    return graph_data


def cache_chart(cache_key, chart_data):
    global chart_cache
    # Check if cache is full
    if len(chart_cache) >= MAX_CACHE_SIZE:
        # Remove the least recently used chart from the cache
        chart_cache.popitem(last=False)
    # Add the new chart to the cache
    chart_cache[cache_key] = chart_data


def get_cached_chart(cache_key):
    global chart_cache
    # Move the accessed chart to the end to mark it as most recently used
    if cache_key in chart_cache:
        chart_data = chart_cache.pop(cache_key)
        chart_cache[cache_key] = chart_data
        return chart_data
    return None


def clear_cache():
    global chart_cache
    chart_cache.clear()
