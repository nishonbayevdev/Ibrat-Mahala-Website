from django.urls import re_path,path
from .views import Home
from .views import About
from .views import News
from .views import Contact
from .views import CategoryRender
from .views import SearchApi
from .views import ContactSend
urlpatterns = [
    re_path(r'^$' , Home , name='home'),
    re_path(r'^about/$' , About , name='about'),
    re_path(r'^news/$' , News , name='news'),
    re_path(r'^contact/$' , Contact , name='contact'),
    re_path(r'^news/search/$' , SearchApi),
    path('news/<str:category>',CategoryRender,name='filter'),
    re_path(r'^contact/send/$' , ContactSend)
]