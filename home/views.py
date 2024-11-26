from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Carousel_Stuff, Order, Frequent_Questions, Payment_Methods, Another_Equal
from .forms import Form_Message, Form_Another_Equal, Register_Form
from catalog.models import Product


def home(request):
    carousel_stuff = Carousel_Stuff.objects.all()
    return render(request, 'index.html', {'car_stuff': carousel_stuff})

def message(request):
    form = Form_Message()
    if request.method == 'POST':
        message = Form_Message(request.POST, request.FILES)
        # message_count = message.count()
        if message.is_valid():
            try:     
                form = Form_Message()     
                alert = 'Hemos recibido tu mensaje! Te enviaremos a tu correo una cotización cuanto antes.'
                message.save()
                return render(request, 'messages.html', {'form': form, 'alert':alert})
            except:
                alert = 'Opps! Parece que algo salió mal...'
                return redirect('index.html')
        else:
            alert = 'no guardado'
            return render(request, 'messages.html', {'form': form, 'alert':alert})
    else:       
        return render(request, 'messages.html', {'form':form})

def orders(request, id):
    order = Product.objects.get(id=id)
    info = Order(name=order.name, price=order.price)
    info.save()
    
    return render(request,'sold_out.html', {'product': order})

def frequent_questions(request):
    questions = Frequent_Questions.objects.all()
    return render(request, 'frequent_questions.html', {'questions': questions})

def payment_methods(request):
    questions = Payment_Methods.objects.all()
    return render(request, 'payment_methods.html', {'payment_methods': questions})

def another_equal(request, id):
    if request.method == 'POST':  
        product = Product.objects.get(id=id)
        email = Form_Another_Equal(request.POST)
        order = Another_Equal(product_ref=product.name, customer_email=email.data['customer_email'])
        alert = 'Hemos recibido tu solicitud, te escribiremos a tu correo cuando el producto esté listo'
        order.save()
        form = Form_Another_Equal()     
        return render(request, 'another_equal.html', {'product': product, 'form':form, 'alert':alert})
  
    else:
        product = Product.objects.get(id=id)
        form = Form_Another_Equal()
        return render(request, 'another_equal.html', {'product': product, 'form':form})

def register_user(request):   
    form = Register_Form()
    if request.method == 'POST':
        new_user = Register_Form(request.POST)
        if new_user.is_valid():
            new_user.save()
            username = new_user.cleaned_data['username']
            password = new_user.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            message = f'{username.capitalize()}'
            return render(request, 'index.html', {'alert': message})
        else:
            message = f'Opps! Parece que algo salió mal...'
            return render(request,'register_user.html', {'form':form, 'alert': message})

    else:       
        return render(request, 'register_user.html', {'form':form})        
