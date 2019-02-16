from django.conf.urls import url
#from search.views import UserLogSearchView
from .views import (
    AccountHomeView,
    AccountEmailActivateView,
    UserDetailUpdateView, 
    )


urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
    #url(r'log/search/$', UserLogView.as_view(), name='user-log'),
    url(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', 
            AccountEmailActivateView.as_view(), 
            name='email-activate'),
    url(r'^email/resend-activation/$', 
            AccountEmailActivateView.as_view(), 
            name='resend-activation'),
]