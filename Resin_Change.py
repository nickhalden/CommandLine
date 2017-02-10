""" 
    takes an xml file and puts in all the changes are mentioned in the .conf file
    eg:
    server:ip
    port:88888
    add additional restarting the server to make chanes to process
    
    // Happy coding
"""
    

#make  server specific changes

conf = open('change.txt', 'r+')
newlines=[]
configFile=conf.readlines()

#adding config file in a list
for line in configFile:
    new= line.strip('\n')
    newlines.append(new)

#putting elements in a dictionary
c=dict(element.split(':') for element in newlines)
print c

inp=open('template.conf', 'r+') #sample template you want to change
out=open('resin.conf','w+') #output

inputLines=inp.readlines()

#replace method using key value pairs in a dictionary
def replace_all(text, dic):
    for i,j in dic.iteritems():
        if i in text:
            text=text.replace(i,j)
    return text

#for each line in template call for making changes(replacements)
for each in inputLines:
    line=str(each)
    ret=replace_all(line,c)
    out.write(ret)

inp.close()
out.close()
conf.close()
