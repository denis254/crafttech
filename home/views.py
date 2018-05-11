from django.shortcuts import render, redirect

from django.contrib import messages

from . forms import contactusForm

# Create your views here.
from django.views.generic import TemplateView

class home(TemplateView):

    template_name = "homepage.html"

class about(TemplateView):

    template_name = "about.html"

class careers(TemplateView):

    template_name = "careers.html"

class webdesign(TemplateView):

    template_name = "webdesign.html"

class seo(TemplateView):

    template_name = "seo.html"

class smo(TemplateView):

    template_name = "smo.html"

class webhost(TemplateView):

    template_name = "webhost.html"

class domain(TemplateView):

    template_name = "domain.html"

class contact(TemplateView):

    template_name = "contact.html"

class contactcomplete(TemplateView):

    template_name = "contactcomplete.html"

class consultancyt(TemplateView):

    template_name = "consultancy.html"

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
