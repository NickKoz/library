## Library

Terminal app using MySQL Connector/Python for access in database.
  

### Requirements

In order to run this app, you must have access to MySQL server. If you don't have already installed it,
you will have to install it from [MySQL site](https://dev.mysql.com/downloads/mysql/)  
      
It is recommended to use Python 3.6 or higher. Makefile uses Python 3.8, change it as you wish. You can download it from [here](https://www.python.org/downloads/).  
The app won't run with Python 2.
      
Then you have to enter the commands below in a linux terminal to install MySQL Connector for Python if you don't have it and then clone the project repo.
      
```bash
pip install mysql-connector-python
git clone https://github.com/NickKoz/library.git
```


### Run
```bash
cd ./library
make
```
