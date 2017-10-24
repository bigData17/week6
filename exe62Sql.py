import sqlite3

conn = sqlite3.connect('northwind.db')
conn.text_factory = lambda x: str(x, 'latin1')
c = conn.cursor()

str2="SELECT X.ProductID, X.OrderID, X.c FROM (SELECT B.ProductID, B.OrderID, count(*) \
    as c FROM (SELECT 'Order Details'.ProductID, A.OrderID FROM 'Order Details' INNER \
    JOIN (SELECT Orders.OrderID FROM Orders WHERE Orders.CustomerID='ALFKI') AS A WHERE \
    A.OrderID='Order Details'.OrderID) AS B GROUP BY B.OrderID) as X WHERE X.c>1"
str3="SELECT 'Order Details'.OrderID, 'Order Details'.ProductID FROM 'Order Details' \ 
    INNER JOIN ("+str2+") as D WHERE D.OrderID='Order Details'.OrderID"
str4="SELECT Products.ProductID, Products.ProductName FROM Products INNER JOIN \ 
    ("+str3+") as E WHERE Products.ProductID=E.ProductID"

for row in c.execute(str4):
	print(row)
