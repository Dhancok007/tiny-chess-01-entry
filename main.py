import json,os,time,base64,zlib,urllib.request as U
_a=0;_r=[_a:=(_a+b)&255 for b in zlib.decompress(base64.b85decode('c-k$H+irv~5JNql1flZN{p0qjyPM3VW?K}25;)^yKJj;b_-o|x6CmM;Fv8Fl?J#Sko^9~RQNZBhKlgPWb$y?Y;aAq!nOBi><#u@cMjD$p{~n0w8U|)R&v4Vk_UB;Dsu?ysUVdn(bpZ4mYl0}W?$DrnUuKr+Ejl@^X`51Xu)~68GPnyUcz4<RAWOVfiWgpMnuL0*k}DlpHBe`Asi>0eAzM<x_4ZbI#oc1g77tl4^|nv_EO%|nU`q8WxXE81$+M?A2pH&8aJ$te9eLzBV)id0;*Np'))]
VM=(82,337,365,477,1025,0);VV=dict(zip('PNBRQK',VM));PM={};SQ=[s for s in range(128)if not s&136]
for _i,_p in enumerate('PNBRQK'):
 _l=[VM[_i]+(_r[_i*64+(7-(s>>4))*8+(s&7)]-128)*10 for s in range(128)];PM[_p]=_l;PM[_p.lower()]=[-x for x in _l[::-1]]
KN=(-33,-31,-18,-14,14,18,31,33);KG=(-17,-16,-15,-1,1,15,16,17);DG=(-17,-15,15,17);SG=(-16,-1,1,16);CM={4:12,7:14,0:13,116:3,119:11,112:7}
B=['.']*128;KP=[0,0];I=10**9
def parse(f):
 global W,CR,AM;p=f.split();B[:]=['.']*128;i=112
 for ch in p[0]:
  if ch=='/':i-=24
  elif ch.isdigit():i+=int(ch)
  else:B[i]=ch;i+=1
 KP[:]=map(B.index,'Kk');W=p[1]=='w';CR=0
 for ch in p[2]:CR|={'K':1,'Q':2,'k':4,'q':8}.get(ch,0)
 AM=sum(PM[B[s]][s]for s in SQ if B[s]!='.')
def A(s,bw):
 for ds,ww in zip((((15,17),(-17,-15))[bw],KN,KG),('pnk','PNK')[bw]):
  for d in ds:
   if not s+d&136 and B[s+d]==ww:return True
 for ds,pp in((DG,'BQ'),(SG,'RQ')):
  for d in ds:
   t=s+d
   while not t&136 and B[t]=='.':t+=d
   if not t&136 and B[t].isupper()==bw and B[t].upper()in pp:return True
 return 0
def gen(cap=False):
 ms=[];ap=ms.append;up=16 if W else-16;last,fst=(6,1)if W else(1,6);PR='QNRB'if W else'qnrb'
 for s in SQ:
  x=B[s]
  if x=='.'or x.isupper()!=W:continue
  u=x.upper();r=s>>4
  if u=='P':
   t=s+up
   if B[t]=='.':
    if r==last:
     for z in PR:ap((s,t,z,'.'))
    elif not cap:
     ap((s,t,'','.'))
     if r==fst and B[t+up]=='.':ap((s,t+up,'','.'))
   for d in(up-1,up+1):
    t=s+d
    if t&136:continue
    v=B[t]
    if v!='.'and v.isupper()!=W:
     if r==last:
      for z in PR:ap((s,t,z,v))
     else:ap((s,t,'',v))
  else:
   for d in(KN,KG,DG,SG,KG)['NKBRQ'.index(u)]:
    t=s+d
    while not t&136:
     v=B[t]
     if v=='.'and not cap or v!='.'and v.isupper()!=W:ap((s,t,'',v))
     if v!='.'or u in'NK':break
     t+=d
   if u=='K'and not cap and s==KP[not W]:
    for sg,bt in((1,1),(-1,2)):
     if CR&bt*(1 if W else 4)and B[s+sg]=='.'and B[s+2*sg]=='.'and(sg>0 or B[s-3]=='.')and not any(A(s+k*sg,not W)for k in(0,1,2)):ap((s,s+2*sg,'','.'))
 return ms
def make(m):
 global W,CR,AM;s,t,pr,cap=m;x=B[s];AM-=PM[x][s]
 if cap!='.':AM-=PM[cap][t]
 n=pr or x;B[t]=n;B[s]='.';AM+=PM[n][t]
 if x in'Kk':
  KP[x=='k']=t
  if abs(t-s)==2:
   rs,rt=(s+3,s+1)if t>s else(s-4,s-1);rc=B[rs];B[rt]=rc;B[rs]='.';AM+=PM[rc][rt]-PM[rc][rs]
 CR&=CM.get(s,15)&CM.get(t,15);W=not W
def O(ms):
 return sorted(ms,key=lambda m:VV.get(m[3].upper(),0)*10-VV[B[m[0]].upper()]//10+2000*bool(m[2]),reverse=True)
def S(d,a,b):
 global ND,BM,B,CR,AM,KP,W;ND+=1
 if ND&255==0 and time.time()>DL:raise 1
 chk=A(KP[not W],not W)
 qs=d<=0
 if qs:a=max(a,AM if W else-AM)
 best=-I
 for m in O(gen(qs and 1)):
  u=(B[:],CR,AM,KP[:],W);make(m)
  if A(KP[W],W):B,CR,AM,KP,W=u;continue
  if best==-I or qs:sc=-S(d-1,-b,-a)
  elif d>=3 and m[3]=='.'and not m[2]and not chk:
   sc=-S(d-2,-b,-a)
  else:sc=-S(d-1,-b,-a)
  B,CR,AM,KP,W=u
  if sc>best:
   best=sc
   if d==RT:BM=m
  if sc>a:a=sc
  if a>=b:break
 return a if qs else-I if best==-I and chk else 0 if best==-I else best
def choose():
 global ND,DL,BM,RT,B,CR,AM,KP,W;ND=0;DL=time.time()+3.5;legal=[]
 for m in gen():
  u=(B[:],CR,AM,KP[:],W);make(m)
  if not A(KP[W],W):legal.append(m)
  B,CR,AM,KP,W=u
 BM=legal[0];dep=1
 while 1:
  sv=BM;RT=dep
  try:S(dep,-I,I)
  except TypeError:BM=sv;break
  dep+=1
 return BM
URL=os.getenv('MAKEFUN_ENV_URL','')
def post(p,b):return json.load(U.urlopen(URL+p,data=json.dumps(b).encode()))
if URL:
 while 1:
  g=post('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':
   parse(g['fen']);x=choose();g=post('/move',{'game':g['game'],'move':f'{chr(97+(x[0]&15))}{x[0]//16+1}{chr(97+(x[1]&15))}{x[1]//16+1}{x[2].lower()}'})
