#For testing the contents of NewFile.txt

ReadMyNewFile = open('/Users/boku/Documents/Programming/Python/python-PythonForKids/Chapter9/NewFile.txt')
NewContents = ReadMyNewFile.read()
print(NewContents)