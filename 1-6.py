ms=int(input("input math score"))
es=int(input("input englush score"))
if ms>100 or es>100 or ms<0 or es<0:
    print("error")
elif ms>=90 and es>=90:
    print("perfact")
elif ms>=90 or es>=90:
    print("keep working")
else:
    print("bad")
      
      