def permutations(iterable, r=None): #from itertools
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def gta(limit, *args): # find the base_list first
    base_list = []
    mx = len(str(max(args)))
    for i in range(mx):
        for num in args:
            if len(str(num)) > i:
                if base_list.count(int(str(num)[i])) == 0:
                    base_list.append(int(str(num)[i]))
    base_list [:] = base_list[:limit]
    

    ### BULLSHIT - FORGOT SITUATIONS WHEN ITEMS ARE SKIPPED
    gta_value = sum(base_list)
    for l in range(2,len(base_list)+1):
        perms = list(permutations(base_list, l))
        gta_value +=sum([x for t in perms for x in t])
    
    return gta_value

print(gta(3,1,2,3))