# html_parsing

This README contains information about the Python exam. 


## Task 1: Create and initialize a Python project 

The goal of this task was to automate the process of setting up the working environment through the creation of a virtual environment and the installation of dependencies. For this purpose, we created a Makefile that first checks if the OS is Windows or a Unix-like system and then creates a virtual environment and installs dependencies. The script was tested only on  Windows and should be also tested on Linux/Mac. After the environment has been set up, we are able to run different commands and use our application. 


## Task 2: Detect & parse Holidays

The goal of this task was to scrape information about public holidays in Western Australia. The web page provided offers data about 11 different Holidays for the years 2022, 2023, and 2024. With help of requests_html, we were able to scrape and parse the HTML table that contained the required information. The code for scraping and parsing the data is located in assignment/get_holidays.py where we created GetPublicHolidays class. We could have achieved the same thing by using pandas read_html()  (assignment/pandas_parser.py) that automatically parses HTML table in a data frame and reduces the need for coding (but where is the fun in that). The main application is located in assignment/app.py where we simply instantiated our class, printed the parsed data, and then stored it into SQLite DB.  



## Task 3: Implement a unit test class 

The goal of this task was to create a unit test for our parsing functions. The code for this is located in assingment/get_holidays_test.py. We created a total of 4 tests: 
1. the First test is checking if we scraped the right page by checking the page title (Public holidays in Western Australia | Department of Mines, Industry Regulation and Safety). Each time we run our app, we store the page title in a file for testing purposes. 
2. the Second test is checking if we returned the expected list of Holidays (11 in total). We select distinct Holidays from our database and compare them against the holiday list from the config file. 
3. the Third test does the same thing but for the years. We know that currently, the given URL contains data for 2022, 2023, and 2024 and those are the years that we expect to see in our database. 
4. The last test is aimed at checking if we returned the expected number of rows(records). As we know that on the given URL we have 11 different holidays, and for each one of them we know that we are supposed to get 3 different records, which gives us a total of 33 rows. We simply verify that number against the number of records (select count (*) from Holidays) stored in our database. 

## Task 4: Save the parsed result into sqlite3 in-memory database

The goal of this task was to store retrieved data into an SQLite DB. For that purpose, we created db_conn.py where we with help of SQLalchemy create a connection for our Sqlite DB. 


# INSTRUCTIONS


1. In the project directory run "make run". This command will first check if venv task (creation of virtualenv and installation of dependencies) has been satisfied and will then run the app. If not, it will automatically run "venv" task and prepare the working environment. 

2. If you want to read the data from th#e database, use "make read_sql". In order to avoid running SQL against a nonexisting database, this action will trigger "make run" to make sure that there is data in the database. 

3. In order to perform the unit test, use the "make run_test" command. 

4. In order to build and run a docker image, you can use the "make docker" command. It will first run the docker build command, and then the docker run with "python assignment/app.py" as the default cmd. If you wish to run some other command, you can do it by changing CMD variable in Makefile (python assignment/sql_read.py to read data from SQLite or python -m pytest assignment/get_holiday_test.py to run the unit test). 




# Future suggestions

The Makefile should be tested on Linux/OS and modified if needed. 


