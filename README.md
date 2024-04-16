# Bombastic Bookstore
SP2024-CSC289 Group project (group 2) at Wake Technical Community College

# Installation Instructions using Pycharm

First, clone/download the git repo to a folder on your computer.
Where this goes is up to you.
Then, open PyCharm and click File -> New Project in the upper left.

![](https://i.imgur.com/kT245zw.png)

On the next screen you have to change several settings.

![](https://i.imgur.com/YM4q0qk.png)

Change the location at the top to your new folder with the project files in it
Select "New environment using `Virtualenv`", and select a location for this. 
I suggest a sub folder to the rest of the project titled `.venv` as this is included in the gitignore already.
Base interpreter should be the latest version of Python you have. 
Minimum `3.10`.
Do not inherit global packages. 
Making available to all projects is up to you, I suggest no.
Do not create a welcome script.
Click create.

Next you will be presented with this prompt:

![](https://i.imgur.com/4UAbauQ.png)

Click Create from Existing Sources.

You now have the PyCharm project created. 
There is one more step before you can run the application.

Go to the PyCharm project Terminal in the lower left of the screen:

![](https://i.imgur.com/JFLHGIW.png)

Input the following command: `pip install -r requirements.txt`

![](https://i.imgur.com/j9KTgad.png)

You are now ready to run the application.

# How to run the web application

To run the web app, type `flask run` into the PyCharm Terminal when it is at the root project folder and connect to the localhost ip it provides in it's output with your web browser.
To stop the program, press ctrl-C in the same terminal.

# User logins
For testing purposes we have made several users.

The admin user's login is: admin
and their password is: Capstone

There is also a regular user login
login: test
password: test

# The Features

## Add to Cart Button

- This button is on evey book and when pressed it will add the book and then direct the user to the cart page.

## Navbar

- If the user is not logged in, they will only see the Home and Login buttons.
- If the user is logged in, they will see the Home, Cart, Profile, and Logout buttons.
- If the user is an admin, they will see the Home, Cart, Profile, Logout, and Admin buttons.

Below the Navbar buttons, there is a Search Bar.

## Search Bar

- Allows users to search for books within the website, with the ability to search by Title, Author, and Genre.
- How to use: Enter your what you want in the input bar then on the right or below that you can see a drop down menu select how you want to search and then hit the search button.

## Home Page

- Serves as the landing page of the website, featuring highlights of books. Users have the option to navigate to the Display Page by pressing the "View All" button.

## Display Page

- Shows all the books in the database.

## Book Details

- Show all of the selected Book info

## Search Results Page

- Displays search results based on the user's query.

## Login Page

- Allows users to log in to their accounts.

## Register Page

- Enables new users to create an account.

## Profile Page

- Displays user information.

## Cart Page

- Shows items that the user has added to their shopping cart.

## Checkout Page

- Provides the necessary fields and steps for users to complete their purchases.

## Receipt Page

- Displays a receipt or confirmation message after a successful purchase.

## Admin Page

- Accessible only to admin users, this page allows management of products, inventory, and orders.

## Catalog Page

- Lists all available products or items in a categorized manner.

## Inventory Page

- Allows admin users to manage the inventory of products.

## Order Page

- Displays details of past orders and allows users to track their orders.

## Sales Page

- Provides insights and analytics on sales data.

## Visual Page

- Possibly visual data like Monthly Sales Trend, Sales Amount by State, Top Selling Authors, Inventory Percentages, and Top Selling Books.
