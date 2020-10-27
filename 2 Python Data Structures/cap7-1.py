# Use words.txt as the file name

fname = input("Enter file name: ")
file = open (fname)
for line in file:
    ln = line.rstrip ()
    print (ln.upper())
