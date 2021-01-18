from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('<int:requestion_id>/', views.detail, name='detail'),
    path('<int:requestion_id>/results/', views.results, name='results'),
    path('<int:requestion_id>/vote/', views.vote, name='vote'),
]