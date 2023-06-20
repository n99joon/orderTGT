import mysql .connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="HOWgreatthouart75@*%",
    database="mydatabase"
)

#Replace `yourusername`, `yourpassword`, and `yourdatabase` with the appropriate values for your MySQL setup.
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#This creates a new table named `customers` with three columns: `id`, `name`, and `address`
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

#This code inserts a new customer record into the `customers` table with the name "John" and the address 
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

#This code selects all the rows from the `customers` table and retrieves the data using the `fetchall()` method of the cursor object. It then prints the data to the console.

mydb.close()

#This closes the connection to the MySQL database.
