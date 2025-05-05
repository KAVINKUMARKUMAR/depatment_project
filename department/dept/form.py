from django import forms
from .models import add_department

class AdddeptForm(forms.ModelForm):
    class Meta:
        model = add_department
        fields = ["Department_Name", "Department_description"]
        widgets = {
            "Department_Name": forms.TextInput(attrs={'class': 'form', 'placeholder': 'Department Name' ,'style' : 'text-align: center;'}),
            "Department_description": forms.TextInput(attrs={'class': 'form', 'placeholder': 'Description','style' : 'text-align: center;'}),
        }
class EditdeptForm(forms.ModelForm):
    class Meta:
        model = add_department
        fields = ["Department_Name", "Department_description"]
        widgets = {
            "Department_Name": forms.TextInput(attrs={'class': 'form', 'placeholder': 'Department Name' ,'style' : 'text-align: center;'}),
            "Department_description": forms.TextInput(attrs={'class': 'form', 'placeholder': 'Description','style' : 'text-align: center;'}),
        }
