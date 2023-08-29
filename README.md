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
   ```python
   from sqlalchemy import create_engine
   from time import time
   import pyodbc
   import pandas as pd
