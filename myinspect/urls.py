from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import add_visitor, visitor_list


urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact_us'), 
    path("login/", views.login_view, name="login_view"),  # Custom login route
    path("visitor_form/", add_visitor, name="visitor_form"),
    path("visitor_list/", visitor_list, name="visitor_list"),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('visitor_list/', views.visitor_list, name='visitor_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)