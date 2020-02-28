class User:
    def name(self,First_Name,Last_name):
        self.First_Name=First_Name
        self.Last_Name=Last_name
        return

    First_Name=input("Enter your first name:")
    Last_name=input("Enter your last name:")
    First_Name=(First_Name[::-1])
    print(First_Name)
    Last_name=(Last_name[::-1])
    print(Last_name)
    
user=User()




