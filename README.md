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

Input the following command to install Flask in the same way as the last step: `pip install flask`

You are now ready to run the application.