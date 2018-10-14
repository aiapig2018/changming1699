from django.conf.urls import url
from . import views
 

urlpatterns = [
    url(r'^test/',views.Test,name="ourstory_test"),
    url(r'^home/',views.home,name="ourstory_home"),
    url(r'^(?P<id>\d+)/$',views.Detail,name="ourstory_detail"),
]


