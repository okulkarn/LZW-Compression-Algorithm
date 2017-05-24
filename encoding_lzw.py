import struct
from sys import argv

MAX_TABLE_SIZE = 2**100
#MAX_TABLE_SIZE = 2**int(argv[2])     # Max table size taken from input argument

i = 0                                # initialising variables
j = 0
k = 0
o = []
output = 256                        # input declared as length of the array
output_table = []                   # output file declared as a 1list
output_sequence = []
output_sequence_binary = []
n = len(output_table)
symbol = ''
string = ''
string1 = ''
input_sequence = 'abscjskbwcjblwckwwdqwdqcecc'

##myfile = open("C:\Python27\\"+str(argv[1]),"rb")    # input sequence taken
###myfile = open(userinput)
##input_sequence = myfile.read()
##myfile.close()

print input_sequence

table2 = ' '.join(set(input_sequence))
print table2

m = len(table2)
i = 0
table = []

# dictionary table taken as list of 256 chars
for i in range(0,256):
    table.append((chr(i)))

#table = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

print table

i = 0
while i < m:
    while j < 256:
        if table2[i] == table[j]:
            output_table.append(j)
            break
        j=j+1
    j = 0
    i = i + 1

j = 0

output_table = sorted(output_table)
#print output_table

t = []
i = 0

while i < len(input_sequence):
    symbol = input_sequence[i]
    string1 = string1 + symbol
    #print symbol
    i = i+1
    if string1 in table :
        string = string + symbol
    else :
        while string != table[j]:
            j=j+1
        while j != output_table[k]:
            k=k+1
        output_sequence.append(output_table[k])
        k = 0
        j = 0
        if len(table) < MAX_TABLE_SIZE :
            output_table.append(output)
            output = output + 1
            string = string + symbol
            t = string
            table.append(t)
        string = symbol
        string1 = symbol
#output_table[n+i] = output + 1
if string1 in table:
    while string != table[j]:
        j=j+1
    while j != output_table[k]:
        k=k+1
    output_sequence.append(output_table[k])
    k = 0
    j = 0

i = 0

print output_sequence

#data paked 16 bit binary
for i in range(0,len(output_sequence)):
    output_sequence_binary.append(struct.pack('>H',output_sequence[i]))

print output_sequence_binary
i = 0


for i in range(0,len(output_sequence_binary)):
    o.append(struct.unpack(">H",output_sequence_binary[i]))


o = [x[0] for x in o]    
output_sequence_binary =''.join(output_sequence_binary)

i=0

fo = open(argv[1][:-3]+"lzw",'wb')
fo.write(output_sequence_binary)    

# Close opend file
fo.close()
