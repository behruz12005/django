from django.urls import path
from .views import homePageViem

urlpatterns = [
		path('',homePageViem,name='home')
]