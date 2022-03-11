from django.shortcuts import render
# Create your views here.
from .models import employes
from .models import theDataOfBuildings
from .models import ageCount
from .models import communityEmployes
from .models import nameOfRoads
from .models import About as about
from .models import NewsPost
from .models import Catagory
from .models import Contact as contact
# Home page render
def Home(request):
    data = {
        'employes':employes.objects.all(),
        'edit':theDataOfBuildings.objects.all(),
        'ages':ageCount.objects.all(),
        'commemplyes':communityEmployes.objects.all(),
        'nameOfRoads':nameOfRoads.objects.all(),

    }
    return render(request,'home/index.html' , data)

# About page render
def About(request):

    data = {
        'edit':about.objects.all()
    }
    return render(request , 'home/about.html' , data)

# def news page render
def News(request):
    data ={
        'edit':NewsPost.objects.all(),
        'categorys':Catagory.objects.all(),
        'searchHide':True
    }
    return render(request , 'home/news.html' , data)

def SearchApi(request):
    search = []
    if request.method == 'GET':
        key = request.GET['query']
        search = searchNews(NewsPost.objects.all() , key , search)
        print(key)
        print(search)
    data ={
        'edit':search,
        'categorys':Catagory.objects.all()
    }    
    return render(request , 'home/news.html' , data)

def Contact(request):
    data = {}
    return render(request , 'home/contact.html' , data) 

def ContactSend(request):
    if request.method == 'POST':
        contact(fullName=request.POST['name'],phoneNumber = request.POST['phone'],messageUser = request.POST['message']).save()
    return render(request , 'home/contact.html') 

def CategoryRender(request,category):
    newsSplitCategory = []
    data = {
        'edit':filterCategory(NewsPost.objects.all() , newsSplitCategory , category[4::]),
        'categorys':Catagory.objects.all()
    }
    return render(request,'home/news.html',data)

def filterCategory(args:list , data:list , request:str) -> list: 
    for arg in args:
        if arg.select.catagory == request:
            data.append(arg)
    return data
def searchNews(args:list,key:str,newArgs:list) -> list:
    for arg in args:
        if arg.message.lower().count(key.lower()) > 0:
            newArgs.append(arg)
    return newArgs
        

# Comments page render 
# def Comments