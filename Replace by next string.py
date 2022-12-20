string=str(input(' enter a string : '))
replacestring=''
for letter in string:
    code=ord(letter)
    next_letter=chr(code+1)
    replacestring=replacestring+ next_letter
print(replacestring)
