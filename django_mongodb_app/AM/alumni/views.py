from django.shortcuts import render

# Create your views here.
# alumni/views.py
from django.shortcuts import render
from .mongo import alumni_collection

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        graduation_year = request.POST.get('graduation_year')

        alumni_collection.insert_one({
            'name': name,
            'email': email,
            'graduation_year': graduation_year
        })

        return render(request, 'register_success.html', {'name': name})

    return render(request, 'register.html')
