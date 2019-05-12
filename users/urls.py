from django.conf.urls import url

from users.views import UserDetail

urlpatterns = [
    url(r'^$', UserDetail.as_view()),

]