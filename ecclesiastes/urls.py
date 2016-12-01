"""ecclesiastes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from website import views
import django.contrib.auth.views
from django.views.generic import ListView, DetailView
from website.models import ContactStatus
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/', views.home, name='home'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^website/', include('website.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', django.contrib.auth.views.login, name='login'),
    url(r'^accounts/logout/', views.logout, name='logout'),
    url(r'^followup/(?P<pk>(\d+))/$', views.FollowUpDetailView.as_view(), name='detail'),
    url(r'^followup/edit/(?P<pk>(\d+))/$', views.FollowUpUpdateView.as_view(), name='edit'),
    url(r'^followup/$', ListView.as_view(queryset=ContactStatus.objects.all().order_by("id"), template_name='followup/followup.html'),name='followup'),

    #url(r'^followup/', login_required(ListView.as_view(queryset=ContactStatus.objects.all().order_by("id"), template_name='followup/followup.html')))
    #url(r'^website/followup/', FollowupListView.as_view(), name='contactstatus-list')
    #url(r'^followup/', views.followup, name='followup')
]
