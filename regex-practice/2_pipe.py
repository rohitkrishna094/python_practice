import re

# the pipe operator will match one of the many expressions
# if r'Batman|Tina Fey' is given, then it will match either Batman or Tina Fey
# When both occur in the string, the first occurrence is matched

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel due to ')
print(mo.group())  # should return Batmobile
print(mo.groups())
