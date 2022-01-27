from django.urls import re_path 
from primerComponenete.views import PrimerViewList


urlpatterns = [
    re_path(r'^lista/$', PrimerViewList.as_view()),
]
