from django.http import Http404
from django.shortcuts import render
from .models import NJ_CC_Data_Tables

def index(request):
	all_courses = NJ_CC_Data_Tables.objects.all()
	#context = {'all_courses' : all_courses}
	return render(request, 'NJCCData/NJCCData.html', {'all_courses' : all_courses})

def course_descriptions(request, course_description):
	try:
		course = NJ_CC_Data_Tables.objects.get(pk=course_description)
	except NJ_CC_Data_Tables.DoesNotExist:
		raise Http404("Course description not available")
	return render(request, 'NJCCData/course_description.html', {'course' : course})
