#Python For Kids Chapter 9 
#Challenge #3 Copying a File

ReadMyFile = open('/Users/boku/Documents/Programming/Python/python-PythonForKids/Chapter9/CopyFile.txt')
Contents = ReadMyFile.read()
print(Contents)

WriteMyFile = open('/Users/boku/Documents/Programming/Python/python-PythonForKids/Chapter9/NewFile.txt', 'w')
WriteMyFile.write(Contents)

#ReadMyNewFile = open('/Users/boku/Documents/Programming/Python/python-PythonForKids/Chapter9/NewFile.txt')
#NewContents = ReadMyNewFile.read()
#print(NewContents)