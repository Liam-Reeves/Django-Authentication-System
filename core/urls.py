from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.Home_View, name='home'),
    path('register/',views.Register_View, name='register'),
    path('login/',views.Login_View, name='login'),
    path('logout/',views.Logout_View, name='logout'),
    path('profile/',views.Profile_View, name='profile'),
    
    
]+static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)