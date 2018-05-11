from django import forms

from .models import contactusa

class contactusForm(forms.ModelForm):

    class Meta:
        model = contactusa
        widgets = {
            'Type_of_Project': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
            'Tell_Us_About_Your_Project': forms.Textarea(attrs={'cols': 43, 'rows': 12})
        }

        fields = (
                 'Full_Name',
                 'Email',
                 'Phone_Number',
                 'Country',
                 'Type_of_Project',
                 'Estimated_budget',
                 'Tell_Us_About_Your_Project'
        )
