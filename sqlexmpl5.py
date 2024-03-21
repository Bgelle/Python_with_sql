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
# Example of updating data in the table
update_data_query = """
UPDATE test_table SET age = %s WHERE name = %s
"""
new_age = 31
name_to_update = "John Doe"
cursor.execute(update_data_query, (new_age, name_to_update))
db_connection.commit()
