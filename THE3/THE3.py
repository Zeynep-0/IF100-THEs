user = input("Please enter usernames and passwords: ")
user1=user.split(";")
modinfo = input("Please enter last modification information: ")
modinfo1=modinfo.split(";")
digit=0
if len(user1)==len(modinfo1):
  name = input("Please enter the username: ")
  user2 = user.replace(":",";").split(";")
  pas = user2[1::2]
  if name in user2:
   password= input("Please enter the password: ")
   if password[::-1] in str(pas):
    if password[::-1] in user2[user2.index(name)+1]:
      modinfo2= modinfo.replace(" ",";").split(";")
      if int(modinfo2[user2.index(name)][0])>0:
       print("It has been more than 6 months since your last password update!")
       print("Successful login")
      elif int(modinfo2[user2.index(name)+1][0])>=6:
        print("It has been more than 6 months since your last password update!")
        print("Successful login")
      elif modinfo2[user2.index(name)+1].find("10")!=-1:
        print("It has been more than 6 months since your last password update!")
        print("Successful login")
      else:
        print("Successful login")
    else:
      print("Wrong password")
   else:
    print("Wrong password")
  else:
    print("Wrong username")
else:
  print("List length mismatch!")
