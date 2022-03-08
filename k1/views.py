import re
from django.shortcuts import render
from django.http import HttpResponse
import time
import threading
import pandas as pd
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def i(request):
    # HttpResponse(request,"hello")
    word = pd.read_csv('\k1\static\word.csv')
    word = word[["word","mean","syn"]]
    wordsample = word.sample(10)
    words = list(wordsample['word'])
    means = list(wordsample['mean'])
    syns = list(wordsample['syn'])
    lis = []
    for i in range(len(words)):    
        lines = words[i] +" --> "+ syns[i]
        lines = lines.replace("[","")
        lines = lines.replace("]","")
        lines = lines.replace("'","")
        lines = lines.replace(":","")
        lis.append(lines)
    cal = lis
    return render(request, 'k1/word.html', {'cal': cal})
@csrf_exempt
def index(request):
  if request.method == 'POST':
        # fb2,fb3 = 2
        try:
            fb = request.POST['fcal']
        except: fb = 1
        try:
            fb2 = request.POST['fcal2']
        except: fb2 = 4
        try:
            f1 = request.POST['f5']
        except: f1 = 6
        try:
            f12 = request.POST['f25']
        except: f12 = 0
        try:
            cal = int(f1) * int(f12) + int(fb) * int(fb2)
        except:cal = 'no'
        return render(request, 'k1/list.html', {'cal': cal})
  else:
        return render(request, 'k1/list.html', {})
