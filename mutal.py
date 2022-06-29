from asyncore import read
import os


with open('file1.txt', 'r') as file1:
    print("frist file", file1)
    with open('file2.txt', 'r') as file2:
        print("Second file", file2)
        
        same = set(file1).intersection(file2)
        

same.discard('\n')
print("similar data", same)
##print(type(same))

with open('output.txt', 'w') as output:
    output.write('\n'.join(str(line) for line in same))
    
    
if os.stat('output.txt').st_size == 0:
    print("Duplicate data not found")
else:
    print("Duplicate data found")