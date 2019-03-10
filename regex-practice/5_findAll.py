import re

# findAll unlike search returns all occurrences or matches as shown below
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1.group())

# FindAll returns a list of matched strings
print('------------findAll')
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex.findAll('Cell: 415-555-9999 Work: 212-555-0000')
