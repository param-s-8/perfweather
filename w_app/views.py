from django.shortcuts import render,redirect
import requests
from .models import City, DeetCity
from .forms import CityForm, DeetCityForm, FeedbackForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=0207eee93287e4d5666e4548cc55c81a'
    err_msg=''
    msg=''
    msg_class=''
    if request.method=='POST':
        form=CityForm(request.POST)
        if form.is_valid():
            new_city=form.cleaned_data['name']
            city_exist=City.objects.filter(name=new_city).count()
            if city_exist==0:
                r=requests.get(url.format(new_city)).json()
                if r['cod']==200:
                    form.save()
                else:
                    err_msg='No Such City In The World!'
            else:
                err_msg='City Already Exists!'
        if err_msg:
            msg=err_msg
            msg_class='is-danger'
        else:
            msg='City Added Succesfully!'
            msg_class='is-success'
    form = CityForm()
    cities=City.objects.all()
    l_w=[]
    for city in cities:
        r=requests.get(url.format(city)).json()
        city_weather={
            'city':city.name,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        l_w.append(city_weather)
    context = {
        'l_w':l_w,
        'form':form,
        'msg':msg,
        'msg_class':msg_class
        }
    return render(request,'w_app/weather.html',context)

def delete_city(request,city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')

def deet_view(request):
    url1='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=0207eee93287e4d5666e4548cc55c81a'
    city=''
    err_msg=''
    msg=''
    msg_class=''
    form=DeetCityForm()
    if request.method=='POST':
        form=DeetCityForm(request.POST)
        if form.is_valid():
            city=form.cleaned_data['name']
        r1=requests.get(url1.format(city)).json()
        if r1['cod']==200:
            form.save()
        else:
            err_msg='No Such City In The World!'
    if err_msg:
        msg=err_msg
        msg_class='is-danger'
    else:
        msg='City Search Succesful!'
        msg_class='is-success'
    form=DeetCityForm()
    r1=requests.get(url1.format('Mumbai')).json()
    #city=form['name']
    lat=r1['coord']['lat']
    lon=r1['coord']['lon']
    icon=r1['weather'][0]['icon']
    if msg=='No Such City In The World!':
        city=''
    url2='https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=metric&appid=0207eee93287e4d5666e4548cc55c81a'.format(lat,lon)
    r2=requests.get(url2).json()
    hourly_temp=[] 
    hourly_humidity=[]
    mx=[]
    mn=[]
    for i in range(0,5):
        hourly_temp.append(r2['hourly'][i]['temp'])
        hourly_humidity.append(r2['hourly'][i]['humidity'])
        mx.append(r2['daily'][i]['temp']['max'])
        mn.append(r2['daily'][i]['temp']['min'])
    deets={
        'lat':r2['lat'], 'hourly_humidity':hourly_humidity, 'daily_min_temp':mn,
        'lon':r2['lon'], 'hourly_temp':hourly_temp, 'daily_max_temp':mx,
        'tz':r2['timezone'], 'curr_humidity':r2['current']['humidity'], 'curr_clouds':r2['current']['clouds'],
        'icon':icon, 'curr_temp':r2['current']['temp'], 'temp_feel':r2['current']['feels_like'],
    }
    form=DeetCityForm()
    print(city)
    context={
        'deets':deets,
        'city':city,
        'form':form,
        'msg':msg,
        'msg_class':msg_class
        }
    return render(request,'w_app/deets.html',context)

def feedback_form(request):
    if request.method=='POST':
        pDict=request.POST.copy()
        form=FeedbackForm(pDict)
        if form.is_valid():
            form.save()
            form=FeedbackForm()
                       
    else:
        form=FeedbackForm()
    context={'form':form}
    return render(request,'w_app/feedback.html',context)

def aboutUs(request):
    return render(request,'w_app/about.html')