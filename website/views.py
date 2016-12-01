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
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views import generic
from django.core.urlresolvers import reverse_lazy

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

@login_required(login_url="login/")
def followup(request):
	followup_on_contacts = ContactStatusForm(request.POST or None)
	if followup_on_contacts.is_valid():
		save_it = followup_on_contacts.save(commit = False)
		save_it.save()
		followup_on_contacts = ContactStatusForm()
		messages.success(request, 'Follow details have been saved')
		return render(request, "followup/followup.html",{'followup_on_contacts':followup_on_contacts})
	return render(request, "followup/followup.html", {'followup_on_contacts':followup_on_contacts})

class FollowUpDetailView(generic.DetailView):
	model = ContactStatus
	template_name = "followup/detail.html"

class FollowUpUpdateView(generic.edit.UpdateView):
	model = ContactStatus
	fields = ['contact_id', 'followup_completed', 'date_completed', 'notes', 'priority']
	success_url = reverse_lazy('home')
	#success_url = "/index.html"
	#template_name = "followup/edit.html"
	

class FollowUpEditView(generic.edit.FormView):
	form_class = ContactStatusForm
	template_name = "followup/edit.html"
	success_url = "/index.html"
	def form_valid(self, form):
		form.save()
		return super(FollowUpEditView, self).form_valid(form)

#@login_required#(login_url="login/")
#def followup(request):
#	followup_on_contacts = ContactStatusForm(request.POST or None)
#	if followup_on_contacts.is_valid():
#		save_it = followup_on_contacts.save(commit = False)
#		save_it.save()
#		followup_on_contacts = ContactStatusForm()
#		messages.success(request, 'Follow details have been saved')
#		return render(request, "followup/index.html",{'followup_on_contacts':followup_on_contacts})
#	return render(request, "followup/index.html", {'followup_on_contacts':followup_on_contacts})

#class FollowupListView(ListView):
#	model = ContactStatus
#	def get_context_data(self, **kwargs):
#		context = super(FollowupListView, self).get_context_data(**kwargs)
#		return context