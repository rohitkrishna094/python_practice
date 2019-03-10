import re

# in this we will see ?, *, {}, +

# ? is enforces preceding thing to be optional
# will match both batman and batwoman
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

# * is used to match zero or more
# In the below example wo is matched zero or once or more times
print('-----------------------------------')
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The adventures of Batwowowowoman')
print(mo3.group())

# + is to match once or more
print('-----------------------------------')
batRegex = re.compile(r'Bat(wo)+man')
# this wont be matched this time
mo1 = batRegex.search('The adventures of Batman')
if(mo1 != None):
    print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The adventures of Batwowowowoman')
print(mo3.group())
