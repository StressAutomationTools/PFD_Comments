import xml.etree.ElementTree as ET
import sys
inputs = sys.argv
filename = inputs[1]
temp = filename.split('.')
outname = temp[0]
tree = ET.parse(filename)
root = tree.getroot()
tabfile = open(outname+'.tab', 'w')
for child in root[0]:
    page = 0
    text = ''
    ctype = child.tag
    temp = ctype.split('}')
    ctype = temp[1]
    page = int(child.get('page'))+1
    if child[0].tag == '{http://ns.adobe.com/xfdf/}popup':
        text = ''
    elif child[0][0][0].find('{http://www.w3.org/1999/xhtml}span') != None:
        text = child[0][0][0][0].text
    tabfile.write(ctype+'\t'+str(page)+'\t'+text+'\n')
tabfile.close()
