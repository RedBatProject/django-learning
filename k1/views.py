from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def index(request):
  if request.method == 'POST':
      fb = request.POST['fcal']
      cal = int(fb) * 7
      return render(request, 'k1/list.html', {'cal': cal})
  else:
      return render(request, 'k1/list.html', {})
