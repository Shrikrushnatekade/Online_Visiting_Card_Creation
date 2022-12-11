from django.http import HttpResponse
from django.shortcuts import render
from htmlcss.models import Member
from .models import Businesscard, SelfCard
from django.contrib.auth import logout as django_logout
# Create your views here.

def profile(request):
    session = request.session.get('username')
    return render(request, "profile.html",{'usern': session})

def logout(request):
    django_logout(request)
    return HttpResponse("logout")


def createCard(request):
    if request.method == 'POST':
                fullName = request.POST['fullName']
                email = request.POST['email']
                number = request.POST['number']
                street = request.POST['street']
                city = request.POST['city']
                state = request.POST['state']
                country = request.POST['country']
                weurl = request.POST['websiteN']
                busn = request.POST['BusinessN']

                busc1 = Businesscard()

                busc1.name = fullName
                busc1.emailu = email
                busc1.number = number
                busc1.street = street
                busc1.city = city
                busc1.state = state
                busc1.country = country
                busc1.weurl = weurl
                busc1.business = busn

                return render(request, "CreateCard.html", {'busc1': busc1})
    else:
        return render(request, "CreateCard.html")


def createcard2(request):
    if request.method == 'POST':
            fullName = request.POST['fullName']
            email = request.POST['email']
            number = request.POST['number']
            street = request.POST['street']
            city = request.POST['city']
            work = request.POST['work']


            busc1 = Businesscard()

            busc1.name = fullName
            busc1.emailu = email
            busc1.number = number
            busc1.Address = street
            busc1.country = city
            busc1.work = work

            return render(request, "creationcard2.html",{'data':busc1})

    else:
        return render(request, "creationcard2.html")


def creationcard3(request):
    if request.method == 'POST':
        fullName = request.POST['fullName']
        email = request.POST['email']
        number = request.POST['number']
        twitter = request.POST['twitter']
        website = request.POST['website']
        work = request.POST['work']

        busc1 = Businesscard()

        busc1.name = fullName
        busc1.emailu = email
        busc1.number = number
        busc1.twitter = twitter
        busc1.website = website
        busc1.work = work

        return render(request, "businessinfo3.html",{'data':busc1})
    else:
        return render(request, "businessinfo3.html")


def selfcard(request):
    if request.method == "POST":
        data = SelfCard()
        data.username = request.POST.get("name")
        data.email1 = request.POST.get("email")
        data.place = request.POST.get("place")
        data.shopname = request.POST.get("shopname")
        data.number = request.POST.get("number")
        data.fb = request.POST.get("fb")

        if len(request.FILES) != 0:
            data.userimg = request.FILES['image']
        data.save()

        # fm = SelfCard.objects.all()

        return render(request, "self_card.html", {'fm' : data})
    else:
        return render(request, "self_card.html")
    
def card4(request):
    if request.method == 'POST':
        fullName = request.POST['fullName']
        email = request.POST['email']
        number = request.POST['number']
        city = request.POST['city']
        work = request.POST['work']

        busc1 = Businesscard()

        busc1.name = fullName
        busc1.emailu = email
        busc1.number = number
        busc1.city = city
        busc1.work = work

        return render(request,'card4.html',{'data': busc1})
    else:
        return render(request,'card4.html')

def service(request):
    return render(request,'service.html')