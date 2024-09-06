width = int(input("Please enter the image width in pixels: "))
lenght = int(input("Please enter the image height in pixels: "))

bitnum = 24*(width * lenght)


hs = bitnum/(64*1000)
if hs>=60:
  hm = hs/60
else:
  hm=0

if hm>=60:
  hh = hm/60
else:
  hh=0

s = bitnum/(10000000)
if s>=60:
  m = s/60
else:
  m=0

if m>=60:
  h = m/60
else:
  h=0


print("")
print("Tranmission delay of an "+ str(width) + "x" + str(lenght) + " image - " + "(" + str(bitnum) + " bits in total)")
print("Over 64 Kbps modem connection:", int(hh) ,"hour(s),", int(hm%60),"minute(s) and", format(hs%60, ".4f") ,"second(s)")
print("Over 10 Mbps ethernet connection:", int(h) ,"hour(s),", int(m%60)  ,"minute(s) and", format(s%60,".4f") ,"second(s)")
