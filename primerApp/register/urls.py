from django.urls import path, re_path
from django.conf.urls import include


from register.views import RegisterView,RegisterViewNew,RegisterIdView

urlpatterns = [
    re_path(r'^v1/register/', RegisterView.as_view()),   
    re_path(r'^v2/register/', RegisterViewNew.as_view()),
    re_path(r'^v3/register/(?P<pk>\d+)$', RegisterIdView.as_view()),
]