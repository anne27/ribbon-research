# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
import numpy as np
import pandas as pd
import csv
from sklearn import svm
from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

s=""
finallist=[]
mylist=[]

def choose_option(mystring):
	if (mystring=="Yes"):
  		return(1)
  	else:
  		return (0)

def home(request):
	global mylist
	finallist=[]
	finallist.append(mylist)
	if (ml_script(finallist)==0):
		s="Result: Negative"
	else:
		s="Result: Positive"
	return HttpResponse(s)
	#return HttpResponse(ml_script([[23, 2, 17, 3, False, 0, 0, False, 2, False, 0, False, 0, False, False, False, False, False, False, False, False, False, False, False, False, 0, 6, 5, 0, 0, 0, 0]]))

def uform(request):
	return render(request, "index.html")

def services(request):	
	return render(request, "services.html")

@csrf_exempt
def product(request):	
	global mylist
	username=""
	password=""

	if request.method == 'POST':
  		mylist.append(int(request.POST['i0']))
  		mylist.append(int(request.POST['i1']))
  		mylist.append(int(request.POST['i2']))
  		mylist.append(int(request.POST['i3']))
  		mylist.append(choose_option(request.POST.get('b4', None)))
  		mylist.append(int(request.POST['i5']))
  		mylist.append(int(request.POST['i6']))
  		mylist.append(choose_option(request.POST.get('b7', None)))
		mylist.append(int(request.POST['i8']))
		mylist.append(choose_option(request.POST.get('b9', None)))
		mylist.append(int(request.POST['i10']))
		mylist.append(choose_option(request.POST.get('b11', None)))
		mylist.append(int(request.POST['i12']))
		mylist.append(choose_option(request.POST.get('b13', None)))
		mylist.append(choose_option(request.POST.get('b14', None)))
		mylist.append(choose_option(request.POST.get('b15', None)))
		mylist.append(choose_option(request.POST.get('b16', None)))
		mylist.append(choose_option(request.POST.get('b17', None)))
		mylist.append(choose_option(request.POST.get('b18', None)))
		mylist.append(choose_option(request.POST.get('b19', None)))
		mylist.append(choose_option(request.POST.get('b20', None)))
		mylist.append(choose_option(request.POST.get('b21', None)))
		mylist.append(choose_option(request.POST.get('b22', None)))
		mylist.append(choose_option(request.POST.get('b23', None)))
		mylist.append(choose_option(request.POST.get('b24', None)))
		mylist.append(int(request.POST['i25']))
		mylist.append(int(request.POST['i26']))
		mylist.append(int(request.POST['i27']))
		mylist.append(choose_option(request.POST.get('b28', None)))
		mylist.append(choose_option(request.POST.get('b29', None)))
		mylist.append(choose_option(request.POST.get('b30', None)))
		mylist.append(choose_option(request.POST.get('b31', None)))

  		print(mylist)
  		#return HttpResponseRedirect("/home")

		#s=str(i0)+str(i1)+str(i2)+str(selected_option)
		#print s
		#print "Ash"
	
	return render(request, "product.html")

def findmean(val,col):
    s=0
    n=0
    for i in range (len(val)):
        if (val[i][col]=='?'):
            continue
        else:
            s+=float(val[i][col])
            n+=1
    print s/n
    return (s/n)

def svc_param_selection(X, y, nfolds):
    Cs = [0.001, 0.01, 0.1, 1, 10]
    gammas = [0.001, 0.01, 0.1, 1]
    param_grid = {'C': Cs, 'gamma' : gammas}
    grid_search = GridSearchCV(svm.SVC(kernel='rbf'), param_grid, cv=nfolds)
    grid_search.fit(X, y)
    grid_search.best_params_
    return grid_search.best_params_        

def ml_script(given):
	#Open the csv file
	df = pd.read_csv('risk_factors_cervical_cancer.csv')
	#names=df.Names
	#with open('risk_factors_cervical_cancer.csv','r') as csvfile:
	    
	#Split the data into 80-20 training-testing partition.
	sss = StratifiedShuffleSplit(n_splits=3, test_size=0.2, random_state=0)
	sss.get_n_splits(df)
	val=df.values

	meancols=[]
	for x in range(28):
	    meancols.append(findmean(val,x))

	    
	'''
	Index([u'Age',  0--LONG
	    u'Number of sexual partners',   1--INT
	    u'First sexual intercourse',    2--INT
	       u'Num of pregnancies',       3--INT
	       u'Smokes',                   4--BOOL
	       u'Smokes (years)',           5--INT
	       u'Smokes (packs/year)',      6--INT
	       u'Hormonal Contraceptives',  7--BOOL
	       u'Hormonal Contraceptives (years)',  8--INT
	       u'IUD',                      9--BOOL
	       u'IUD (years)',              10--INT
	       u'STDs',                     11--BOOL
	       u'STDs (number)',            12--INT
	       u'STDs:condylomatosis',      13--BOOL
	       u'STDs:cervical condylomatosis', 14--BOOL
	       u'STDs:vaginal condylomatosis',  15--BOOL
	       u'STDs:vulvo-perineal condylomatosis',   16--BOOL
	       u'STDs:syphilis',            17--BOOL
	       u'STDs:pelvic inflammatory disease', 18--BOOL
	       u'STDs:genital herpes',      19--BOOL
	       u'STDs:molluscum contagiosum',   20--BOOL
	       u'STDs:AIDS',                21--BOOL
	       u'STDs:HIV',                 22--BOOL
	       u'STDs:Hepatitis B',         23--BOOL    
	       u'STDs:HPV',                 24--BOOL
	       u'STDs: Number of diagnosis',    25--INT
	       u'STDs: Time since first diagnosis', 26--INT
	       u'STDs: Time since last diagnosis',  27--INT
	       u'Dx:Cancer',                28--BOOL
	       u'Dx:CIN',                   29--BOOL
	        u'Dx:HPV',                  30--BOOL
	        u'Dx',                      31--BOOL
	        u'Hinselmann',              OUTPUT
	        u'Schiller',                OUTPUT
	       u'Citology',                 OUTPUT
	       u'Biopsy'],dtype='object')   OUTPUT      '''

	#print('vaallllll')
	#print(val)
	for i in range(len(val)):               #ith row
	    for j in range(1,28):               #jth col
	        if (j==1 or j==2 or j==3 or j==5 or j==6 or j==8 or j==10 or j==12 or j==25 or j==26 or j==27):
	            if (val[i][j]=='?'):          #? or missing value
	                val[i][j]=meancols[j]               #Replace missing value with mean of that column.
	            val[i][j]=float(val[i][j])
	            val[i][j]=int(val[i][j])
	        elif (j==4 or j==7 or j==9 or j==11 or (j in range(13,25)) or (j in range(28,32))):
	            if (val[i][j]=='?'):
	                val[i][j]=0
	            val[i][j]=float(val[i][j])
	            val[i][j]=int(val[i][j])
	            val[i][j]=bool(val[i][j])
	               
	                        
	x=[]
	y1=[]       #Hinselmann
	y2=[]       #Schiller
	y3=[]       #Citology
	y4=[]       #Biopsy

	for i in range (0,len(val)):
	    x.append(val[i][0:32])
	    y1.append(val[i][32])
	    y2.append(val[i][33])
	    y3.append(val[i][34])
	    y4.append(val[i][35])

	x=np.array(x)
	y1=np.array(y1)

	for i in range (len(x)):
	    x[i][0]=x[i][0]

	for train_index, test_index in sss.split(x, y1):
	    print("TRAIN:", train_index, "TEST:", test_index)
	    X_train, X_test = x[train_index], x[test_index]
	    y_train, y_test = y1[train_index], y1[test_index]

	#clf=LinearSVC(random_state=0,max_iter=1000,C=0.35,penalty='l1')
	#clf=LinearSVC()
	#clf=clf.fit(X_tr,y)
	#predictions=clf.predict(X_tr2[0:72427])
	parameters = {'kernel':('linear', 'rbf'), 'C':[0.1, 10]}
	svc = svm.SVC()
	clf = GridSearchCV(svc, parameters)
	clf.fit(X_train, y_train)
	myscore=clf.score(X_test,y_test)
	ar=clf.predict(X_test)
	ans=clf.predict(given)

	return (ans)
