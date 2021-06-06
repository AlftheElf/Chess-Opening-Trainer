#

import re
import os
import os.path

def box(body):
    os.system("osascript -e 'Tell application \"System Events\" to display dialog \"" + body + "\"'")

f = open("/Users/alfiestoppani/Documents/Scripts/HTML/Apache/index.html", "r")
x = f.read()
f.close()

a = re.findall(r'<!-- Version .+? -->',x)[0]
b = a.split(' ')[-2]

c = b.split('.')

dirString = "V%s.%s" % (c[0],c[1])
fileString = "/%s.%s.%s.html" % (c[0],c[1],c[2])
filePath = '/Users/alfiestoppani/Documents/Scripts/HTML/Apache/Versions/' + dirString + fileString
bigString = 'cp /Users/alfiestoppani/Documents/Scripts/HTML/Apache/index.html ' + filePath

#Test if file already exists
if os.path.exists(filePath):
    box('File already exists!')
else:
    box('Success')
    os.system('mkdir /Users/alfiestoppani/Documents/Scripts/HTML/Apache/Versions/%s' % dirString)
    os.system(bigString)
