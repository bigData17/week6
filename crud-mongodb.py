import pymongo
from pymongo import MongoClient

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.CustomerData

# The following function insert the data to mongoDB 
def insert():
        customerId = input('Enter Customer ID : ')
        customerName = input('Enter Customer Name : ')
        customerAge = input('Enter Customer Age : ')
        customerPhone = input('Enter Customer Phone Number : ')
        db.Customers.insert_one(
	        {
		    "id": customerId,
	            "name":customerName,
		    "age":customerAge,
		    "phoneNr":customerPhone
	        })
        print('\nInserted data successfully\n')

# The following function update a record in mongoDB
def update():
        id = input('Enter new id to update : ')
        name = input('Enter new name to update: ')
        age = input('Enter new age to update: ')
        phone = input('Enter new phone number to update: ')
        
        db.Customers.update_one(
	        {"id": id},
	        {
		    "$set": {
		    "name":name,
		    "age":age,
		    "phoneNr":phone
		    }
	        }
	    )
        print("\nRecords updated successfully\n")	

# The following function read a record from mongoDB
def read():
	    customerCol = db.Customers.find()
	    print ('\n All data from CustoemerData Database \n')
	    for customer in customerCol:
	        print(customer)


# The following function delete a record from mongoDB
def delete():
        id = input('\nEnter employee id to delete\n')
        db.Customers.delete_many({"id":id})
        print('Deletion successful\n')

def main():
    while(1):
	    # you have to choose one option to do CRUD operations
        selection = input('Select 1 to insert, 2 to update, 3 to read, 4 to delete\n')
    
        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            print('delete')
            delete()
        else:
            print('\n Selection is invalid \n')

if __name__ == "__main__": main()
