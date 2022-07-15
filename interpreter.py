def dico(file):
    d={}
    with open(file,'rb') as f:
        for l in f.read().decode('utf-8','replace').splitlines():
            if '=' in l:d.__setitem__(*l.split('='))
    for k in ['notes','&also','instruments']:
        if k in d:d[k]=d[k].split(',')
    return d
def spot(possibilities,text,canbedigit=False):
    i=len(possibilities)-1
    while i!=-1:
        if not possibilities[i]:
            del possibilities[i]
        i-=1
    if possibilities:
        if len(possibilities)==1:
            if not canbedigit:return possibilities[0]
        else:
            ps=[d[k] for k in possibilities]
            ps.sort(key=len)
            ps.reverse()
            while ps:
                if ps[0]==text[:len(ps[0])]:return ps[0]
                ps.pop(0)
    if canbedigit:
        i=0
        while text:
            if not text[i].isdigit():return text[:i]
            i+=1
with open('example','rb') as f:
    F=f.read().decode('utf-8','replace').splitlines()
d=dico(F.pop(0))# dict of found settings
print(d)
F=''.join(F).replace(' ','')# compact rest of file
print(F)
b=len(d['channel'].split('%')[0])# block size
m=False# block match with known keyword
g=False# global section already encountered
while F:
    if F[:b]==d['channel'].split('%')[0]:
        m=True
        c=spot(['global section'*(not g),'drum section'],F[b:],True)
        b+=len(c)
        if (not g) and c==d['global section']:
            g=True
            print("We're now in the global section.")
        elif c==d['drum section']:
            print('drum')
        else:print(f'channel {c}')
    F=F[b if m else 1:]
    b=len(d['channel'].split('%')[0])
    m=False