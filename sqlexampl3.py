import mysql.connector

# Replace with your MySQL database credentials
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
database="mydatabase"
)
# Create a cursor to execute SQL queries
cursor = db_connection.cursor()
# Example of creating a table
create_table_query = """
CREATE TABLE test_table(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
"""
cursor.execute(create_table_query)
db_connection.commit()
