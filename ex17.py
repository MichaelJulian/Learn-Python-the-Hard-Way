# copy one file from another
from sys import argv
from os.path import exists

script, from_file, to_file = argv 

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file eixst? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Done"

out_file.close()
in_file.close()

# Review:
# open(file) to open the file
# .read on the file object
# .write on a file object to write
# .close on file object when you're done. 
