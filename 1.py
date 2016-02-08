import sys
a=0
for arg in sys.argv[1:]:
    if len(arg)%3==0:
        a+=1
print(a)
