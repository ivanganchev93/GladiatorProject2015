from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'message': "SPARTACUS"}
    return render(request, 'Spartacus/index.html', context_dict)

