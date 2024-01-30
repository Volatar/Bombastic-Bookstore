import requests
from bs4 import BeautifulSoup

url = 'https://libraryof1000books.wordpress.com/the-list-of-1000-books/'

# Send request to the URL
response = requests.get(url)

# Check if successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the element(s) containing the list of books
    book_list_elements = soup.find_all('li')

    # Scrape the text of book list.
    # Starting at the 4th list value and Stopping after 1000 list values due to unneeded text before and after.
    book_list = [element.get_text(strip=True) for element in book_list_elements[4:1000]]

    # For loop to print all books in list
    for book in book_list:
        print(book)

else:
    print("Failed to retrieve")
