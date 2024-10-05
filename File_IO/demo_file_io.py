# Reading mode "r"
f = open("E:\\Python\\prac\\File_IO\\demo.txt","r")
# data = f.read()#Can specify number of characters
line1 = f.readlines()
print(line1)
print(type(line1))
f.close()