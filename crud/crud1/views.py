from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse,request,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import details
import time
# Create your views here.
@csrf_exempt
def index(request):
    if request.method=='POST':
        print(True)
        name=request.POST.get("name","")
        print(name)
        language=request.POST.get("language","")
        print(name)
        print(time.time())

        details(name=name,language=language).save()
        messages.success(request,"Addedd")
    detail=details.objects.all()
    g=""
    print(detail)
    for i in detail:
        g=g+f"<tr style='border:1px;solid;black;'> <td>{i.name}</td><td>{i.language}</td><td><a href='/delete/{i.name}/'>Delete This</a></td> </tr>"
    print(g)
    return HttpResponse(f"<h1>Details of the students</h1><table rules='all' border='5' style='text-align:center;border:1px;solid;black;' width='100%'><tr style='border:1px;solid;black;'> <td>Name</td><td>Language</td><td>Action</td> </tr>{g}</table><br><br><h1>Create A new one</h1><br><form style:'text-align:center;' action='/' method='post'>"
                         "Enter the Name :<input type='text' id='name' name='name' required><br>Enter the Language:<input type='text' id='language' name='language'><br><button type='submit'>Create</button> </form>")
def pre(request):
    return HttpResponse("pre")
def delete(request,id):
    details.objects.filter(name=id).delete()
    return HttpResponseRedirect("/")
