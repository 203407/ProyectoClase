from Profile.views import RegisterIdView,RegisterIdPView
from django.urls import path, re_path

urlpatterns = [    
    re_path(r'^v1/profile/(?P<pk>\d+)$', RegisterIdView.as_view()),
    re_path(r'^v2/profile/(?P<pk>\d+)$', RegisterIdPView.as_view())
]