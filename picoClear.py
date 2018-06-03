#todo
#multiline comment --Done--
#true false changing to t f
#time for t
#
#
#
#
#glob is for reading any files in input
import glob
#for sorting the input out a bit
import re


filename=""
output=[]
mline=False #multi-line commens

for file in glob.glob('input\*.txt'):
    filename=file
    with open(file, 'r') as f:
        _str = f.read().splitlines() 


filtered = filter(lambda x: not re.match(r'^\s*$', x), _str)
#filtered is not really an array i want to put this to an array to work better
for i in filtered:
    output.append(i)


#prints your file to console
filename=filename[6:]
print(filename)
print("This is your code: {}\n".format(filename))
for line in output:   
    print(line)

filename=filename.split(".txt")[0]
filename=filename + "_output.txt"

print("Now editing your code:")

edit_out=lambda string,out: string.split(out)[0]

for index,line in enumerate(output):
    #edits stuff out
    content=line 
    if("--[[" in line):
        mline=True
        content=line
        print("found --[[")
    elif("]]--" in line):
        content=""
        mline=False
        print("found ]]--")
    elif("--" in line):
        content=edit_out(line,"--")
        print("found --")
    elif("//" in line):
        content=edit_out(line,"//")
        print("found //")
    if(mline):
        content=""
    print(content)
    output[index]=content
        

print("Creating a {}".format(filename))
#clears the current file
with open(filename,'w'): pass
#
for i in output:
    with open(filename, "a") as f:
        if(i!=""):
            f.write(i + "\n")
