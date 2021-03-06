from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import os

import pandas as pd

# In[76]:



# Create your views here.

def index(request):
    df = pd.DataFrame(columns=['type','title'])

    f = open(os.path.join(settings.BASE_DIR, 'plan/Gekookt.txt'),'r+',encoding="utf-8")
    for line in f.readlines():
        l, r = line[:3], line[4:].strip()
        regel = {'type':l,'title':r}
        df = df.append(regel,ignore_index=True)
    f.close()

    count = 0
    while(count<1):
        week = df.sample(n=5)
        if(len(set(week['type']))>4):
            count = count + 1
            
    out = list(week['title'])
    out = '<br/>'.join(out)    
    return HttpResponse(out)
    