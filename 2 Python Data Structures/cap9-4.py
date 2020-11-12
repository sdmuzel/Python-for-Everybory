# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer


texto = open ("mbox-short.txt")
counts = dict()

for line in texto:
    if not line.startswith ('From: '): continue  # In this case is necessary use from:, for only sended emails
    word = line.split()
    email = word [1]
    counts [email] = counts.get(email, 0) + 1


bigsender = None
bigtimes = None

for email,send_numb in counts.items():
    if bigtimes is None or send_numb > bigtimes:
        bigsender = email
        bigtimes = send_numb

print (bigsender, bigtimes)
