from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('rd/',views.rd,name='rd'),
    path('blog/',views.blog,name='blog'),
    path('room10/',views.room10,name='room10'),
    path('room/',views.room,name='room'),
    path('room2/',views.room2,name='room2'),
    path('room3/',views.room3,name='room3'),
    path('room4/',views.room4,name='room4'),
    path('room5/',views.room5,name='room5'),
    path('room6/',views.room6,name='room6'),
    path('room7/',views.room7,name='room7'),
    path('room8/',views.room8,name='room8'),
    path('room9/',views.room9,name='room9'),
    path('book/',views.book,name='book'),
    path('base/',views.base,name='base'),
    path('checkout/',views.checkout,name='checkout'),
]