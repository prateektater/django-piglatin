from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def translate(request):
	original = request.GET['original']

	translation = ''
	for word in original.split():
		if word[0] in ['a', 'e', 'i', 'o', 'u']:
			translation += word
			translation += 'yay'

		else:
			translation += word[1:]
			translation += word[0]
			translation += ay

			translation += 'consonant'
	return render(request, 'translate.html')