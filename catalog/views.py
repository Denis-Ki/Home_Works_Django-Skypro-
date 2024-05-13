from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name)
        print(phone)
        print(message)
    return render(request, "contacts.html")