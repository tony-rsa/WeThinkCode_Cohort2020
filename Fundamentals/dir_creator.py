import os

os.system('wtc-lms topics 505079ba-4393-47ff-a956-330555b09f00 | grep "In Progress" >> topics.txt')
file = open("topics.txt", "r")
os.remove("topics.txt")
topics = file.readlines()
file.close()

commnads = list()
for each in topics:
    words = each.split(" ")
    i = 0
    line = 'mkdir "'
    while words[i] != "[In":
        line += words[i] + " "
        i += 1
    commands.append(line + '"\n')

for each in commands:
  os.system(each)
