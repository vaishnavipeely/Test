from django.shortcuts import render

import pandas as pd
import numpy as np
from sklearn import pipeline,preprocessing,metrics,model_selection,ensemble
from sklearn_pandas import DataFrameMapper
from sklearn import impute
from sklearn.impute import SimpleImputer
import joblib as jb


# Create your views here.

# from . import service
# from django.http import HttpResponse

# def gett(request):
#         #article_data = service.get_data.all()
#         print(service.article_data)
#         return render(request, 'index.html', article_data)

    
# import os
# import requests
# from requests.auth import HTTPBasicAuth

# def api(request):
#     Company = request.POST.get('Company')
#     Position = request.POST.get('position')

#     url = os.environ.get("URL", 'http://myhost:port/projectname/api/addposition?compName=Google&category=Developer')
#     url = "%s" % (url)
#     body = {"Company" : "%s" % Company, "Position" : "%s" % Position}response = requests.post(url, auth=HTTPBasicAuth('USER', 'PASSWORD'), headers={'Content-Type': 'application/json'}, json=body)
#     if response.status_code == 200:
#         print("Code 200")
#     else:
#         print("Code not 200")

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
import requests
import csv
from . serializers import ApiSerializer
from . models import Apimodel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['POST'])
def saveapi(request):
	if request.method =='POST':
		a=request.data
		print(a)
		data=pd.read_csv('datagas.csv')
		saveserialize= ApiSerializer(data=request.data)
		mapper = DataFrameMapper([(['Quiz','sampletest','playing','sleeping','learning'], preprocessing.StandardScaler())])
		pipeline_obj = pipeline.Pipeline([('mapper',mapper),("model", ensemble.RandomForestRegressor())])
		# data.columns
		X=['Quiz', 'sampletest', 'playing', 'sleeping','learning']
		Y=['Total']
		pipeline_obj.fit(data[X],data[Y].values.ravel())
		#print(pipeline_obj.predict(data[X]))
		jb.dump(pipeline_obj,'RFModelforMPG.pkl')
		modelReload=jb.load('RFModelforMPG.pkl')
		testDtaa=pd.DataFrame({'x':request.data}).transpose()
		print(testDtaa)
		if saveserialize.is_valid():
			saveserialize.save()
			print(request.data)
			return Response(modelReload.predict(testDtaa)[0],status=status.HTTP_201_CREATED)
			return Response(modelReload.predict(testDtaa)[0],status=status.HTTP_400_BAD_REQUEST)
			




# def home(request):
# 	response = requests.get('http://jsonplaceholder.typicode.com/users/')
# 	geodata = response.json()
# 	print([d['id'] for d in geodata if 'id' in d])
# 	print([d['name'] for d in geodata if 'name' in d])
# 	print([d['username'] for d in geodata if 'username' in d])
# 	print([d['email'] for d in geodata if 'email' in d])
# 	out=zip([d['id'] for d in geodata if 'id' in d],[d['name'] for d in geodata if 'name' in d],[d['username'] for d in geodata if 'username' in d],[d['email'] for d in geodata if 'email' in d])
# 	with open('outdatacsv.csv', 'w',newline='') as file:
# 		writer = csv.writer(file)
# 		writer.writerow(['Quiz','sampletest','playing','sleeping','learning'])
# 		writer.writerows([(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),
# 			(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),
# 			(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),
# 			(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),
# 			(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),
# 			(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),
# 			(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),
# 			(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),(2,20,3,2,1),])
# 	return render(request, 'home.html', {'geodata':geodata})

   

def index(request):
    return render(request, 'index.html')





def result(request):
	if request.method == "POST":
		temp={}
		temp['Quiz']=request.POST.get('Quiz')
		print(temp['Quiz'])
		temp['sampletest']=request.POST.get('sampletest')
		temp['playing']=request.POST.get('playing')
		temp['sleeping']=request.POST.get('sleeping')
		temp['learning']=request.POST.get('learning')
		print(temp)
		#headers= {'Content-Type':'application/json'}
		#read= requests.post('http://127.0.0.1:8000/checkapi/',json=temp,headers=headers)
		#home(request)
		data=pd.read_csv('datagas.csv')
		#print(data)
		#quiz= request.POST.get('quiz')
		#print(quiz)
		#context= {'quiz': quiz}
		
	    
		data.head()
		data.isnull().sum()
		#print(data)
		mapper = DataFrameMapper([(['Quiz','sampletest','playing','sleeping','learning'], preprocessing.StandardScaler())])
		pipeline_obj = pipeline.Pipeline([('mapper',mapper),("model", ensemble.RandomForestRegressor())])
		# data.columns
		X=['Quiz', 'sampletest', 'playing', 'sleeping','learning']
		Y=['Total']
		pipeline_obj.fit(data[X],data[Y].values.ravel())
		#print(pipeline_obj.predict(data[X]))
		jb.dump(pipeline_obj,'RFModelforMPG.pkl')
		modelReload=jb.load('RFModelforMPG.pkl')
		#print(modelReload.predict(data[X]))
		#sampledata={1:{'quiz':2,'sampletest':10,'sleep':2,'learn':5},2:{'quiz':2,'sampletest':10,'sleep':2,'learn':5},3:{'quiz':2,'sampletest':10,'sleep':2,'learn':5}}

		#print((temp['Quiz']*2)+ (temp['sampletest']*2)+ (temp['sleeping']*2))
		testDtaa=pd.DataFrame({'x':temp}).transpose()
		#print(testDtaa)
		#print(modelReload.predict(testDtaa)[0])
		return render(request, 'result.html',{'quiz':modelReload.predict(testDtaa)[0]})



class TestView(APIView):
	def get(self,request,*args,**kwargs):
		data=pd.read_csv('datagas.csv')
		mapper = DataFrameMapper([
                        (['Quiz','sampletest','playing','sleeping','learning'], preprocessing.StandardScaler())])
		pipeline_obj = pipeline.Pipeline([('mapper',mapper),("model", ensemble.RandomForestRegressor())])
		X=['Quiz', 'sampletest', 'playing', 'sleeping','learning']
		Y=['Total']
		pipeline_obj.fit(data[X],data[Y].values.ravel())
		pipeline_obj.predict(data[X])
		print(data['id'])
		print(dict(zip(data['id'],pipeline_obj.predict(data[X]))))
		#result(request)
		#outdata="hello python"
		#data = {
		#'name':'vaish',
		# 'age':25
		# }
		
		return Response(dict(zip(data['id'],pipeline_obj.predict(data[X]))))



# class TestView1(APIView):
# 	def get(self,request,*args,**kwargs):
# 		#result(request)
# 		outdata="hello python"
# 		data = {
# 		'name':'vaish',
# 		'age':25
# 		}
# 		return Response(outdata)
