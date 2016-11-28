from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import ContactUs
from .models import ContentManagement
from .models import ContactStatus
from .forms import ContactUsForm, ContactStatusForm
from  django.contrib import messages
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

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

def logout(request):
	auth.logout(request)
	return render(request, 'registration/logout.html')
	#return render(request, 'registration/logout.html')
	#return render(request, 'logout/index.html')

@login_required#(login_url="login/")
def followup(request):
	followup_on_contacts = ContactStatusForm(request.POST or None)
	return render(request, "followup/index.html", {'followup_on_contacts':followup_on_contacts})