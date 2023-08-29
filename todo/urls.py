from django.urls import path
from django.views.generic import TemplateView
from todo.views import RegistrationView,MyLoginView,DashboardView,MyLogoutView,myview,CourseDetail,addtocart,mycart,buynow,deletefromcart,updatequantity,checkout,paypalpage,payment_canceled,payment_done,searchcourse,orderview
from django.conf import settings
from django.conf.urls.static import static

#You can use generic cbv directly in URL file
urlpatterns = [
    path('',TemplateView.as_view(template_name="home.html")),
    path('registration/',RegistrationView.as_view(),name="registration"),
    path('login/',MyLoginView.as_view(),name="login"),
    path('dashboard/',myview,name="dashboard"),
    path('logout',MyLogoutView.as_view(),name="logout"),
    path('details/<pk>',CourseDetail.as_view(),name="details"),
    path('search/',searchcourse,name="search"),
    path('addtocart/<cid>',addtocart,name="addtocart"),
    path('deletefromcart/<cid>',deletefromcart,name="deletefromcart"),
    path('buynow/<cid>',buynow,name="buynow"),
    path('cart/',mycart,name="cart"),
    path('updatequantity/<cid>',updatequantity,name="updatequantity"),
    path('checkout/',checkout,name="checkout"),
    path('paypal/',paypalpage,name='paypal'),
     path('payment-done/', payment_done, name='payment_done'),
    path('payment-cancelled/', payment_canceled, name='payment_cancelled'),
    path('orders',orderview,name="orders")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
