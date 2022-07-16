from pymongo import MongoClient
from bson.objectid import ObjectId

def run_actions():
    print("-----------------------------")
    print("-- Actions ------------------")
    print("-----------------------------")
    print("I : Insert new record")
    print("U : Update one record")
    print("D1 : Delete by name")
    print("D2 : Delete by Id")
    print("G : Get ny name")
    print("R : Read all record")
    print("C : Count all record")
    print("Q : Quit")
    action = input("Please Select Your Action:").upper()

    client = MongoClient("mongodb://localhost:27017");
    db = client["PythonTest"]
    collection = db["Users"]

    if action == "I":
        name = input("Please Input name:")
        lname = input("Please Input last name:")
        age = input("Please Input age:")
        item1 = {"name": name, "lname": lname, "age": int(age)}
        collection.insert_one(item1)
        print("Data inserted in python")
    elif action == "U":
        id = input("Please Input id:")
        new_name = input("Please Input new name:")
        new_lname = input("Please Input new last name:")
        new_age = input("Please Input new age:")
        collection.update_one({"_id": ObjectId(id)}, {"$set": {"name": new_name, "lname": new_lname, "age": int(new_age)}})
    elif action == "D1":
        name = input("Please Input name:")
        res = collection.delete_many({"name": name})
        print(str(res.deleted_count) + " items deleted")
    elif action == "D2":
        id = input("Please Input id:")
        res = collection.delete_one({"_id": ObjectId(id)})
        print(str(res.deleted_count) + " items deleted")
    elif action == "G":
        name = input("Please Input name:")
        results = collection.find({"name": name})
        if len(list(results.clone())) != 0:
            for result in results:
                print(result)
        else:
            print("Item not found")
    elif action == "R":
        results = collection.find({})
        for result in results:
            print(result)
    elif action == "C":
        count = collection.count_documents({})
        print("Total records: " + str(count))
    elif action == "Q":
        print("Good bye..")
        return False
    else:
        print("Wrong command ... ")
    return True


while (True):
    if not run_actions():
        break
