from django.urls import path
from .import views

urlpatterns = [
    path('<int:movid_id>',views.detail,name='detail'),
]