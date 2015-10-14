from sys import argv

script, name = argv
prompt = '> '

print "hi %s, I'm the %s script." % (name, script)
print("do you like me?") 
likes = raw_input(prompt)

lives = raw_input("Oh. where do you live?")

print "where the fuck?"
print "what computer u got"
comp = raw_input(prompt)

print """
Ok, so you said %r about liking me.
You live in %r.
You have a %r computer.
""" % (likes, lives, comp)