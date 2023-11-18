from django.shortcuts import render, redirect
from .forms import  RegTableForm, LoginForm, FileUploadForm
from .models import RegTable, File 

#First created registration
def registration_view(request):
    if request.method == 'POST':
        form = RegTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redirect to the correct URL pattern name
    else:
        form = RegTableForm()
    return render(request, 'registration.html', {'form': form})

#second created after registration
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = RegTable.objects.get(username=username, password=password)
                print("Successfully logged in")
                
                request.session['user_name'] = user.name #Bring this data across other sites, so from login view check data and bring the name to homepage.html  
                return redirect('homepage_view')
            
            except RegTable.DoesNotExist:
                print("Invalid username or password")
                
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def homepage_view(request):
    user_name = request.session.get('user_name', None)

    if user_name:
        if request.method == 'POST':
            form = FileUploadForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                print("File uploaded successfully")
                return upload_success_logic(request)

        else:
            form = FileUploadForm()

        uploaded_files = File.objects.all()
        return render(request, 'homepage.html', {'user_name': user_name, 'form': form, 'uploaded_files': uploaded_files})
    else:
        return redirect('login')
    
def upload_success_logic(request):
    user_name = request.session.get('user_name', None)
    uploaded_files = File.objects.all()  # Get the list of uploaded files
    print("uploaded success")
    return render(request, 'homepage.html', {'user_name': user_name, 'uploaded_files': uploaded_files, 'upload_success': True})
