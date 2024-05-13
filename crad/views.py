from django.shortcuts import render, redirect
from  .models import Contact
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Component
from .forms import ComponentForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if len(username)>0 and len(password)>0:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successfull")
                return redirect('home')            
            return render(request,'login.html')
    else: 
        messages.error(request,"Pleas fill your currect details")
        return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.mehtod == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if len(username) < 4:
            messages.error(request, "Invalid username")
        User.objects.create(username=username, email=email, password=password)
        messages.success(request, "Account created successfully")
        return login_view(request)
    return render(request, 'login.html', {
       'register':1
    })

def contact_view(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        if len(name)>0 and len(email)>0 and len(subject)>0 and len(message)>0:
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()
            message.success(request, "your message has been sent successfully!")
            return redirect('contact')
        else:    
            message.error(request,"please fill in all the fields!")
    return render(request,'contact.html')

def components(request):
    return render(request, 'components.html', {
        'components': Component.objects.all()
    })

def component_edit(request,pk):
    c = Component.objects.get(pk=pk)
    form = ComponentForm(instance=c)
    if request.method=='POST':
        form = ComponentForm(request.POST, request.FILES, instance=c)
        if form.is_valid():
            form.save()
            messages.success(request, "component updated successfully")
            return redirect('components')
    return render(request, "component_edit.html", {
        'form': form
    })

def component_delete(request,pk):
    c = Component.objects.get(pk=pk)
    c.delete()
    messages.warning(request, "component deleted")
    return redirect("components")

def component_add(request):
    form = ComponentForm()
    if request.method=='POST':
        form = ComponentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "component added successfully")
            return redirect('components')
    return render(request, "component_add.html", {
        'form': form
    })

def component_view(request, pk):
    try:
        component = Component.objects.get(pk=pk)
        return render(request,'component_view.html',{
            'component' : component
        } )
    except Exception as e:
        messages.error(request, "component do not exists")
        return redirect("components")