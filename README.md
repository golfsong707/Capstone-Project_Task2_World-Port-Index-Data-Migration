# World Port Index Data Migration

## Table of Contents
- [Introduction/Project Overview](#introductionproject-overview)
- [Objective](#objective)
- [Instructions](#instructions)
- [How it Works](#how-it-works)
- [Data Extraction](#data-extraction)
- [Loading the Data](#loading-the-data)
- [SQL Queries Analysis and Result Explanation](#sql-queries-analysis-and-result-explanation)
- [Requirements](#requirements)
- [Conclusion](#conclusion)
- [Contribution and Feedback](#contribution-and-feedback)

## Introduction/Project Overview
GoFrieghts, a prominent logistics company, has enlisted your expertise as a Data Engineer. Your remit involves migrating World Port Index data from an archaic Access database to a contemporary PostgreSQL relational database. The resultant analysis will facilitate the creation of data marts.

## Objective
The objective of this project is to construct an Extract Load (EL) pipeline in Python to transition the World Port Index data from the Access database to PostgreSQL.

## Instructions
Construct an Extract Load (EL) pipeline in Python to transition the World Port Index data from the Access database to PostgreSQL Database, executing a specific set of SQL queries and analyzing the following:
- Find the Nearest Ports to Singapore's JURONG ISLAND.
- Find the Country with the Largest Number of Cargo Wharf Ports.
- Find the Nearest Port with Provisions, Water, Fuel, and Diesel.

## How it Works
1. Install Necessary Python Modules:
   Ensure you have the required Python modules installed. This can be achieved using the following code snippet: 
   python 3.x.x
   from sqlalchemy import create_engine
   from time import time
   import pyodbc
   import pandas as pd

## Establish Connection to Access Database:
    Create a function to establish a connection to the Microsoft Access database name WPI.mdb.
    the function also Retrieve the list of table names from the Access database and print them.

## Data Extraction
The data extraction was done with Python, using the python libraries pyodbc, which enables a connection to the Microsoft Access database, 
and thus enable  Retrieving  the list of all table names from the Access database, once that was done we procceded to exract the data from one of the table named "Wpi Data" into a pandas dataframe

## Loading the Data
To load the Wpi dataframe to postgres database, The loading was done using python sqlalchemy libraries, the import create_engine command was used to establish a database connection to postgres, and 
"to_sql" command,was used to load the DataFrame named table_result to PostgreSQL databases.

## SQL Queries Analysis and Result Explanation
The PostgreSQL database acts as a centralized repository for easy access and analysis. The python libraries psycopg2 and pandas were used to establish a database connection to read the table named 'Wpi Data' in PostgreSQL databases, Jupyter web-based interactive development environment, was used SQL queries, and analysis, to the already connected databse,thus  providing the ability to run SQL queries directly within the Jupyter Notebook environment, enhancing the ability to work with databases interactively in your notebooks.

## Requirements
    Python 3.x
    psycopg2
    pyodbc
    Pandas
    SQLAlchemy
    PostgreSQL

## Conclusion
In conclusion, the GoFrieghts Data Migration Project provides an overview of the steps or process for extracting data from the Access database, loading it into a PostgreSQL database, and executing specific queries for analysis.

## Contribution and Feedback

Contributions are welcome to enhance and extend this EL pipeline further. Feel free to submit pull requests, raise issues, or provide feedback to help us improve the project.
