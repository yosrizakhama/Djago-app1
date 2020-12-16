from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .form import OrderForm
from django.forms import inlineformset_factory

# Create your views here.

def home(request):
    # return HttpResponse('Home page')
    costumers = Customer.objects.all()
    orders = Order.objects.all()
    t_orders = orders.count()
    p_orders = orders.filter(status='Pending').count()
    d_orders = orders.filter(status='Delicered').count()
    in_orders = orders.filter(status='Out of order').count()
    out_orders =orders.filter(status='In Progress').count()
    context = {'customers':costumers,'orders':orders,'count':{'t_orders':t_orders,'p_orders':p_orders,'d_orders':d_orders,'in_orders':in_orders,'out_orders':out_orders}}
    return render(request,'bookstore/dashboard.html', context)

def book(request):
    #return HttpResponse('book page')
    books = Book.objects.all()
    return render(request,'bookstore/profile.html', {'books': books})

def connect(request):
    #return HttpResponse('connect page')
    return render(request,'bookstore/customer.html')

def costumer(request,id):
    #return HttpResponse('connect page')
    costumer=Customer.objects.get(id=id)
    order = costumer.order_set.all()
    nb_orders = order.count()
    context = {'costumer':costumer,'order':order, 'nb_orders':nb_orders}
    return render(request,'bookstore/costumerinfo.html',context)

def create(request):
    form = OrderForm()
    if request.method == 'POST':
        #print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form,'customer':'Customer','status':'Status','tag':'Tag','book':'Book'}
    return render(request,'bookstore/my_order_form.html',context)

def update(request,id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance = order)
    if request.method == 'POST':
        #print(request.POST)
        form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form,'customer':'Customer','status':'Status','tag':'Tag','book':'Book'}
    return render(request,'bookstore/my_order_form.html',context)

def delete(request,id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        #print(request.POST)
        order.delete()
        return redirect('/')
    context = {'order':order}
    return render(request,'bookstore/delete_form.html',context)

def create_inline(request,pk):
    customer = Customer.objects.get(id=pk)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('status','book','tag'), extra = 2)
    formset = OrderFormSet(queryset = Order.objects.none(), instance=customer)
    if request.method == 'POST':
        #print(request.POST)
        formset = OrderFormSet(request.POST, instance = customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request,'bookstore/my_order_form_set.html',context)