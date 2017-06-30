import csv,sys,os

project_dir = "/home/jason/Repo/NJ_CC_Transfer/NJ_CC_Transfer/mysite/mysite/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from NJCCData.models import NJ_CC_Data_Tables

data = csv.reader(open("/home/jason/Repo/NJ_CC_Transfer/NJ_CC_Transfer/mysite/AtlanticCapeCountyData.csv"), delimiter=",")

for row in data:
	#if row[0] != 'credits':
		nj_cc_data_tables = NJ_CC_Data_Tables()
		nj_cc_data_tables.credits = row[0]
		nj_cc_data_tables.equivalent_course = row[1]
		nj_cc_data_tables.save()
