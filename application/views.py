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


from django.shortcuts import render
import requests

def home(request):
    response = requests.get('http://jsonplaceholder.typicode.com/users/')
    geodata = response.json()
    

    return render(request, 'home.html', {'geodata':geodata})

def index(request):
    return render(request, 'index.html')





def result(request):
	data=pd.read_csv('datagas.csv')
	print(data)
	quiz= request.POST.get('quiz')
	print(quiz)
	#context= {'quiz': quiz}
	
    
	data.head()
	data.isnull().sum()
	print(data)
	mapper = DataFrameMapper([(['Quiz','sampletest','playing','sleeping','learning'], preprocessing.StandardScaler())])
	pipeline_obj = pipeline.Pipeline([('mapper',mapper),("model", ensemble.RandomForestRegressor())])
	# data.columns
	X=['Quiz', 'sampletest', 'playing', 'sleeping','learning']
	Y=['Total']
	pipeline_obj.fit(data[X],data[Y].values.ravel())
	print(pipeline_obj.predict(data[X]))
	jb.dump(pipeline_obj,'RFModelforMPG.pkl')
	modelReload=jb.load('RFModelforMPG.pkl')
	print(modelReload.predict(data[X]))
	temp={}
	temp['Quiz']=request.POST.get('quiz')
	temp['sampletest']=request.POST.get('sample')
	temp['playing']=request.POST.get('playing')
	temp['sleeping']=request.POST.get('sleeping')
	temp['learning']=request.POST.get('learning')
	testDtaa=pd.DataFrame({'x':temp}).transpose()
	print(testDtaa)
	print(modelReload.predict(testDtaa)[0])
	return render(request, 'result.html',{'quiz':modelReload.predict(testDtaa)[0]})