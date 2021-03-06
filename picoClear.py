#todo
#multiline comment --Done--
#cleans the file --Done--
#true false changing to t f --Done--
#time for t function
#long if statemen shortening
#Bug: is_true gets replaced by is_t remove that from happening
#Replace print with ?
#
#glob is for reading any files in input
import glob
#for sorting the input out a bit
import re


filename=""
output=[]
mline=False #multi-line commens
#checks if t=true or f=false declared in pico-8 code
tDeclared=False
fDeclared=False

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
    #edits stuff out elif is neccesary
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
    if("true" in line):
        print("found true")
        content=content.replace("true", "t")
    if("false" in line):
        print("found false")
        content=content.replace("false", "f")
    print(content)
    output[index]=content


print("Creating a {}".format(filename))
#clears the current file
with open(filename,'w'): pass
#adds if line is not empty
with open(filename, "a") as f:
    f.write("t=true \n")
    f.write("f=false \n")
    for i in output:
        if(i!=""):
            f.write(i + "\n")
