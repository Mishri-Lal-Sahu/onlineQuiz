from django.conf.urls import url
from . import views

urlpatterns=[
       url(r'^$',views.logout,name="logout"),
       url(r'^index',views.index,name="index"),
       url(r'^registration',views.registration,name="registration"),
       url(r'^cusernam',views.cusernam,name="cusernam"),
       url(r'^login',views.login,name="login"),
       url(r'^gkquiz',views.gkquiz,name="gkquiz"),
       url(r'^mathquiz',views.mathquiz,name="mathquiz"),
       url(r'^computerquiz',views.computerquiz,name="computerquiz"),
       url(r'^sciencequiz',views.sciencequiz,name="sciencequiz"),
       url(r'^gkqresult',views.gkqresult,name="gkqresult"),
       url(r'^mqresult', views.mqresult, name="mqresult"),
       url(r'^cqresult',views.cqresult,name="cqresult"),
       url(r'^sqresult',views.sqresult,name="sqresult"),
       url(r'^logcode',views.logcode,name="logcode"),
       url(r'^contactus',views.contactus,name="contactus"),
       url(r'^aboutus',views.aboutus,name="aboutus"),
]