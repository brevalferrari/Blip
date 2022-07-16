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
    FI=f.read().decode('utf-8','replace').splitlines()
d=dico(FI.pop(0))# dict of found settings
F=''
for l in FI:
    if not l.startswith(d['comment']):F+=l
trans={
    d['channel'].split('%')[0]:'\nif not channels in locals():channels=list()\n\
        if liste in locals():channels.append(liste)\nliste=list()\n\
        lengh=4\noctave=4\nvolume=50\nvolume_step=10\n\
        list.append(',
    d['global section']:'"g"',
    d['drum section']:'"d"',
    d['channel'].split('%')[1]:')',
    d['lengh']:'\nlengh=',
    d['octave']:'\noctave=',
    d['up']:'\noctave+=1',
    d['down']:'\noctave-=1',
    d['volume']:'\nvolume=',
    d['more']:'\volume+=volume_step',
}

print(d)
print(F.translate(F.maketrans(trans)))