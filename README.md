World Port Index Data Migration
•	Table of contents
•	Introduction/Project Overview
•	Objective
•	Instructions
•	How it works
•	Data Extraction
•	Loading the data
•	SQL Queries analysis and result Explanation
•	Requirements
•	Conclusion
•	Contribution and Feedback
Introduction/Project Overview
GoFrieghts, a prominent logistics company, has enlisted your expertise as a Data Engineer. Your remit involves migrating. World Port Index data from an archaic Access database to a contemporary PostgreSQL relational database. The resultant analysis will facilitate the creation of data marts.
Objective
The objective of this project is to construct an Extract Load (EL) pipeline in Python to transition the World Port Index data from the Access database to PostgreSQL.
Instructions
Construct an Extract Load (EL) pipeline in Python to transition the World Port Index data from the Access database to PostgreSQL Database, executing specific set of SQL queries and analysis the following:
•	Find the Nearest Ports to Singapore's JURONG ISLAND.
•	Find Country with the Largest Number of Cargo Wharf Ports.
•	Nearest Port with Provisions, Water, Fuel, and Diesel

How it Works
1.	Install Necessary Python Modules:
Ensure you have the required Python modules installed. This can be achieved using the following code snippet: 
•	from sqlalchemy import create_engine
•	from time import time
•	import pyodbc
•	import pandas as pd
2.	Establish Connection to Access Database.
Create a function to establish a connection to the Microsoft Access database:
3.	Get Table Names from Access Database
Retrieve the list of table names from the Access database and print them.
4.	Read World Port Index Data Table Using Pandas DataFrame
Define a function to query the "Wpi Data" table from the Access database and store the result in a Pandas DataFrame.
5.	Load DataFrame into PostgreSQL Database
Use the sqlalchemy library to load the DataFrame into the PostgreSQL database:
6.	Connect to PostgreSQL Database for Querying
Define functions to establish a connection to the PostgreSQL database and run SQL queries

Data Extraction: 
The data extraction was done with Python, using python libraries, import pyodbc, which enable connection the Microsoft access database, and thus reading and printing out of all the tables the World Port Index data database. 
Data Loading: 
The data loading was done with Python, using. Two python libraries sqlalchemy and Psycopg2 was installed and used to interact with already created PostgreSQL databases. sqlalchemy import create_engine was used to established Database connection to  load the dataframe named (table_result) to PostgreSQL databases using the to_sql function to write the table_result DataFrame to a table named 'Wpi Data' in the connected database.
SQL Queries analysis and result Explanation
The PostgreSQL database acts as a centralized repository for easy access and analysis. Two python libraries, import psycopg2 and import pandas as pd, was used established Database connection, to read the table named 'Wpi Data' in the to PostgreSQL databases enable running SQL queries within Jupyter Notebok Environment, with the help of ipython-sql psycopg2 python libraries. 
Using this connection, provide the ability to run SQL queries directly within the Jupyter Notebook environment, thus enhancing my ability to work with databases interactively in your notebooks.
Requirements
•	Python 3.x
•	psycopg2
•	pyodbc
•	Pandas
•	SQLAlchemy
•	PostgreSQL
Conclusion
In In conclusion, GoFrieghts Data Migration Project, provided an overview the steps or process for extracting data from the Access database, loading it into a PostgreSQL database, and executing specific queries for analysis.
Contribution and Feedback
Contributions are welcomed to enhance and extend this EL pipeline further. Feel free to submit pull requests, raise issues, or provide feedback to help us improve the project.
