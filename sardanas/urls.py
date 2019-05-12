from django.conf.urls import url

from sardanas.views import SardanesList, SardanaDetail

urlpatterns = {
    url(r'^$', SardanesList.as_view()),
    url(r'(?P<pk>\d+)', SardanaDetail.as_view()),
}