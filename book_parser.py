import requests
from bs4 import BeautifulSoup

url = 'https://libraryof1000books.wordpress.com/the-list-of-1000-books/'

# Send request to the URL
response = requests.get(url)

# Check if successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate elements containing the list of books
    book_list_elements = soup.find_all('li')

    # Scrape the text of book list. Starting at the 4th list value
    # and Stopping after 1004 list values due to unneeded text before and after.
    book_list = [element.get_text(strip=True) for element in book_list_elements[4:1004]]

    # Open a file for writing. 
    # Do we need this? This gives title, author, and year in the .txt file
    with open('book_list.txt', 'w', encoding='utf-8') as file:
        for book in book_list:
            file.write(book + '\n')

    print("Books written to book_list.txt")

else:
    print("Failed to retrieve")

# Open a book_list.tx to split for titles only
with open('book_list.txt', 'r', encoding='utf-8') as file:
    book_list = [line.split('–', 1)[0].strip() for line in file]

# Output new titles_only.txt file
with open('titles_only.txt', 'w', encoding='utf-8') as output_file:
    for title in book_list:
        output_file.write(title + '\n')

print("Titles only written to titles_only.txt")
