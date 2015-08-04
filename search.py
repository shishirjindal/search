import os
print "Enter The name of directory u want to search:"
s = raw_input()
print "Enter name of drive to search file"
drive = raw_input()
for root, dirs, files in os.walk(drive+"://", topdown=False):
    for name in files:
    	if(name == s):
    		print(os.path.join(root, name))
    		break
    for name in dirs:
        if(name == s):
    		print(os.path.join(root, name))
    		break