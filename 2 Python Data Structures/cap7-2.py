fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0


for line in fh:
    if not line.startswith("X-DSPAM-Confidence: ") :
        continue


    busca = line.find("0")
    number = float (line [busca: ])
    count = count + 1
    total = total + number

print (total / count)
