from django.contrib import admin
from django.urls import path,include,re_path,reverse_lazy
from . import views
from .views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



app_name = "user"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.loginuser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    
    path('password_reset/', views.PasswordResetView.as_view(success_url=reverse_lazy(
        'user:password_reset_done' )), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(success_url = reverse_lazy('user:password_reset_complete'))
    , name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)