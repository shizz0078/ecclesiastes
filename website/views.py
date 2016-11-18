from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import ContactUs
from .models import ContentManagement
from .forms import ContactUsForm
from  django.contrib import messages
from django.contrib import auth
from django.template.context_processors import csrf

# Create your views here.
def index(request):
	#return HttpResponse("YERP")
	#return HttpResponse(template.render(request))
	cm = ContentManagement.objects.get(id=1)
	return render(request, 'home/index.html', {'cm':cm})

def home(request):
	#return HttpResponse("YERP")
	#return HttpResponse(template.render(request))
	cm = ContentManagement.objects.get(id=1)
	return render(request, 'home/index.html', {'cm':cm})

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

def login(request):
	c ={}
	c.update(csrf(request))
	return render_to_response('login.html', c)