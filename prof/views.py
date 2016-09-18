from django.shortcuts import render

from django.forms import inlineformset_factory
from .models import UserProfile
from .forms import ContactUsForm 
 #,ImageForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.views.generic import DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
        	name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobilenumber = form.cleaned_data['mobile']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form.save()       
            print "i m here"    
            return render(request,'done.html',locals())
        return render(request,'notdone.html',locals())
    else:
        form = ContactUsForm()
    return render(request,'contactus.html',locals())    