# Library

Terminal app simulation of a library system using MySQL Connector/Python for access in database.
  
The idea for the project was made from the semester class **Designing and Using Database Systems** of the department I attend.  

The whole project was made from me. It's my first big project in Python and I'm proud of it :D . Although, I can still develop it everyday by adding new features and -who knows- someday I will add a **GUI**.
  

## Requirements

In order to run this app, you must have access to MySQL server. If you don't have already installed it,
you will have to install it from [MySQL](https://dev.mysql.com/downloads/mysql/) site.
      
It is recommended to use Python 3.6 or higher. **Makefile** uses **Python 3.8**, use any as you wish. You can download it from [here](https://www.python.org/downloads/).  
The app **WON'T** run with **Python 2**.
      
Then you have to enter the commands below in a linux terminal to install **MySQL Connector for Python** if you don't already have it and then clone the project repo.
      
```bash
pip install mysql-connector-python
git clone https://github.com/NickKoz/library.git
```  

Then you have to open **MySQL server** and run SQL scripts **library.sql** and **initialize_library.sql** after. These scripts will prepare the database for you so you can run the program. These scripts will create the corresponding database and add an initial **admin**. You can add new users as **visitors** and then change their role using the **admin**.  
You can explore the rest of it in console!


## Run
To run the project, just enter its directory and then type `make` :
```bash
cd ./library
make
```

## Versions

* 1.9.1
    * ADD: Adding feature for updating user's personal data.
    * CHANGE: Updated user's interface for the new feature.
* 1.8.1
    * FIX: Minor bug fixes
    * FIX: Change repo's structure.

