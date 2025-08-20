from django.shortcuts import render,redirect
from django.http import HttpResponse
from IplApp.models import Franchise ,Player,Stadium
from .forms import PlayerForm,StadiumForm,UserForm,ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    return HttpResponse('welcome to IPL App..!!')

def info(request):
    detail=[
        {
          'name':'shashi',
          'course':'python',
          'fees':20000,
          'duration':'5 months'
        },
         {
          'name':'rehan',
          'course':'java',
          'fees':20000,
          'duration':'4 months'
        }
        

    ]
    return HttpResponse(detail)

def create_franchise(request):
    if request.method=='POST':
        name=request.POST.get('name')
        short_name=request.POST.get('short_name')
        owner=request.POST.get('owner')
        coach_name=request.POST.get('coach_name')
        city=request.POST.get('city')
        founded_year=request.POST.get('founded_year')
        logo=request.FILES.get('logo')

        Franchise.objects.create(
            name=name,
            short_name=short_name,
            owner=owner,
            coach_name=coach_name,
            city=city,
            founded_year=founded_year,
            logo=logo
        )
        return redirect('list_franchise')
    else:

       return render(request,'create_franchise.html')
    
def list_franchise(request):
       
       franchises= Franchise.objects.all()
     
       return render(request,'list_franchises.html',{'franchises': franchises})

def franchise_details(request,id):
       
       franchise= Franchise.objects.get(id=id)
     
       return render(request,'franchise_details.html',{'franchise': franchise})


def update_franchise(request,id):
     franchise=Franchise.objects.get(id=id)
     if request.method=='POST':
        name=request.POST.get('name')
        short_name=request.POST.get('short_name')
        owner=request.POST.get('owner')
        coach_name=request.POST.get('coach_name')
        city=request.POST.get('city')
        founded_year=request.POST.get('founded_year')
        logo=request.FILES.get('logo')

        franchise.name=name
        franchise.short_name=short_name
        franchise.owner=owner
        franchise.coach_name=coach_name
        franchise.city=city
        franchise.founded_year=founded_year
        if (logo):
             franchise.logo=logo

        franchise.save()
        return redirect('list_franchise')
          
     else:    
        return render(request,'update_franchise.html',{'franchise':franchise})


def delete_franchise(request,id):
    franchise= Franchise.objects.get(id=id)

    if request.method=='POST':
        franchise.delete() 
        return redirect('list_franchise')
    


def create_player(request):

    if request.method == 'POST':
        if request.FILES.get('photo'):
            form = PlayerForm(request.POST,request.FILES)
            form.save()
        else:   
            form = PlayerForm(request.POST)
            form.save()
        return HttpResponse('Created Succesfully')
    else: 
         form = PlayerForm()
         return render(request,'create_player.html',{'form':form})
    

def list_players(request,franchise_id):
    players= Player.objects.filter(franchise_id=franchise_id)
     
    return render(request,'list_players.html',{'players': players})


def create_stadium(request):
     if request.method == 'POST':
         form=StadiumForm(request.POST)
         if form.is_valid():
            form.save()
            return HttpResponse('created stadium successfully ')    
         else:
            return HttpResponse('Invalid Data')    
     else:    
        form=StadiumForm()
        return render(request,'create_stadium.html',{'form':form})
     

def list_stadiums(request):
    stadiums= Stadium.objects.all()
     
    return render(request,'list_stadiums.html',{'stadiums': stadiums})     

#register the login form
def register_user(request):
   if request.method=='POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user= user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()

            return HttpResponse('Registered User Successfully')
        else:
            return HttpResponse('Invalid Data')  

   else:
        user = UserForm()
        profile = ProfileForm()

        return render(request,'register_user.html',{'user':user,'profile':profile})


def login_user(request):
   if request.method=='POST':
       user_from = AuthenticationForm(request,data=request.POST)
       if user_from.is_valid():
           username = user_from.cleaned_data['username']
           password = user_from.cleaned_data['password']
           user= authenticate(request, username=username, password=password)
           if user is not None:
               login(request,user)
               return redirect('list_franchise')
               
           else:
               return HttpResponse('Incorrect Username or Password')    
       else:
           return HttpResponse('Incorrect Username or Password')    
   else:
       user = AuthenticationForm()
       return render(request,'login.html',{'user':user})