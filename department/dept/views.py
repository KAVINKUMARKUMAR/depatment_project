from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,JsonResponse
from .models import add_department
from django.views.generic import DetailView,UpdateView,DeleteView,ListView,CreateView
from .form import AdddeptForm
from django.urls import reverse_lazy
# Create your views here.

class Adddept(CreateView):
    model = add_department
    template_name = 'add_dept.html'
    form_class = AdddeptForm
    success_url = '/'
class Editdept(UpdateView):
    model = add_department
    template_name = 'edit_dept.html'
    form_class = AdddeptForm
    success_url = '/'
class deldept(DeleteView):
    model = add_department  # Make sure this matches your model name
    template_name = 'confirm_delete.html'  # The template that asks for confirmation
    success_url = '/'
def dept_det(request):
    template = loader.get_template('dept_detial.html')
    context = {
        'depts' : add_department.objects.all()
    }
    return HttpResponse(template.render(context,request))
# views.py
from django.shortcuts import get_object_or_404, render, redirect
from .models import add_department

def conf_del(request, pk):  # ← accept pk here
    dept = get_object_or_404(add_department, pk=pk)

    if request.method == 'POST':
        dept.delete()
        return redirect('dept_det')
    
    return render(request, 'confirm_delete.html', {'dept': dept})
