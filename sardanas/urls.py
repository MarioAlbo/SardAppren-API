from django.conf.urls import url

from sardanas.views import SardanesList, SardanaDetail, SardanaFileView

urlpatterns = {
    url(r'^$', SardanesList.as_view()),
    url(r'(?P<pk>\d+)/?$', SardanaDetail.as_view()),
    url(r'(?P<pk>\d+)/file/?$', SardanaFileView.as_view()),
}