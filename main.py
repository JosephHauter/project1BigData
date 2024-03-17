
import json
from pymongo import MongoClient
import random
#connects to server
client = MongoClient('mongodb://localhost:27017/')

# create database
db = client['mydatabase']

# create collection inside database
collection = db['mycollection']

# Task 1
# opens json
# with open('city_inspections.json', 'r') as f:
#     for line in f:
#         # load every line
#         document = json.loads(line)

#         # remove the '$oid' field from the '_id' field
#         document['_id'] = document['_id']['$oid']

#         # insert into collection
#         collection.insert_one(document)

# Task 2
# count the total number of inspections
# total_inspections = collection.count_documents({})

# # count the number of inspections performed in 2015
# inspections_2015 = collection.count_documents({"date": {"$regex": "2015"}})

# # count the number of inspections performed in 2016
# inspections_2016 = collection.count_documents({"date": {"$regex": "2016"}})

# print(f"Total inspections: {total_inspections}")
# print(f"Inspections in 2015: {inspections_2015}")
# print(f"Inspections in 2016: {inspections_2016}")

# Task 3
# # ask user for business name
# business_name = input("Please enter a business name: ")

# # search for a document that matches the provided business name
# document = collection.find_one({"business_name": business_name})

# if document is not None:
#     # check if the business has a violation
#     if document['result'] == 'Violation Issued':
#         print(f"The business '{business_name}' has a violation.")
#     else:
#         print(f"The business '{business_name}' does not have a violation.")
# else:
#     print("Business Not found.")


# Task 4
# # find businesses with violations
# violations_brooklyn = collection.find({"$and": [{"address.city": "BROOKLYN"}, {"result": "Violation Issued"}]})
# violations_bronx = collection.find({"$and": [{"address.city": "BRONX"}, {"result": "Violation Issued"}]})

# # count the number of violations
# count_brooklyn = collection.count_documents({"$and": [{"address.city": "BROOKLYN"}, {"result": "Violation Issued"}]})
# count_bronx = collection.count_documents({"$and": [{"address.city": "BRONX"}, {"result": "Violation Issued"}]})

# # calculate the difference in count
# difference = abs(count_brooklyn - count_bronx)

# # print the names and addresses of the first five businesses in Brooklyn and Bronx
# print("First five businesses with violations in Brooklyn:")
# for i, business in enumerate(violations_brooklyn.limit(5)):
#     print(f"{i+1}. {business['business_name']}, {business['address']}")

# print("\nFirst five businesses with violations in Bronx:")
# for i, business in enumerate(violations_bronx.limit(5)):
#     print(f"{i+1}. {business['business_name']}, {business['address']}")

# # print the number of violations and the difference in count
# print(f"\nNumber of violations in Brooklyn: {count_brooklyn}")
# print(f"Number of violations in Bronx: {count_bronx}")
# print(f"Difference in count: {difference}")

# Task 5
zip_code = input("Please enter a zip code: ")
# convert to int
zip_code = int(zip_code)
# find all businesses 
businesses = list(collection.find({"address.zip": zip_code}))
# check if any businesses were found
if businesses:
    # print the total number of businesses
    print(f"Total number of businesses in zip code {zip_code}: {len(businesses)}")

    # randomly select five businesses
    selected_businesses = random.sample(businesses, min(5, len(businesses)))

    # print the names of the selected businesses
    print("Randomly selected businesses:")
    for business in selected_businesses:
        print(business['business_name'])
else:
    print("zip-code Not found.")