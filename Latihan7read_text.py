#open file
data = open("data_iris.txt","r")
print ("Nama file",data.name)

#read
file_konten = data.read(100)
print ("isi data:",file_konten)

#Closed
data.close()
