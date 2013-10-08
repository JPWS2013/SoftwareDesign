def head(lst):
    if len(lst) > 0:
        return lst[0]
    else:
        raise "Can't get head of empty list"

def rest(lst):
    if len(lst) > 0:
        return lst[1:]
    else:
        raise "Can't get rest of empty list"

def combine (hd, rst):
    return [hd] + rst

def rev(original, revd=None):
    if revd == None: revd = []
    if original == []:
        return revd

    grow = combine(head(original), revd)

    return rev(rest(original), grow)

def madness(m = []):
    m.append(7)
    return m
print rev([1,2,3,4,5,6,7,8,9,10])

print madness()

print madness()