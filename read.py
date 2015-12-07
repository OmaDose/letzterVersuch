'''
Den code kannst du in deine Datei kopieren
und entsprechend anpassen
'''

file_source = 'C:\\Users\\schwe\\Desktop\\file.xyz' #bei dir hast du die datei ja schon
#limit = 10 #limit sodass es nicht die 10 Mio zeilen jedesmal nimmt (debug zwecke)
with open(file_source) as f: #datei oeffnen
    content = f.readlines() #alle zeielen in array lesen
for line in content: #array iterieren
    #limit = limit - 1 #siehe oben
    #if limit == 0:
    #    break
    parts = line.split(' ') #split in x | y | z
    x = parts[0]
    y = parts[1]
    z = parts[2]
    print 'z: ' + str(z) #output z
