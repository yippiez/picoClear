#glob is for reading any 
import glob
#for sorting the input out a bit
import re


filename=""
output=[]

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

for index,line in enumerate(output):
    content=line.split("--")[0]
    output[index]=content



print("Creating a {}".format(filename))
for i in output:
    with open(filename, "a") as f:
        if(i!=""):
            f.write(i + "\n")
