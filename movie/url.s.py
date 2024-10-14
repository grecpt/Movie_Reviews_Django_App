from django.urls import path
from .import views

urlpattern = [
    path('<int:movid_id>',views.detail,name='detail'),
]