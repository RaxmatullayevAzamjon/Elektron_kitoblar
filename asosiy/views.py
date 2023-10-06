from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from .models import *



def bosh_sahifa(request):
    return render(request,"bosh_sahifa.html")


def bolim(request):
    content = {
        "bolimlar": Bolim.objects.all()
    }
    return render(request,"bolimlar.html",content)

def kitoblar(request):
    if request.method == "POST":
        Kitob.objects.create(
            nom=request.POST.get("n"),
            muallif=Muallif.objects.get(id=request.POST.get("m")),
            yil=request.POST.get("y"),
            bolim=Bolim.objects.get(id=request.POST.get("b")),
            user=User.objects.get(id=request.POST.get("u")),
            rasm=request.POST.get("r")
        )
        return redirect("/kitoblar/")
    content = {
        "kitoblar": Kitob.objects.all(),
        "mualliflar": Muallif.objects.all(),
        "bolimlar": Bolim.objects.all(),
        "userlar": User.objects.all()
    }
    return render(request,"kitoblar.html",content)


def tirik_muallif(request):
    content = {
        "kitoblar": Kitob.objects.filter(muallif__tirik=True)
    }
    return render(request,"tirik_muallif.html",content)

def register(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST.get('login'),
            password=request.POST.get('parol')
        )
        return redirect("/")
    return render(request,"tekshiruv/register.html")


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get("login"),
            password=request.POST.get("parol")
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/rejalar/")
    return render(request,"tekshiruv/login.html")

def logout_view(request):
    logout(request)
    return redirect('/')
