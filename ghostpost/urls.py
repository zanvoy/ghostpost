from django.urls import path
from ghostpost import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('/upvote/<int:id>/', views.upvote, name = 'upvote'),
    path('/downvote/<int:id>/', views.downvote, name = 'downvote'),
    path('/top/', views.top, name='top'),
    path('/addpost/', views.broastadd, name='addpost'),
    path('/boast/', views.boast, name='boast'),
    path('/roast/', views.roast, name='roast'),
]
