from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm

# Create your views here.
def home(request):
    list = List.objects.all()
    context = {'list':list}
    return render(request, "list/home.html", context)

def add(request):
    form, success = post_method_task(request)
    
    if (success):
        return redirect('home')

    context = { 'form':form }
    return render(request, "list/add.html", context)

def remove(request, element_id):
    list_element = List.objects.get(id=element_id)
    list_element.delete()
    return redirect("home")

def edit(request, element_id):
    list_element = List.objects.get(id=element_id)
    form, success = post_method_task(request, list_element)

    if (success):
        return redirect('home')

    context = { "form" : form }
    return render(request, 'list/edit.html', context)


def post_method_task(request, inst_elem=None):
    success = False
    if request.method == "POST":
        form = ListForm(request.POST, instance=inst_elem)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = ListForm(instance=inst_elem)

    return form, success