# 📘 Assignment: Python Persistence with SQLite

## 🎯 Objective

Build a Python application that stores and manages data in a SQLite database, using SQL commands for create, read, update, and delete operations.

## 📝 Tasks

### 🛠️ Database Schema and Setup

#### Description
Create a SQLite database file and define a table schema that stores records for the assignment resource.

#### Requirements
Completed program should:

- Use Python's built-in `sqlite3` module
- Create or open a SQLite database file
- Define a table with appropriate columns and data types
- Ensure the table is created only once when the program starts

### 🛠️ Insert and Query Data

#### Description
Add new records to the database and read saved records back into Python.

#### Requirements
Completed program should:

- Insert at least one record into the table
- Read all records and print them in a readable format
- Read a single record by ID and print the result
- Use parameterized queries to protect against SQL injection

### 🛠️ Update, Delete, and Error Handling

#### Description
Implement record updates and deletes, and handle cases where a record is not found.

#### Requirements
Completed program should:

- Update an existing record by ID
- Delete a record by ID
- Commit changes to the database after each write operation
- Handle missing record cases with an appropriate message or exception
