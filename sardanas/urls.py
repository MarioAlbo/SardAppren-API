from django.conf.urls import url

from sardanas.views import SardanesList

urlpatterns = {
    url(r'^$', SardanesList.as_view()),
    # url(r'^(?P<id>\d*)/?$', view=sardana_detail, name='Sardana'),
}