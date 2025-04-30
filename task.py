import sys
import json 
import datetime

with open('test.json', 'r') as file:
    data = json.load(file)

tasks = data["tasks"]

if len(sys.argv) == 2:

    if sys.argv[1] == "list":
        print("\nAll Tasks")
        print("-----------")
        index = 1
        for task in tasks:
            print(str(index) + ": " + task["description"])
            index += 1 
        print("\n")

else:

    if sys.argv[1] == "add":
        tasks.append({
                "id": len(tasks) + 1,
                "description": sys.argv[2],
                "status": "todo",
                "createdAt": datetime.datetime.now(),
                "updatedAt": ""
            })
        print("\nAdded '" +  sys.argv[2] + "' to your task list!\n")

    elif sys.argv[1] in ["update", "delete"]:
        update_id = sys.argv[2]

        # we can't assume that the json's ids are always in order (even tho they will be)
        updated_task = {}
        index = 1
        for task in tasks:
            if task["id"] == update_id:
                updated_task = task
                break
            index += 1

        if sys.argv[1] == "update":
            updated_task["description"] = sys.argv[3]
            print("\nUpdated index " + str(update_id) + " to '" + sys.argv[3] + "'!\n")
        else:
            tasks.pop(index - 1)
            print("\nRemoved '" + updated_task["description"] + "' from your task list\n")

    elif sys.argv[1] in ["mark-in-progress", "mark-done"]:
        search_id = sys.argv[2]
        index = 1
        for task in tasks:
            if task["id"] == search_id:
                updated_task = task
                break
            index += 1

        if sys.argv[1] == "mark-in-progress":
            updated_task["status"] = "in progress"
            print("\nUpdated " + updated_task["description"] + " to 'in progress'!\n")
        else:
            updated_task["status"] = "done"
            print("\nUpdated " + updated_task["description"] + " to 'done'!\n")


    elif sys.argv[1] == "list" and sys.argv[2] == "done":
        print("\nCompleted Tasks")
        print("-----------------")

        index = 1
        for task in tasks:

            if task["status"] == "done":
                print(str(index) + ": " + task["description"])
            index += 1 
        
        print("\n")

    elif sys.argv[1] == "list" and sys.argv[2] == "todo":
        print("\nTasks to Start")
        print("----------------")

        index = 1
        for task in tasks:

            if task["status"] == "todo":
                print(str(index) + ": " + task["description"])
            index += 1 
        
        print("\n")

    elif sys.argv[1] == "list" and sys.argv[2] == "in-progress":
        print("\nTasks to In Progress")
        print("----------------------")

        index = 1
        for task in tasks:

            if task["status"] == "in progress":
                print(str(index) + ": " + task["description"])
            index += 1 

        print("\n")






