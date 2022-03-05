from django.shortcuts import render,redirect
from django.core.mail import send_mail, BadHeaderError
from assignment.models import FileUpload
from .forms import FileForm, LoginForm, SignupForm
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
# Create your views here.

def index(request):
    return redirect('/home')

def home(request):
    if request.user.is_authenticated:
        files = FileUpload.objects.filter(email=request.user).order_by('-createdAt')
    else:
        files = "Please login to view dashboard"
    if request.method == "POST":
        form = FileForm(request.POST, files=request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                uploadform=form.save(commit=False)
                uploadform.email = request.user
                uploadform.save()
                try:
                    send_mail("File Upload done", "File upload done with desc:    "+ uploadform.desc+"    name:   "+str(uploadform.file)+"   on   "+str(uploadform.createdAt), "admin@admin.com", [uploadform.email.email])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            else:
                return redirect("/login")
        else:
            pass
    else:
        form = FileForm()
    return render(request, 'home.html', {"form":form, "files":files})




def signup(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
            
                form.save()
           
                return redirect("/login")
            else:
                pass
        else:
            form = SignupForm()
    
        return render(request, "signup.html", {"form":form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = LoginForm()
        if request.method == 'POST':
            name = request.POST.get('username')
        
            pwd = request.POST.get('password1')
        
            user = authenticate(request, username=name, password=pwd)
        
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                pass
        context = {'form': form}
        return render(request, 'login.html', context)


def signout(request):
    logout(request)
    return redirect('home')


