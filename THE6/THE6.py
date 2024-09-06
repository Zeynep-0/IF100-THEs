startyear = int(input("Enter the starting year: "))
endyear = int(input("Enter the end year: "))
netxt= open("netflix.txt","r")

movies=[]
countries=[]
years=[]
actors=[]
thractor=[]
thr_actor=[]

first_line = netxt.readline()
remaining_lines = netxt.readlines()
for i in remaining_lines:
  i=i.split("\t")
  movies.append(i[0])
  actors.append(i[2])
  countries.append(i[3])
  years.append(int(i[4]))

if endyear<startyear:
  print("The starting year must be less than or equal to the end year!")
else:
  country = input("Enter the country: ")
  while country not in countries:
    print(country,"does not exist in the database!")
    country = input("Enter the country: ")
  thr=int(input("Enter the threshold value: "))
  for i in range(len(years)):
    if endyear>=years[i]>=startyear:
      if country in countries[i]:
        actors[i]=actors[i].split(",")
        for i in actors[i]:
          thractor.append(i.strip())
  for i in thractor:
    cnt=thractor.count(i)
    if cnt>=thr:
      thr_actor.append(i)
  if len(thr_actor)==0:
    print("No actors found!")
  else:
    dictionary={}
    sum=1
    print("The list of actors (alphabetically ordered) who played in at least",thr,"movies between", startyear, "and", endyear)
    for i in range(len(thr_actor)):
      count=thr_actor.count(thr_actor[i])
      dictionary[thr_actor[i].strip()]=count
    sorted_dict = dict(sorted(dictionary.items()))
    for b in sorted_dict:
      print(sum,") ", b.strip()," (",sorted_dict.get(b)," movies)",sep="")
      sum=sum+1
