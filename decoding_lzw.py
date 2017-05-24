import struct
from sys import argv

MAX_TABLE_SIZE = 2**int(argv[2])

 
myfile2 = open("C:\Python27\\"+str(argv[1]),"rb")
output_sequence_binary = myfile2.read()
#print table1
myfile2.close()

n = len(output_sequence_binary)
n = n/2
print n

j = 0
i = 0
h = '>'

for j in range(0,n):
    h = h + 'H'
    
code = (struct.unpack(h,output_sequence_binary))
#print code

o =[]

table = []
for i in range(0,256):
    table.append((chr(i)))

#print table
i = 0
string = ''
newstring = ''
table2 = ''
output = 256
dict_code = []
i=0
j=0

while i < len(code):
    if code[i] < 256:
        dict_code.append(code[i])
    i = i+1

dict_code = sorted(dict_code)
#print dict_code

c = code[0]
decoded_out = ''

#table = table1.split()

#table = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']

string = table[c]
decoded_out = string
#print string
i=1
while i < len(code):
    c = code[i]
    i = i+1
    if c not in dict_code :
        newstring = string + string[0]
    else:
        while c != dict_code[j]:
            j=j+1
        newstring=table[dict_code[j]]
        j = 0
        #print newstring
    decoded_out=decoded_out + (newstring)

    if len(table) < MAX_TABLE_SIZE:
        table2 = string + newstring[0]
        table.append(table2)
        dict_code.append(output)
        output = output + 1
        #print table
    string = newstring
        
#print dict_code
print decoded_out
#print table
