import requests
import random


def search_open_library(title):
    base_url = "http://openlibrary.org/search.json"
    params = {'title': title}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        works = data.get('docs', [])
        if works:
            # Getting the last ISBN result
            last_isbn = works[0].get('isbn', ['N/A'])[-1]

            # Getting the first result for genre, publisher, and category
            first_genre = works[0].get('subject', ['N/A'])[0]
            first_publisher = works[0].get('publisher', 'N/A')[0]
            first_category = works[0].get('subject', ['N/A'])[0]
            first_publish_date = works[0].get('publish_date', ['N/A'])[0]

            # random price between 4.99 and 24.99
            price = round(random.uniform(4.99, 24.99), 2)
            formatted_price = "{:.2f}".format(price)

            # Remaining code remains the same
            work = works[0]
            result = f"Title: {work.get('title', ['N/A'])}\n" \
                     f"Author: {', '.join(work.get('author_name', ['N/A']))}\n" \
                     f"Categories: {first_category}\n" \
                     f"Genres: {first_genre}\n" \
                     f"Publisher: {first_publisher}\n" \
                     f"Publish Date: {first_publish_date}\n" \
                     f"ISBN: {last_isbn}\n" \
                     f"Price: ${formatted_price}\n" \
                     f"---------------------------------------------\n"

            return result
        else:
            return f"Book {title} not found on Open Library."
    else:
        return f"Failed: {response.status_code}"


# Read in titles_only.txt file
with open('titles_only.txt', 'r', encoding='utf-8') as file:
    book_titles = [line.strip() for line in file]

# Open a file for writing
with open('search_open_library.txt', 'w', encoding='utf-8') as output_file:
    # Make a call to the API for each book title and write information to the file
    for book_title in book_titles:
        result = search_open_library(book_title)
        output_file.write(result)

print("Search results written to search_open_library.txt")
