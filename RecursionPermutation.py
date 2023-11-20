vovels = ["a","e","i","o","u"]

def Perm(vovels,perm):
    if len(vovels) > 0:
        for c in vovels:
            perm.append(Perm([x for x in vovels if x!=c],perm+[c]))
        return perm
    else:
        return perm

print(Perm(vovels,[]))