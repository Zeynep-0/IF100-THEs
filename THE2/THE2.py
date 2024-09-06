citizenship = input("Please enter the country for citizenship inquiry: ")

if citizenship == "USA":
  born = input("Was the applicant born in the United States or a territory of the United States? ")
  if born=="yes":
    print("The applicant is a U.S. citizen.")
  elif born=="no":
    parent = input("Was at least one of the applicant's parents a U.S. citizen? ")
    if parent == "yes":
      print("The applicant is a U.S. citizen.")
    elif parent == "no":
      print("The applicant is not a U.S. citizen.")
    else:
      print("Invalid entry! Terminating the program.")
  else:
    print("Invalid entry! Terminating the program.")

elif citizenship == "Switzerland":
  married = input("Are the applicant's parents married? ")
  if married=="yes":
    citizen=input("Is one of the parents a Swiss citizen? ")
    if citizen=="yes":
      print("The applicant is a Swiss citizen.")
    elif citizen=="no":
      print("The applicant is not a Swiss citizen.")
    else:
      print("Invalid entry! Terminating the program.")
  elif married=="no":
    mother = input("Is unmarried mother a Swiss citizen? ")
    if mother=="yes":
      print("The applicant is a Swiss citizen.")
    elif mother=="no":
      father=input("Is unmarried father a Swiss citizen? ")
      if father=="yes":
        accept=input("Does unmarried father acknowledge paternity? ")
        if accept=="yes":
          print("The applicant is a Swiss citizen.")
        elif accept =="no":
         print("The applicant is not a Swiss citizen.")
        else:
           print("Invalid entry! Terminating the program.")
      elif father=="no":
        print("The applicant is not a Swiss citizen.")
      else:
         print("Invalid entry! Terminating the program.")
    else:
       print("Invalid entry! Terminating the program.")
else:
  print("Invalid entry! Terminating the program.")
