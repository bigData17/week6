from pymongo import MongoClient; import pprint

client = MongoClient()

db = client.Northwind

orders = db['orders']

order_details = db['order-details']

products = db['products']

# 1) Finding ALFKI's orders
order_ids = []

for order in orders.find({"CustomerID" : "ALFKI"}):
    order_ids.append(order['OrderID'])


# 2) Finding product ids from orders
product_ids = [] 
i=0
ord2prod = {}

while i < len(order_ids): 
    temp = []
    for  entry in order_details.find({'OrderID': order_ids[i]}):
        temp.append(entry['ProductID'])

    ord2prod[str(order_ids[i])] = temp
    i = i + 1


# 3) Finding product names from product ids
orders = list(ord2prod.keys())
product_ids = list(ord2prod.values())

#unpacking list of lists
flat_list=[]

for entry in product_ids:
    for element in entry:
        flat_list.append(element)

product_names = []
i=0        

while i < len(flat_list): 
    for entry in products.find({'ProductID' : flat_list[i]}):
        product_names.append(entry['ProductName']) 

    i = i+1

# Creating dictionary: {productID : productName}

id2name = {k:v for k,v in list(zip(flat_list, product_names))}

# Creating final dictionary: {orderID : productName}    

new_values = []

for i in range(len(orders)):
    temp = []
    for j in range(len(product_ids[i])):
        temp.append(id2name[product_ids[i][j]])

    new_values.append(temp)

order2name = {k:v for k,v in list(zip(orders, new_values))}

pprint.pprint(order2name) 