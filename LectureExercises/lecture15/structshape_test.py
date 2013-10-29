from structshape import structshape

t = range(3)
s = 'allen'
t.append(s)

d = []
# d[1,2] = s
# d[2,3] = t

d=[d,1]

print d
print structshape(d)