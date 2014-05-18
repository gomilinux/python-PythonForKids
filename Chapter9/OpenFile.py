#Python For Kids Chapter 9 Opening Files

test_file = open('/Users/boku/Documents/Programming/Python/python-PythonForKids/Chapter9/test.txt')
text = test_file.read()
print(text)


test_file = open('/Users/boku/Documents/Programming/Python/python-PythonForKids/Chapter9/myfile.txt', 'w')
text = test_file.write('this is my test file for writing')
print(text)
test_file.close()


test_file = open('/Users/boku/Documents/Programming/Python/python-PythonForKids/Chapter9/myfile.txt')
text = test_file.read()
print(text)

