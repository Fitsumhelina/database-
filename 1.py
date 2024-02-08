
'''''
users =[]
user={}
def add_user():
  name= input("enter your name ")
  age =input ("enter your age ")
  city =input ("enter your city ")
  user ["name"]=name
  user ["age"]=age
  user ["city"]=city
  return user

def display_user():
  users .append(user)
  print (users , "\n")

def delate_user():
   print ( "enter the name you want to delate ")
   name_del= input("enter your name ")
   for user in users:
      if user["name"] == name_del:
         users.remove(user)
         print (users, "\n")
        

   



while True :
  print("1. open registration\n2. acess data   \n3.delate user data \n4.exit \n")
  choice  = input ("enter your choose  ")

  if choice  =='1':
     add_user()

  elif  choice =='2':
     display_user()

  elif  choice =='3':
     delate_user()

  elif choice  =='4':
     break  

'''



# Define the User class
class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Define the UserManagement class
class UserManagement:
    def __init__(self):
        print ("welcome to user managment system")
        self.user={}

    def create_user(self, name, email):
          user1 = user(name, email)
          self.user [name]=user1
          
          return user

    def read_user(self, name):
        print(self.user[name].name , self.user[name].email)




    def update_user(self, name, new_email):
        # Implement user updating method] 
        self.user [name].email = new_email
        return user


    def delete_user(self, username):
        # Implement user deletion method
        del self.user[username]
        return user
    
usermgt = UserManagement()
while True:
  # Implement the menu
        print("1. open registration\n2. read data   \n3.delate user data \n4.update_user   \n5.exit \n")
        choice  = input ("enter your choose  ")
        if choice  =='1':
         name= input("enter your name ")
         email =input ("enter your email ")
         usermgt.create_user(name, email)
        elif  choice =='2':
            name= input("enter your name ")
            usermgt.read_user(name)
        elif  choice =='3':
            name= input("enter your name ")
            usermgt.delete_user(name)
        elif  choice =='4':
            name= input("enter your name ")
            new_email =input ("enter your new email ")
            usermgt.update_user(name , new_email)
        elif choice  =='5':
            break
