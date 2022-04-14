from django.contrib import admin
from django.urls import path, re_path,  include
from rest_framework.routers import DefaultRouter
from supermarket_api.routers import router as r1
from account_api.routers import router as r2
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.registration.views import (
    RegisterView, VerifyEmailView,
    ConfirmEmailView, ResendEmailVerificationView
    )


router = DefaultRouter()
router.registry.extend(r1.registry)
router.registry.extend(r2.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    #login,logout,... url patterns incluse:
    #/login/  
    #/logout/
    #/password/change/
    #/user/  return user info, can change username, firstname, lastname 
    path('', include('dj_rest_auth.urls')),
    #overwrite reset-password urls
    path('password-reset/', PasswordResetView.as_view()),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),

    #registeration urls
    path('register/', RegisterView.as_view()),  
    path('resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
         VerifyEmailView.as_view(), name='account_confirm_email'),
    #Unnecessary, for confirm email with post method
    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),

]

urlpatterns += router.urls


