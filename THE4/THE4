books= input("Please enter the book database: ")

if "," not in books:
  print("Invalid option!")
elif books.count(",")%3 != 0:
  print("Length mismatch in the entries!")
else:
  books1= books.split("$")
  books2= books.replace("$",",")
  if len(set(books1))!=len(books1):
    print("There are duplicated items in the given database!")
  else:
    print("Please select an option:")
    print("1) Display an author's average book sales")
    print("2) Display the book with the highest sales")
    print("3) Display the year that saw the greatest number of books published")
    choice = input("Please enter your choice: ")
    if choice=="1":
      au = input("Please enter an author name: ")
      books2 = books2.split(",")
      if au in books2:
        count= books2.count(au)
        sum=0
        for i in books1:
          book_info = i.split(",")
          if str(book_info[1]) == str(au):
            sales_per_book = int(book_info[3])
            sum += sales_per_book
        avg=int(sum)/count
        print("Avg. sales per book by",au,"is",format(avg,".2f"))
      else:
        print(au,"does not appear in the given database!")
    elif choice=="2":
     books2= books2.split(",")
     name=books2[3::4]
     max=0
     for i in name:
      if int(max)<int(i):
        max=i
     idxx= books2.index(max)
     print("The book with the all-time highest sales is",books2[idxx-3])
    elif choice == "3":
      books2= books2.split(",")
      years=books2[2::4]
      year_count= [ ]
      for i in years:
        cnt=years.count(i)
        year_count.append(cnt)
      booknum= max(year_count)
      year=years[year_count.index(booknum)]
      print("The year that saw the greatest number of books published is", year,"with", booknum,"books in total")
    else:
      print("Invalid option!")
