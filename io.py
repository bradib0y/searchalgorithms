import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

# r'string' - A raw string that makes writing regular expressions easier
pattern = r'something'

# Use re.match for beginning of the string 
print(re.match(r'Love', data))

# Use re.search for anywhere inside the string
print(re.search(r'Chalkley', data))

