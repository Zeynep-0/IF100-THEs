board = input("Enter the board layout: ")

while "K" not in board or "B" not in board:
  print("Missing pieces!")
  board = input("Enter the board layout: ")
board= board.replace("@", "| ")
board=board.replace("B","|B")
board=board.replace("K","|K")
board=board.replace(",","")
board_line=board.split(";")

idx4= board.index("B")
b_line= int((idx4/17)+1)
bsline= board_line[b_line-1]
b_loc=bsline.find("B")
a=1
idx6= board.index("K")
k_line= int((idx6/17)+1)
ksline= board_line[k_line-1]
k_loc=ksline.find("K")

def bloc(c,b):
  if 16>b>0:
   if b==k_loc and c==k_line-1:
    return 5
sum=0
for i in board_line:
  plus= sum-(b_line-1)
  if b_loc+2*plus>0 and b_loc-2*plus>0:
    if plus<0:
      if bloc(sum,b_loc+2*plus)==5 or bloc(sum,b_loc-2*plus)==5:
        a=2
        if bloc(sum,b_loc+2*plus)==5:
          board_line[sum]= i[:b_loc+2*plus]+"K"+i[b_loc+2*plus+1:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:]
          if len(board_line[sum])!=16:
           board_line[sum]= i[:b_loc+2*plus]+"K"+i[b_loc+2*plus+1:]
        else:
          board_line[sum]= i[:b_loc+2*plus]+"+"+i[b_loc+2*plus+1:b_loc-2*plus]+"K"+i[b_loc-2*plus+1:]
          if len(board_line[sum])!=16:
           board_line[sum]= i[:b_loc+2*plus]+"+"+i[b_loc+2*plus+1:]
      else:
        board_line[sum]= i[:b_loc+2*plus]+"+"+i[b_loc+2*plus+1:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:]
        if len(board_line[sum])!=16:
          board_line[sum]= i[:b_loc+2*plus]+"+"+i[b_loc+2*plus+1:]
    elif plus>0:
      if bloc(sum,b_loc+2*plus)==5 or bloc(sum,b_loc-2*plus)==5:
        a=2
        if bloc(sum,b_loc+2*plus)==5:
          board_line[sum]= i[:b_loc-2*plus]+"K"+i[b_loc-2*plus+1:b_loc+2*plus]+"+"+i[b_loc+2*plus+1:]
          if len(board_line[sum])!=16:
           board_line[sum]= i[:b_loc-2*plus]+"K"+i[b_loc-2*plus+1:]
        else:
          board_line[sum]= i[:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:b_loc+2*plus]+"K"+i[b_loc+2*plus+1:]
          if len(board_line[sum])!=16:
           board_line[sum]= i[:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:]
      else:
        board_line[sum]=i[:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:b_loc+2*plus]+"+"+i[b_loc+2*plus+1:]
        if len(board_line[sum])!=16:
          board_line[sum]= i[:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:]
  elif b_loc+2*plus>0:
    if plus<0:
      if bloc(sum,b_loc+2*plus)==5 or bloc(sum,b_loc-2*plus)==5:
        a=2
        if bloc(sum,b_loc+2*plus)==5:
          board_line[sum]= i[:b_loc+2*plus]+"K"+i[b_loc+2*plus+1:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:]
          if len(board_line[sum])!=16:
           board_line[sum]= i[:b_loc+2*plus]+"K"+i[b_loc+2*plus+1:]
        else:
          board_line[sum]= i[:b_loc+2*plus]+"+"+i[b_loc+2*plus+1:b_loc-2*plus]+"K"+i[b_loc-2*plus+1:]
          if len(board_line[sum])!=16:
           board_line[sum]= i[:b_loc+2*plus]+"K"+i[b_loc+2*plus+1:]
      else:
        board_line[sum]= i[:b_loc+2*plus]+"+"+i[b_loc+2*plus+1:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:]
        if len(board_line[sum])!=16:
          board_line[sum]= i[:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:]
    elif plus>0:
      if bloc(sum,b_loc+2*plus)==5 or bloc(sum,b_loc-2*plus)==5:
        a=2
        if bloc(sum,b_loc+2*plus)==5:
          board_line[sum]= i[:b_loc+2*plus]+"K"+i[b_loc+2*plus+1:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:]
          if len(board_line[sum])!=16:
           board_line[sum]= i[:b_loc+2*plus]+"K"+i[b_loc+2*plus+1:]
        else:
          board_line[sum]= i[:b_loc+2*plus]+"+"+i[b_loc+2*plus+1:b_loc-2*plus]+"K"+i[b_loc-2*plus+1:]
          if len(board_line[sum])!=16:
           board_line[sum]= i[:b_loc+2*plus]+"K"+i[b_loc+2*plus+1:]
      else:
        board_line[sum]=i[:b_loc+2*plus]+"+"+i[b_loc+2*plus+1:]
        if len(board_line[sum])!=16:
          board_line[sum]= i[:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:]
  elif 27>b_loc-2*plus>0:
    if plus<0:
      if bloc(sum,b_loc-2*plus)==5:
        a=2
        board_line[sum]= i[:b_loc-2*plus]+"K"+i[b_loc-2*plus+1:]
        if len(board_line[sum])!=16:
          board_line[sum]= i[:b_loc-2*plus]+"K"
      else:
        board_line[sum]= i[:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:]
        if len(board_line[sum])!=16:
          board_line[sum]= i[:b_loc-2*plus]+"+"
    elif plus>0:
      bloc(sum,b_loc+2*plus)
      bloc(sum,b_loc-2*plus)
      if bloc(sum,b_loc+2*plus)==5 or bloc(sum,b_loc-2*plus)==5:
        a=2
        if bloc(sum,b_loc+2*plus)==5:
          board_line[sum]= i[:b_loc+2*plus]+"K"+i[b_loc+2*plus+1:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:]
          if len(board_line[sum])!=16:
           board_line[sum]= i[:b_loc-2*plus]+"K"
        else:
          board_line[sum]= i[:b_loc+2*plus]+"+"+i[b_loc+2*plus+1:b_loc-2*plus]+"K"+i[b_loc-2*plus+1:]
          if len(board_line[sum])!=16:
           board_line[sum]= i[:b_loc-2*plus]+"K"
      else:
        board_line[sum]=i[:b_loc-2*plus]+"+"+i[b_loc-2*plus+1:]
        if len(board_line[sum])!=16:
          board_line[sum]= i[:b_loc-2*plus]+"+"
  sum= sum+1

addk=k_loc-2
downk=k_loc+2
if a == 2:
  if k_line-b_line<0:
   change= board_line[:k_line-1]
   change= change[::-1]
   if k_loc-b_loc>0:
    for p in range(len(change)):
     i=change[p]
     plus_search=i[downk]
     if "+" in plus_search:
      i=i[:downk]+" "+i[downk+1:]
      change[p]=i
      downk= downk+2
    board_line[:k_line-1]=change[::-1]
   else:
    for p in range(len(change)):
     i=change[p]
     plus_search=i[addk]
     if "+" in plus_search:
      i=i.replace("+"," ",1)
      change[p]=i
      addk= addk-2
    board_line[:k_line-1]=change[::-1]
  elif k_line-b_line<0:
    change= board_line[k_line-1:]
    if k_loc-b_loc<0:
      for p in range(len(change)):
        i=change[p]
        plus_search=i[addk]
        if "+" in plus_search:
          i=i.replace("+"," ",1)
          change[i]=i
          addk= addk-2
    if k_loc-b_loc>0:
      for p in range(len(change)):
        i=change[p]
        plus_search=i[downk]
        if "+" in plus_search:
          i=i[:downk]+" "+i[downk+1:]
          change[p]=i
          downk= downk+2
    board_line[k_line-1:]=change

for elem in board_line:
  print("-----------------")
  elem=elem+"|"
  print(elem)
print("-----------------")

if a==2:
  print("The bishop can attack the king")
else:
  print("The king is safe")
