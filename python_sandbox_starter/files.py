# Python has functions for creating, reading, updating, and deleting files.

# to open a file
myFile = open('myfile.txt', 'w')

#get info from the file
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

#write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

#append to file
myFile=open('myfile.txt', 'a')
myFile.write(' and also PHP')
myFile.close()

#read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)