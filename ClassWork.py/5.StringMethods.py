s=input()

# Case Cnversion Methods

c=s.upper()  #covert all charaters into Upper
print(c)
b=s.lower()   ##covert all charaters into Lower
print(b)
a=s.capitalize()
print(a)       #covert first charater in word  into Upper
d=s.title()
print(d)     #covert first letters in word  into Upper
e=s.swapcase()
print(e)   #covert big letters into small and small to big
f=s.casefold()
print(f)

# #Alignment and Formatting Methods

g=s.center(30,"*")
print(g)
h=s.ljust(30,"=")
print(h)
i=s.rjust(30,"-")
print(i)
j=s.zfill(5)
print(j)

# #Search and Find Methods

k=s.find('m')      #find the value and return its index value
print(k)       #0
l=s.rfind("n")     #find the value and return its index value (moves from right)
print(l)       #4
m=s.index("L")     #returns the index values
print(m)       #1
n=s.rindex("s")    #returns the index values(from right side)
print(n)        #2
o=s.count("L")     #it tells the count of the character
print(o)       #1




# #Replace and Modify Methods

aa=input()
ss=aa.replace('a','*')
print(ss)
#dd=aamLs
# aa=input()
# v="aeiou"
# for v in aa:
#     aa=aa.replace(v,"*")
# print(aa)

# a="12394"
# c=len(a)
# print(c)
# d=max(a)
# print(d)
# e=ord("2")
# print(e)
# dd=min(a)
# print(dd)
# ee=chr(11111)
# print(ee)
# r=sorted(a)
# print(r)