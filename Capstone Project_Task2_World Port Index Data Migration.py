#!/usr/bin/env python
# coding: utf-8

# ### Data Engineering Capstone Project 2: World Port Index Data Migration

# #### Introduction/Project Overview.
#    * GoFrieghts, a prominent logistics company, has enlisted your expertise as a Data Engineer. 
#    * Your remit involves migrating World Port Index data from an archaic Access database to a contemporary PostgreSQL    relational database. The resultant analysis will facilitate the creation of data marts.
# #### The objective of this Project.  
#    * Construct an Extract Load (EL) pipeline in Python to transition the World Port Index data from the Access              database to PostgreSQL.
# #### Extraction Process,
#    * start with installing the necessary python modules, make the connection string to access the microsoft access          database, and read and printing out all the table the World Port Index data database.
# 

# In[1]:


from sqlalchemy import create_engine
from time import time
import pyodbc
import pandas as pd


# In[2]:


def get_accessbase_conn():
    return pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/LENOVO/Desktop/DATA_ENG/PUB150/WPI.mdb')

conn = get_accessbase_conn()
cursor = conn.cursor()

# Get the list of table names
table_names = [table.table_name for table in cursor.tables(tableType="TABLE")]

# Print the table names
for name in table_names:
    print(name)


# ## Read Wpi Data Table Pandas Dataframe
# #### Read Table name  "Wpi Data" from MS-Access database using conn = get_accessbase_conn()

# In[3]:


def query_accessdb_table(query, conn):
    table_result = pd.read_sql(query, conn)
    return table_result

query = '''
SELECT * FROM "Wpi Data"
'''

table_result = query_accessdb_table(query, conn)
table_result


# ## Loading Table_Result Dataframe to Postgres Database
# #### Using sqlalchemy import create_engine to load the dataframe to Postgres db

# In[5]:


from sqlalchemy import create_engine

def save_to_database(table_result):
    engine = create_engine('postgresql://postgres:Mysong123@localhost:5432/World_Port_Index')
    table_result.to_sql('Wpi Data', con=engine, schema='public', if_exists='replace')

# Call the function and pass the 'table_result' DataFrame as an argument
save_to_database(table_result)


# ### Make a Connection to connect to the PostgreSQL database
# ----this connection will be use to run query on the database---

# In[4]:


#this connection will be use to run query on the  PostgreSQL database
import psycopg2
import pandas as pd

def connect_to_database():
    conn = psycopg2.connect(
        dbname="World_Port_Index",
        user="postgres",
        password="Mysong123",
        host="localhost",
        port="5432"
    )
    return conn

# Call the function to establish a connection
connection = connect_to_database()


# ### Runing  SQL Query on the database using psycopg2 connection

# In[29]:


# This connection will be used to run queries on the PostgreSQL database
import psycopg2
import pandas as pd

def connect_to_database():
    conn = psycopg2.connect(
        dbname="World_Port_Index",
        user="postgres",
        password="Mysong123",
        host="localhost",
        port="5432"
    )
    return conn

# Call the function to establish a connection
connection = connect_to_database()

# This query is to see the table in just 3 rows.
# Run SQL query
sql_query = 'SELECT * FROM "Wpi Data" LIMIT 3'  
df_Wpi = pd.read_sql_query(sql_query, connection) 

# Close the connection
connection.close() 

# Show the dataframe
print(df_Wpi)


# ### TASK 2: Q1:
# #### What are the 5 nearest ports to Singapore's JURONG ISLAND port? (country ='SG',port_name = 'JURONG ISLAND').Your answer should include the columns port_name and distance_in_meters only.

# In[ ]:





# In[5]:


import psycopg2
import pandas as pd

def find_nearest_ports_to_jurong_island():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="World_Port_Index",
        user="postgres",
        password="Mysong123",
        host="localhost",
        port="5432"
    )

    # Run SQL query to find the 5 nearest ports to JURONG ISLAND
    sql_query = '''
    SELECT "Main_port_name",
    (
        6371000 * 
        acos(
            cos(radians(1)) * cos(radians("Latitude_degrees")) * cos(radians("Longitude_degrees") - radians(103.98765)) +
            sin(radians(1)) * sin(radians("Latitude_degrees"))
        )
    ) AS distance_in_meters
FROM
    "Wpi Data"
WHERE
    "Wpi_country_code" = 'SG'
    AND "Main_port_name" != 'JURONG ISLAND'
ORDER BY
    distance_in_meters
LIMIT 5;
    '''

    # Execute the query and fetch the result into a DataFrame
    Task2_Q1 = pd.read_sql_query(sql_query, conn)

    # Close the connection
    conn.close()
    
    return Task2_Q1

# Call the function to find and display the nearest ports to JURONG ISLAND
nearest_ports_df = find_nearest_ports_to_jurong_island()
print(nearest_ports_df)


# ### TASK 2: Q2:
# #### Which country has the largest number of ports with a cargo_wharf? Your answer should include the columns country and port_count only.

# In[19]:


import psycopg2
import pandas as pd

def country_with_largest_cargo_wharf_ports():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="World_Port_Index",
        user="postgres",
        password="Mysong123",
        host="localhost",
        port="5432"
    )

    # Run SQL query to find which country has the largest number of ports with a cargo_wharf.
    sql_query = '''
    SELECT 
        "Wpi_country_code" as country,
        count("Main_port_name") as port_count 
    FROM 
        "Wpi Data"  
    GROUP BY 
        "Wpi_country_code" 
    ORDER BY 
        port_count DESC 
    LIMIT 1
    '''

    # Execute the query and fetch the result into a DataFrame
    Task2_Q2 = pd.read_sql_query(sql_query, conn)

    # Close the connection
    conn.close()
    
    return Task2_Q2

# Call the function to find and display the country with the largest number of cargo wharf ports
largest_cargo_wharf_country = country_with_largest_cargo_wharf_ports()
print(largest_cargo_wharf_country)


# ### TASK 2: Q3:
# #### You receive a distress call from the middle of the North Atlantic Ocean. The person on the line gave you a coordinates of lat: 32.610982, long: -38.706256 and asked for the nearest port with provisions, water, fuel_oil and diesel. Your answer should include the columns country, port_name, port_latitude and port_longitude only.

# In[24]:


import psycopg2
import pandas as pd

def find_nearest_provision_ports(latitude, longitude):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="World_Port_Index",
        user="postgres",
        password="Mysong123",
        host="localhost",
        port="5432"
    )

    # Run SQL query to find the nearest port with provisions, water, fuel_oil, and diesel.
    sql_query = f'''
    SELECT "Wpi_country_code" AS country, "Main_port_name" AS port_name, "Latitude_degrees" AS port_latitude, "Longitude_degrees" AS port_longitude,
        (6371000 * 
            acos(
                cos(radians({latitude})) * cos(radians("Latitude_degrees")) * cos(radians("Longitude_degrees") - radians({longitude})) +
                sin(radians({latitude})) * sin(radians("Latitude_degrees"))
            )
        ) AS distance_in_meters
    FROM "Wpi Data"
    WHERE "Supplies_provisions" = 'Y' AND "Supplies_water" = 'Y'
    AND "Supplies_fuel_oil" = 'Y' AND "Supplies_diesel_oil" = 'Y'
    ORDER BY distance_in_meters
    LIMIT 1;
    '''

    # Execute the query and fetch the result into a DataFrame
    Task2_Q3 = pd.read_sql_query(sql_query, conn)

    # Close the connection
    conn.close()
    
    return Task2_Q3

# Call the function to find and display the nearest port with provisions, water, fuel_oil, and diesel
latitude = 32.610982
longitude = -38.706256
nearest_provision_ports = find_nearest_provision_ports(latitude, longitude)
print(nearest_provision_ports)


# ### End

# In[ ]:




