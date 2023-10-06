from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bosh_sahifa),
    path('bolim/', bolim),
    path('kitoblar/', kitoblar),
    path('tirik_muallif/', tirik_muallif),
    path('register/', register),
    path('login_view/', login_view),
    path('logout_view/', logout_view),
]
