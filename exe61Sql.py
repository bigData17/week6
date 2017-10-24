import sqlite3                                  # Import necessary package
conn = sqlite3.connect('northwind.db')          # Connect to the chosen database
conn.text_factory = lambda x: str(x, 'latin1')  # Make it accept special charecters
c = conn.cursor()

for row in c.execute(" SELECT Products.ProductID, Products.ProductName, B.OrderID \
    FROM Products INNER JOIN (SELECT 'Order Details'.OrderID,'Order Details'.ProductID\
    FROM 'Order Details' INNER JOIN (SELECT Orders.OrderID FROM Orders WHERE \
    Orders.CustomerID='ALFKI') as A WHERE 'OrderDetails'.OrderID=A.OrderID) as B WHERE\
    Products.ProductID=B.ProductID"):
    print(row)
