from sys import argv

script, filename = argv

print "We're finna erase %r." % filename
print "If you don't want that, hit CTRL + C"
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating File. Cya!"
target.truncate()

print "Give me 3 lines:"
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Writing to file..."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "now its closed." 
target.close()