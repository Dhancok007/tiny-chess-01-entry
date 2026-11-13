import json,os,base64,urllib.request as U
V=dict(zip('PNBRQK',(100,320,330,500,900,0)))
_d=[x-60 for x in base64.b64decode('PDw8PG5ubm5GRlBaQUFGVTw8PFBBNzI8QUZGKDw8PDweFBQKHhQUCh4UFAoeFBQKKB4eFDIoKChQUDw8UFpGPA==')]
_T=[_d[:32],_d[32:]];Z=[0]*32
TAB=dict(zip('PK',_T))
KN=(-33,-31,-18,-14,14,18,31,33);KG=(-17,-16,-15,-1,1,15,16,17)
DG=(-17,-15,15,17);SG=(-16,-1,1,16);DIRS={'N':KN,'K':KG,'B':DG,'R':SG,'Q':KG}
SQ=[s for s in range(128)if not s&136]
B=['.']*128;W=True;KP=[0,0];CR='';ND=0;CAP=99999;I=10**9
def parse(fen):
 global W,CR,OS
 p=fen.split();B[:]=['.']*128;r,f=7,0
 for ch in p[0]:
  if ch=='/':r,f=r-1,0
  elif ch.isdigit():f+=int(ch)
  else:B[r*16+f]=ch;f+=1
 KP[:]=map(B.index,'Kk')
 OS={s for s in SQ if B[s]!='.'}
 W=p[1]=='w';CR=p[2].strip('-')
def attacked(s,bw):
 for dirs,ww in zip(((-17,-15)if bw else(15,17),KN,KG),'PNK'if bw else'pnk'):
  for d in dirs:
   t=s+d
   if not t&136 and B[t]==ww:return True
 for d in DG+SG:
  t=s+d
  while not t&136:
   c=B[t]
   if c!='.':
    if c.isupper()==bw and(c.upper()=='Q'or c.upper()==('B'if abs(d)in(15,17)else'R')):return True
    break
   t+=d
def gen(cap=False):
 ms=[];ap=ms.append;up=16 if W else-16;last,f6=(6,1)if W else(1,6);pr='Q'if W else'q'
 for s in SQ:
  c=B[s]
  if c=='.'or c.isupper()!=W:continue
  u=c.upper();r=s>>4
  if u=='P':
   t=s+up
   if B[t]=='.':
    if r==last:ap((s,t,pr,'.'))
    elif not cap:
     ap((s,t,'','.'))
     if r==f6 and B[t+up]=='.':ap((s,t+up,'','.'))
   for d in(up-1,up+1):
    t=s+d
    if t&136:continue
    v=B[t]
    if v!='.'and v.isupper()!=W:ap((s,t,pr if r==last else'',v))
  else:
   for d in DIRS[u]:
    t=s+d
    while not t&136:
     v=B[t]
     if v=='.'and not cap:ap((s,t,'','.'))
     elif v!='.'and v.isupper()!=W:ap((s,t,'',v))
     if v!='.'or u in'NK':break
     t+=d
   if u=='K'and not cap and s==KP[not W]and('K'if W else'k')in CR and B[s+1]==B[s+2]=='.'and not attacked(s,not W)and not attacked(s+1,not W)and not attacked(s+2,not W):ap((s,s+2,'','.'))
 return ms
def make(m):
 global W,CR
 s,t,pr,cap=m;c=B[s];o=(c,CR)
 B[t]=pr if pr else c;B[s]='.'
 OS.discard(s);OS.add(t)
 if c in'Kk':
  KP[c=='k']=t
  if abs(t-s)==2:B[s+1]=B[s+3];B[s+3]='.';OS.discard(s+3);OS.add(s+1)
 for ch,sq in(('K',7),('k',119)):
  if c==ch or s==sq or t==sq:CR=CR.replace(ch,'')
 W=not W
 return o
def unmake(m,o):
 global W,CR
 W=not W;s,t,pr,cap=m;c,CR=o;B[s]=c;B[t]=cap
 OS.discard(t);OS.add(s)
 if cap!='.':OS.add(t)
 if c in'Kk':
  KP[c=='k']=s
  if abs(t-s)==2:B[s+3]=B[s+1];B[s+1]='.';OS.discard(s+1);OS.add(s+3)
def ev():
 s=0
 for sq in OS:
  c=B[sq]
  u=c.upper();r,f=divmod(sq,16);w=c.isupper()
  mf=(f,7-f)[f>3];j=((7-r)if w else r)*4+mf;v=V[u]+TAB.get(u,Z)[j]
  if u in'NBRQ':v+=(mf+(r,7-r)[r>3])*3
  s+=v if w else-v
 return s if W else-s
ordered=lambda ms:sorted(ms,key=lambda m:((V[m[3].upper()]*10-V[B[m[0]].upper()]//10)if m[3]!='.'else 0)+900*bool(m[2]),reverse=True)
def search(d,a,b):
 global ND
 ND+=1
 if ND>CAP:raise Exception
 chk=attacked(KP[not W],not W)
 if d<-6:return-100000-d if chk else ev()
 if d<=0 and not chk:
  st=ev()
  if st>=b:return st
  if st>a:a=st
  ms=gen(True)
 else:ms=gen()
 ok=False
 for m in ordered(ms):
  u=make(m)
  if attacked(KP[W],W):unmake(m,u);continue
  ok=True;sc=-search(d-1,-b,-a);unmake(m,u)
  if sc>a:a=sc
  if a>=b:break
 if not ok:return-100000-d if chk else a if d<=0 else 0
 return a
def choose():
 global ND
 ms=[]
 for m in gen():
  u=make(m)
  if not attacked(KP[W],W):ms.append(m)
  unmake(m,u)
 best=ms[0];dep=1
 while dep<10:
  ND=0;a=-I;cur=best
  try:
   for m in ordered(ms):
    u=make(m);sc=-search(dep-1,-I,I);unmake(m,u)
    if sc>a:a,cur=sc,m
  except Exception:break
  best=cur;dep+=1
 return best
URL=os.getenv('MAKEFUN_ENV_URL','')
def post(p,b):
 return json.load(U.urlopen(U.Request(URL+p,data=json.dumps(b).encode())))
if URL:
 while 1:
  g=post('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':
   parse(g['fen']);x=choose();u='abcdefgh'[x[0]&15]+str(x[0]//16+1)+'abcdefgh'[x[1]&15]+str(x[1]//16+1)+x[2].lower()
   g=post('/move',{'game':g['game'],'move':u})
