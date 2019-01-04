import re

t = 'The ghost that says boo haunts the loo'
find = re.findall('.oo',t)
print(find)
