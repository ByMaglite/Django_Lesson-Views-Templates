from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'title':'clarusway',
        'dict1' :{'django':'best framework'},
        'my_list': [2,3,4],
    }
    return render (request,'app/home.html',context)
