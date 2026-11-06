import json,re,sys
h=open('_artifact-page.html').read()
b=json.loads(re.search(r'id="bank">(.*?)</script>',h,re.S).group(1).replace('<\\/','</'))
def txt(q):
    fl=[]
    for x in q['o']: fl+= x if isinstance(x,list) else [x]
    return (q['q']+' '+' '.join(fl)+' '+q['w']+' '+' '.join(q['x'].values())).lower()
T=[txt(q) for q in b['Q']]
for k in sys.argv[1:]:
    print('%-22s %d'%(k,sum(k.lower() in t for t in T)))
