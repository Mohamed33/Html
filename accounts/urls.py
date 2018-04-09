from django.conf.urls import url
from . import views
app_name = 'accounts'
urlpatterns={
    url(r'^singup/$',views.signup_view,name='singup'),
}
