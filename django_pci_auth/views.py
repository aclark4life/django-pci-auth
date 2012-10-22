from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django_pci_auth.fields import PasswordField
from django.shortcuts import render

def index(request):
    #return HttpResponse("<h1>django-pci-auth</h1><a href='/admin'>Admin</a>")
    form = ExampleForm()
    #return HttpResponse("<h1>django-pci-auth</h1><a href='/admin'>Admin</a>", form.render())
    if request.method == 'POST': # If the form has been submitted...
        form = ExampleForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = ExampleForm() # An unbound form

    return render(request, 'password.html', {
        'form': form,
    })

class ExampleForm(forms.Form):
    password = PasswordField(label="Password")
