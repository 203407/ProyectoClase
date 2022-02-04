from django.urls import re_path 
from primerComponenete.views import PrimerViewList
from primerComponenete.views import PrimerViewDetail

urlpatterns = [
    re_path(r'^lista/$', PrimerViewList.as_view()),
    re_path(r'^lista/(?P<pk>\d+)$',PrimerViewDetail.as_view()),
]
