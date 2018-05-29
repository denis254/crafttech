from django.shortcuts import render, redirect

from django.contrib import messages

from . forms import contactusForm

def home(request):
    return render(request, "home.html")

def blog(request):
    return render(request, "blog.html")

def contactcomplete(request):
    return render(request, "contactcomplete.html")

def mobilesolutions(request):
    return render(request, "mobilesolutions.html")

def websolutions(request):
    return render(request, "websolutions.html")

def payment(request):
    return render(request, "payment.html")

def services(request):
    return render(request, "services.html")

def about(request):
    return render(request, "about.html")

def contact(request):

    if request.method == 'POST':

        enquire = contactusForm(request.POST)

        if enquire.is_valid():

            enquiresave = enquire.save()

            enquiresave.save()

            messages.success(request, 'Enquiry submitted successfully.Thank you')

            return redirect('/contactcomplete/')

    else:
        enquire = contactusForm()

    return render(request, 'contact.html', {'enquire':enquire})
