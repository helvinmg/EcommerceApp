from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import View,ListView,DetailView
from django.contrib.auth.views import LoginView,LogoutView
from todo.forms import RegistraionForm
from django.shortcuts import redirect, render
from todo.models import Course,Cart,Orders
from django.contrib import messages
from todo.signals import user_registered
from django.contrib.auth.models import User
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

class RegistrationView(View):
    template_name="registration.html"
    def get(self,request):
        rf=RegistraionForm()
        return render(request,self.template_name,{'form':rf})
    def post(self,request):
        user=RegistraionForm(request.POST)
        if user.is_valid():
            user.save()
            user_registered.send(sender=User,user=request.POST['username'])
            return redirect('/login')
        else:
            messages.error(request,"Passwords do not match")
            return redirect('/registration')
        
class MyLoginView(LoginView):
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy("dashboard")
    def form_invalid(self,form):
        messages.error(self.request,"Invalid Credentials")
        return redirect("/login")

class MyLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy("login")


class DashboardView(ListView):
        template_name="dashboard.html"
        model=Course
    
myview=login_required(DashboardView.as_view())

class CourseDetail(DetailView):
    template_name="productdetail.html"
    model=Course

def searchcourse(request):
    searchterm=request.GET['term']
    searchcat=request.GET['cat']
    if searchcat=="Course":
        courses=Course.objects.filter(cname__icontains=searchterm)
    else:
        courses=Course.objects.filter(creator__icontains=searchterm)
    return render(request,"dashboard.html",{'object_list':courses})

def buynow(request,cid):
    user=request.user
    course=Course.objects.get(id=cid)
    obj=Cart(user=user,course=course,quantity=1)
    obj.save()
    return redirect("/cart")

def addtocart(request,cid):
    user=request.user
    course=Course.objects.get(id=cid)
    c=Cart.objects.filter(id=cid,user=user)
    print(c)
    if c:
        messages.warning(request,"Item already added")
    else:
        obj=Cart(user=user,course=course,quantity=1)
        obj.save()
        messages.warning(request,"Item added successfully")
    return redirect("/details/"+cid)

def deletefromcart(request,cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect("/cart")

def mycart(request):
    user=request.user
    courses=Cart.objects.filter(user=user)
    amount=0
    for course in courses:
         amount=amount+(course.quantity*course.course.cprice)
    content={'items':courses,'amount':amount}
    return render(request,"cart.html",content)

def updatequantity(request,cid):
    user=request.user
    q=request.POST["quantity"]#read the quantity send by ajax
    course=Cart.objects.filter(id=cid,user=user)#find the product in the cart
    course.update(quantity=q)#change quantity in the database
    print("successfully updated")
    return redirect("/cart")

def checkout(request):
    amt=request.GET["total"]
    print(amt)
    user=request.user
    #course=Cart.objects.filter(user=user)
    obj=Orders(user=user,amount=amt)
    #session set
    obj.save()
    return redirect("/paypal")

def paypalpage(request):
    #order_id = request.session.get('order_id')
    user=request.user
    order=Orders.objects.get(user=user)
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': order.amount,
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'INR',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'paypal.html', {'order': order, 'form': form})

@csrf_exempt
def payment_done(request):
    return render(request, 'payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment_cancelled.html')


    
