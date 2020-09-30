# SDL Assignment No-1
# Write Python code for Word count and find occurrence of word from file.

fo=open("sdl.txt",'r')
str=fo.read()
data=str.split()
counts=dict()

for i in data:
    if i in counts:
        counts[i]+=1
    else:
            counts[i]=1

w=len(str)
l=len(data)

print("Total Characters in the file is :",w)
print("Total Words in the file is :",l)
print("occurrence:",counts)

fo.close()

print("Thank you!")
