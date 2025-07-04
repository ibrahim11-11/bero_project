from django.urls import path , include 
from .views import Tviewset 
from rest_framework.routers import DefaultRouter 

router = DefaultRouter ()
router.register('tasks',Tviewset,basename='task')
urlpatterns = [
    path ('',include(router.urls))
]