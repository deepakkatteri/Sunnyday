"""Sunnyday URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from . import views
app_name="mysite"
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^product/$',views.Product_table,name='product'),
    url(r'^product/(?P<product_id>[0-9]+)/$',views.details,name='details'),
    #url(r'^job_new',views.job_new,name='newjob'),
    #url(r'^downtime/machine/(?P<machine_id>[0-9]+)/$',views.machine_history,name='machine_details'),
    #url(r'^Daily_report_view',views.Daily_report_view,name='Dailyreportform'),
    #url(r'^downtime/plant/(?P<plant_id>[0-9]+)/$',views.plant_status,name='plant_status')
    
]
