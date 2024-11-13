#file = open("file1.txt","r")
#print(file.read())
#file.close


f = open("file1.txt","a")
f.write("\nThis is the last day of our Training in Python")
f.close
f = open("file1.txt","r")
print(f.read())
f.close
