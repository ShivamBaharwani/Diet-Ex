import datetime
from dbmanager import DBHelper
def main():
    db=DBHelper()
    while True:
        print("**********Welcome**********")
        print('Press 0 to insert new Entry')
        print('Press 1 to display perticular Entry')
        print('Press 2 to display all Entries')
        print('Press 3 to delete Entry')
        # print('Press 4 to update Entry')
        print('Press 4 to exit program')
        print()
        try:
            choice=int(input())
            if(choice==0):
                #insert user
                print("Enter details : ")
                id=input("Id : ")
                entry=input("Entry : ")
                dateTime=str(datetime.datetime.now())
                db.insert_user(id,entry,dateTime)
                pass
            elif(choice==1):
                #display perticular user
                id=int(input("Enter UserId: "))
                db.fech(id)
                pass
            elif(choice==2):
                #display user
                db.fech_all()
                pass
            elif choice==3:
                #delete user
                id=int(input("Enter UserId: "))
                db.delete(id)
                pass
            # elif choice==4:
            #     #update user
            #     print("Enter details : ")
            #     id=input("Id : ")
            #     entry=input("Name : ")
            #     dateTime=str(datetime.datetime.now())
            #     db.update(id,entry,dateTime)
            #     pass
            elif choice==4:
                break
            else:
                print("Invalid input! try again")
        except Exception as e:
            print(e)
            print("Invalid Details! try again")

if __name__=="__main__":
    main()