# regex module
import re

# r is used to say that following string is a raw string. Or else we would have to type double \\
# \d matches a digit
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo stands for match objects
mo = phoneNumberRegex.search('My number is 415-555-4242.')
# mo.group() displays the matched group
print('Phone number found: ' + mo.group())

# paranthesis matches group. number of parenths means number of groups
# This can be used to get area code for instance
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 415-555-4242.')
# group 1 will give first matched group, group(2) the second and so on
# group(0) is same as group() that we did on line 10 before
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))

# the groups method gives a tuple of all matched groups
print(mo.groups())
# You can use destructuring or also called multiple assignment trick
areacode, mainNumber = mo.groups()
# sep is used to separate all arguments passed to print using a delimiter(, in the case). By default, sep value is space
print(areacode, mainNumber, sep=', ')
