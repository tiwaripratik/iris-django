from django.http import HttpResponse
from django.shortcuts import render
import pickle


def home(request):
	return render(request,"home.html")

def result(request):
	model = pickle.load(open('model.pkl','rb'))

	lis = []

	lis.append(request.GET['sl'])
	lis.append(request.GET['sw'])
	lis.append(request.GET['pl'])
	lis.append(request.GET['pw'])

	print(lis)

	ans = model.predict([lis])

	x = ['setosa', 'versicolor', 'virginica']

	ans = x[ans[0]]

	return render(request,"result.html",{'ans':ans})