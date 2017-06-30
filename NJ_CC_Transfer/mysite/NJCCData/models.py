from django.db import models
import pandas as pd 

class NJ_CC_Data_Tables(models.Model):
	credits = models.CharField(max_length=10)
	equivalent_course = models.CharField(max_length=50)

	def __str__ (self):
		return self.credits + ' ' + self.equivalent_course
