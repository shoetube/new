#!/usr/bin/python3.5
#to give permission, enter: chmod -v +x [filename]

######################################################################
# This program takes an XML file and converts it to a list of
# dictionaries.  
# 
# 
######################################################################
deleteHead = 22
deleteTail = 3

# Open file and read to string
inputFile = open('animelist.xml')
inputStr = inputFile.read()
inputFile.close()

# splits lines accross a list called l while keeping end of line character
l = inputStr.splitlines(True)

# delete head and tail of file
for i in range(deleteHead):
  l.pop(0)
for i in range(deleteTail):
  l.pop(-1)

# recombines list to string (possible future update: split on ('\t'*3 + '</'))
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

# eliminate cdata enclosure
s1 = '<![CDATA['
s2 = ']]>'
for i in l:
  for j in i:
    start1 = j.find(s1)
    start2 = j.find(s2) 
    if start1 > -1:
      end1   = start1 + len(s1)
      end2   = start2 + len(s2)
      index = i.index(j)
      i[index] = i[index].replace(s1, '')                                              
      i[index] = i[index].replace(s2, '')

# removes '_' and '<' characters
for i in range(len(l)):
  for j in range(len(l[i])):
    l[i][j] = l[i][j].replace('_',' ')
    l[i][j] = l[i][j].replace('<','')

# splits sublist on '>' thus separating key and items
for i in range(len(l)):
  for j in range(len(l[i])):
    l[i][j] = l[i][j].split('>')
    
# removes items with no value associated
for i in range(len(l)):
  j = 0
  while j < len(l[i]):
    if l[i][j][1] == '':
      l[i].pop(j)
      continue
    j+=1

aList = []
for i in range(len(l)):
  aList.append({})
  for j in range(len(l[i])):
    aList[i].update({l[i][j][0]:l[i][j][1]})

# Contents of output
oString = ''
for i in aList:
  if i['my status'] == 'Completed':
    oString += i['series title'] +' '*(60 - len(i['series title'])) + i['my score'] +'\n'

# Outputs results to file
outputFile = open('output.txt', 'w')
outputFile.write(oString)
outputFile.close()
