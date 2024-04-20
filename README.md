# Bombastic Bookstore
SP2024-CSC289 Group project (group 2) at Wake Technical Community College

# Installation instructions using built in batch file

First, clone the repo or otherwise download the project files.
You will need Python 3.10 or later to run this project.
In the root folder of the project there will be a batch file named `Bombastic Bookstore Install.bat`.
Simply run this file, and it will install a virtual environment and all the required dependencies, and then will start the application.

![python installing dependancies](https://i.imgur.com/i50pFd5.png)

![the server starting up](https://i.imgur.com/mN9FCLv.png)

If you wish to stop the server from running, close the command line window that the batch file opened.

# Installation Instructions using Pycharm

If you want to modify the project you will want to install it via PyCharm.
First, clone/download the git repo to a folder on your computer.
Where this goes is up to you.
Then, open PyCharm and click File -> New Project in the upper left.

![PyCharm menu bar](https://i.imgur.com/kT245zw.png)

On the next screen you have to change several settings.

![PyCharm new project window](https://i.imgur.com/YM4q0qk.png)

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

![Directory is not empty prompt](https://i.imgur.com/4UAbauQ.png)

Click Create from Existing Sources.

You now have the PyCharm project created. 
There is one more step before you can run the application.

Go to the PyCharm project Terminal in the lower left of the screen:

![PyCharm bottom menu bar](https://i.imgur.com/JFLHGIW.png)

Input the following command: `pip install -r requirements.txt`

![PyCharm terminal window](https://i.imgur.com/j9KTgad.png)

You are now ready to run the application.

## How to run the web application

To run the web app, type `flask run` into the PyCharm Terminal when it is at the root project folder and connect to the localhost ip it provides in it's output with your web browser.
To stop the program, press ctrl-C in the same terminal.

# User logins
For testing purposes we have made several users.

The admin user's login is: admin
and their password is: Capstone

There is also a regular user login
login: test
password: test

You can also freely register new regular users as you wish.

# Features

### Add to Cart Button

- This button is available on every book. 
When pressed, it adds the book to the cart and redirects the user to the cart page.

    ![Add to Cart](https://i.imgur.com/vO50oFn.png)

### Navbar

- **Not Logged In**: Home and Login buttons.
    ![Navbar](https://i.imgur.com/w7NsFR4.png)
  
- **Logged In**: Home, Cart, Profile, and Logout buttons.
    ![Navbar](https://i.imgur.com/PVZ8x5O.png)
  
- **Admin**: Home, Cart, Profile, Logout, and Admin buttons.
    ![Navbar](https://i.imgur.com/tKZLE2m.png)

### Search Bar

- Allows users to search for books within the website by Title, Author, and Genre.

    ![Search Bar](https://i.imgur.com/KXzcFvW.png)

### Home Page

- Landing page featuring highlights of books.
Users can navigate to the Display Page by pressing the "View All" button.

    ![Home Page](https://i.imgur.com/XfJp4IL.png)

### Display Page

- Shows all the books in the database.

    ![Display Page](https://i.imgur.com/zRAUqMS.png)

### Book Details

- Displays all information about the selected book.

    ![Book Details](https://i.imgur.com/d7luRER.png)

### Search Results Page

- Displays search results based on the user's query.

    ![Search Results](https://i.imgur.com/j6Y1rwD.png)

### Login Page

- Allows users to log in to their accounts.

    ![Login Page](https://i.imgur.com/ePnRNBk.png)

### Register Page

- Enables new users to create an account.

    ![Register Page](https://i.imgur.com/zZLhwdM.png)

### Profile Page

- Displays user information.

    ![Profile Page](https://i.imgur.com/RmdmKgd.png)

### Cart Page

- Shows items that the user has added to their shopping cart.

    ![Cart Page](https://i.imgur.com/me7PLmT.png)

### Checkout Page

- Provides fields and steps for users to complete their purchases.

    ![Checkout Page](https://i.imgur.com/Dz2xzjM.png)

### Receipt Page

- Displays a receipt or confirmation message after a successful purchase.

    ![Receipt Page](https://i.imgur.com/iSkQial.png)

### Admin Page

- Allows management of products, inventory, and orders.

    ![Admin Page](https://i.imgur.com/ofsjCJ6.png)

### Catalog Page

- Lists all available products or items in a categorized manner.

    ![Catalog Page](https://i.imgur.com/asXlvS6.png)

### Inventory Page

- Allows admin users to manage the inventory of products.

    ![Inventory Page](https://i.imgur.com/W2Q3hUS.png)

### Order Page

- Displays details of past orders and allows users to track their orders.

    ![Order Page](https://i.imgur.com/heX2XGP.png)

### Sales Page

- Provides insights and analytics on sales data.

    ![Sales Page](https://i.imgur.com/uEwj47l.png)

### Visual Page

- Displays visual data such as Monthly Sales Trend, Sales Amount by State, Top Selling Authors, Inventory Percentages, and Top Selling Books.

    ![Visual Page](https://i.imgur.com/5OgkSBC.png)