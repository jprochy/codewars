triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]


def recoverSecret(triplets):
    douplets = []
    lets = []
    secret = ""
    for trips in triplets:
        if [trips[0],trips[1]] not in douplets:
            douplets.append([trips[0],trips[1]])
        if [trips[1],trips[2]] not in douplets:
            douplets.append([trips[1],trips[2]])
        lets.append(trips[0])
        lets.append(trips[1])
        lets.append(trips[2])
        lets[:] = list(set(lets))
    while len(douplets) > 0:
        for a in douplets:
            boo = True
            for b in douplets:
                if (a == b):
                    True
                elif (a[0] == b[1]):
                    boo = False
                    break
            if boo:
                tmp = a[0]
                if tmp in lets:
                    secret+=tmp
                    lets.remove(tmp)
                for it in douplets:
                    if (it[0] == tmp):
                        douplets.remove(it)
                break
    return secret+''.join(lets)
    
print(recoverSecret(triplets))