'''
Den code kannst du in deine Datei kopieren
und entsprechend anpassen
'''

file_source = 'C:\\Users\\schwe\\Desktop\\file.xyz' #bei dir hast du die datei ja schon
file_write = 'C:\\Users\\schwe\\Desktop\\modified.xyz' #wohin die neue datei soll
minZ = 1300
maxZ = 1500
withinLimit = []
with open(file_source) as f: #datei oeffnen
    content = f.readlines() #alle zeielen in array lesen
    f.close()
for line in content: #array iterieren
    #limit = limit - 1 #siehe oben
    #if limit == 0:
    #    break
    parts = line.split(' ') #split in x | y | z
    x = parts[0]
    y = parts[1]
    z = parts[2][:-2] #strip \n
    if float(z) >= 1300 and float(z) <= 1500:
        withinLimit.append(line)

#write content of withinLimit to new file
f = open(file_write, 'w')
for s in withinLimit:
    f.write(s)
f.close()
