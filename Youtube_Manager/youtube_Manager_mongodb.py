from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubepy:youtubepy@test.s6m5xin.mongodb.net/")
# Not a good idea to include id and password in code files

db = client["ytmanager"]
video_collection = db["video"]

print(video_collection)

def list_video():
    for video in video_collection.find():
        print(f"ID : {video['_id']}, Name : {video['name']} and Time : {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})

def update_video(video_id,new_name,new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set" : {"name" : new_name, "time" : new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({'_id' : ObjectId(video_id)})


def main():
    while True:
        print("\n Welcome to Youtube App")
        print("1. List all Videos : ")
        print("2. Add a Video : ")
        print("3. Update a Video : ")
        print("4. Delete a Video : ")
        print("5. Exit from the App : ")

        choice = input("Enter your choices : ")

        if choice == '1':
            print()
            print("*" * 70)
            list_video()
            print()
            print("*" * 70)
        elif choice == '2':
            name = input("Enter the video name : ")
            time = input("Enter the video Time : ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video Id : ")
            name = input("Enter the video name to update : ")
            time = input("Enter the video time : ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter the video id to Delete : ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
