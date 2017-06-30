from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from NJCCData.models import NJ_CC_Data_Tables
from . import views

urlpatterns = [ 
	#/NJCCData/
	#url(r'^$', ListView.as_view(queryset=NJ_CC_Data_Tables.objects.all(),
											#template_name="NJCCData/NJCCData.html")),
	url(r'^$', views.index, name='index'),
	#/NJCCData/25
	url(r'^(?P<course_description>[0-9]+)/$', views.course_descriptions, name='course_descriptions')	
	#url(r'^(?P<pk>\d+)/$', ListView.as_view(queryset=NJ_CC_Data_Tables.objects.all(), template_name = 'NJCCData/course_description.html'))
]	
