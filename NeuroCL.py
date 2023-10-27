import random
import subprocess
inpul = []
import os
import pickle
inpux = []
inpulx = []
logx = []
def inpuld(x):
  global inpul
  back = inpul 
  inpul = x
  return back
r = True
def drs(x,y):
  st1 = set(str(x))
  st2 = set(str(y))
  intersect = st1.intersection(st2)
  uniont = st1.union(st2)
  rpt = len(intersect) / len(uniont)
  rpst = rpt * 100
  return rpst
def nerve_in(inpu,log,split,sts,sts2,res,res2,lear,logxb):
  def run(inpu,log):
    global inpul
    global inpux
    global inpulx
    global r
    global pronouns
    global verbs
    global articles
    global logx
    global feel
    global com
    global nega
    try:
      for y in nega:
        if y in inpu:
          try:
            nega.append(inpu.index(nega) - 1);nega.append(inpu.index(y) - 2);nega.append(inpu.index(nega) + 1)
          except:pass
        flat = []
        for item in nega:
          if isinstance(item, list):flat.extend(item)  
          else:flat.append(item)
        if re == False:
          inpu.remove('nega')
    except: pass
    trm = False
    re = False
    re2 = False
    re3 = False
    re4 = False
    re5 = False
    out = []
    numr = 0
    nume = 0
    rps = drs(inpu,inpux)
    rpst = drs(inpu,inpulx)
    try:
      if rpt >= random.randint(sts-10,sts):inpu.append(inpulx)
    except:pass
    try:inpu = inpu.split(str(split))
    except:pass
    try:
      #Each is different and may require changes
      if inpu[0] == '_':
        inpux.append(inpulx)
        flat = []
        for item in inpux:
          if isinstance(item, list):flat.extend(item)
          else:flat.append(item)
        inpux = flat
        if re == False:inpu.remove('_');re=True
    except:pass
    if re or re2 or re3 or re4 or re5: rem = True
    else: rem = False
    if rem == False:
      flat = []
      inputw = []
      try:inpu = inpu.split(str(split))
      except:pass
      try:
        for item in inpu:
          if item.endswith("?") or item.endswith("!"):
            inputw.append(item)
            inpu.remove(item)
        inpu.extend(inputw)
      except:pass
      for item in logx:
        if isinstance(item, list):flat.extend(item)
        else:flat.append(item)
      logx = flat
      if logxb == True:inpu.append(logx)
      re=True
    for x in inpu:
      #print(inpul)
      if rps < random.randint(sts2-10,sts2):
        if x in inpu:
          try: nl = inpul.index(x)
          except:pass
          try:
            if lear == True:
              if str(x) in inpul or str(x) in inpulx:
                inpul.insert(nl,inpu)
                flat = []
                for item in inpul:
                  if isinstance(item, list):flat.extend(item)
                  else:flat.append(item)
                inpul = flat
                if res2 == True:inpul.append(inpu[inpu.index(x)]);inpul.append(inpu[int(inpu.index(x))-1])
                else:inpul.append(inpu[inpu.index(x)]);inpul.append(inpu[int(inpu.index(x))+1])
              numm = 1
              for n in range(len(inpu)):
                numm += 1
                if inpu[inpu.index(x)+n] != None:
                  inpul.append(inpu[int(inpu.index(x))+n])
          except:pass
          try:
            if res2 == True:
              for xn in range(len(inpu)):out.append(inpul[nl - xn])
            else: out.append(inpul[nl + 1]);out.append(inpul[nl + 2])
            if len(out)>1: out.remove(out[0])
          except:pass
      if rps >= random.randint(sts2-10, sts2):
        trm = True
        try:
          for x in inpu:
            if rps >= random.randint(sts2-10, sts2):
              try:
                nl = inpux.index(x)
                for xn in range(len(inpu)):
                  out.append(inpul[nl + xn])
              except:pass
              if trm == False:
                nl = inpul.index(x)
                for xn in range(len(inpu)):
                  out.append(inpul[nl + xn])
        except:pass
      numr += 1
    try:
      if log == True:print(inpul);print(rps),print(inpux);print(rpt)
    except:pass
    outref = []
    for it in out:
      if it not in outref:
        outref.append(it)
    if r == True:
      try:
        if len(inpu)>=2: inpul.pop(0);inpul.pop(0);r = False
      except:pass
    if res == True:outref.reverse()
    inpulx = outref
    logx = outref
    return outref
  return run(inpu,log)
def nerves_in(inpu,log,split):
  stglo = nerve_in(inpu,log,split,45,60,False,False,True,True)
  stlow = nerve_in(inpu,log,split,45,50,False,False,False,False)
  sthi = nerve_in(inpu,log,split,60,70,False,False,False,False)
  stb = nerve_in(inpu,log,split,45,50,True,True,False,False)
  stb2 = nerve_in(inpu,log,split,45,50,False,True,True,False)
  stb3 = nerve_in(inpu,log,split,45,50,True,False,False,False)
  comb = []
  if random.randint(0,5) == 5:
    for item in stglo:
      nt = random.randint(0,100)
      if nt <= 60:
        if item in stlow or item in sthi or item in stb or item in stb2 or item in stb3:
            comb.append(item)
      if nt <= 70 and nt > 60:
        if item in stlow or item in sthi and item in stb or item in stb2 or item in stb3:
            comb.append(item)
      if nt <= 80 and nt > 70:
        if item in stlow and item in sthi and item in stb or item in stb2 or item in stb3:
            comb.append(item)
      if nt <= 95 and nt > 80:
        if item in stlow and item in sthi and item in stb and item in stb2 or item in stb3:
            comb.append(item)
      if nt <= 100 and nt > 95:
        if item in stlow and item in sthi or item in stb and item in stb2 and item in stb3:
            comb.append(item)
  else:comb.append(stglo)
  flat = []
  for item in comb:
    if isinstance(item, list):flat.extend(item)
    else:flat.append(item)
  comb = flat
  try:sp = ', '.join(comb)
  except:sp = comb
  try:dl = list(set(sp.split(', ')));dl.reverse()
  except:dl = sp
  try:return dl
  except:return 0
def inpumo():
  while True:
    s=(nerves_in(input("\n\u001b[0mInput:"),False," "))
    print(s)
inpumo()