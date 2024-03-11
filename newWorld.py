# this type data : List
x = [1,2.1,"halohehe",True,False,3.3]
x[1] = "ganznih"

print(x)

# this type data : tuple > a part of list but can't change
ha = (1.2,"halo is me",True,4.21)
# ha[1] = "something"

print(ha)

#this type data : set > can't duplicate and without index
ye = {1,2,3,4,4,4,45,7,6}
print(ye)

#this type data : dictionary > consist of key and value, can't use index
tes = {"name":"Riko kurnia","age":123,"isMarried":False}
tes ["haveFriend"] = True
del tes["name"]
print(tes)

#Convertion between int,float and string
# first int to float
print(float(5))
# second float to int
print(int(7.9))
# third string to int or float
print(str(8.3))
print(int("82"))