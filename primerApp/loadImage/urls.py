from django.urls import re_path 
from loadImage.views import FirstViewList

urlpatterns = [
    re_path(r'^list/$',FirstViewList.as_view()),
]