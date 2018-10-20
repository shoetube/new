#!/usr/bin/python3.5
#to give permission, enter: chmod -v +x [filename]
deleteHead = 22
deleteTail = 3

# Open file and read to string
inputFile = open('animelist.xml')
inputStr = inputFile.read()
inputFile.close()

l = inputStr.splitlines(True)

# delete head and tail of file
for i in range(deleteHead):
  l.pop(0)
for i in range(deleteTail):
  l.pop(-1)

# recombines list to string
tempStr = ''
tempStr = tempStr.join(l)
l = tempStr.split('</anime>')

# creates list of lists. top list divides by anime, sublist divides each anime by line
for i in range(len(l)):
  l[i] = l[i].splitlines()  

# removes white space from each line
for i in range(len(l)):
  for j in range(len(l[i])):
    l[i][j] = l[i][j].strip()
    if l[i][j] == '\t\t\t':
      l[i].pop(j)

# removes empty strings from sublists
for i in range(len(l)):
  while l[i].count('') > 0:
    l[i].remove('')

# removes empty sublists
while l.count([]):
  l.remove([])

# removes end tags

for i in range(len(l)):
  subFor = range(len(l[i])) 
  for j in subFor:
    sSlice = l[i][j].find('</')
    if sSlice > 1:
      l[i][j] = l[i][j].replace(l[i][j][sSlice:],'')

# Contents of output
oString = ''
for i in l:
  for j in i:
    oString += j+'\n'

# Outputs results to file
outputFile = open('output.txt', 'w')
outputFile.write(oString)
outputFile.close()
