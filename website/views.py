from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactUs
from .forms import ContactUsForm
from  django.contrib import messages

# Create your views here.
def index(request):
	#return HttpResponse("YERP")
	#return HttpResponse(template.render(request))
	return render(request, 'home/index.html')

def home(request):
	#return HttpResponse("YERP")
	#return HttpResponse(template.render(request))
	return render(request, 'home/index.html')

def contact(request):
	#return HttpResponse("YERP")
	#return HttpResponse(template.render(request))
	form = ContactUsForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		form = ContactUsForm()
		messages.success(request,'Thank you, we will contact you soon')
		return render(request, 'contact/index.html')
		
	return render(request, 'contact/index.html', {'form':form})