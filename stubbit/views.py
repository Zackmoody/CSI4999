from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate, logout
from django.http import HttpResponse
from django.template import loader
from .models import *
from .backend import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, OrganizationForm
from django.contrib.messages import *

from .forms import CreateUserForm
from django.contrib import messages

def index(request):
    outputHTTP_string = ""
    
    Backend.WipeStubAttachments()
    Backend.WipeStubs()
    Backend.WipeUserMetas()
    Backend.WipeUserPasses()
    Backend.WipeUsers()
    Backend.WipeOrganizations()
    Backend.WipeLicenses()
    
    Backend.CreateTestLicenses()
    Backend.CreateTestOrganizations()
    Backend.CreateTestUsers()
    Backend.CreateTestUserPasses()
    Backend.CreateTestUserMetas()
    Backend.CreateTestStubs()
    Backend.CreateTestStubAttachments()
    
    outputHTTP_string = Backend.PrintLicenses() + "\n\n\n" + Backend.PrintOrganizations() + "\n\n\n" + Backend.PrintUsers() + "\n\n\n" + Backend.PrintUserPasses() + "\n\n\n" + Backend.PrintUserMetas() + "\n\n\n" + Backend.PrintStubs() + "\n\n\n" + Backend.PrintStubAttachments()
    
    return HttpResponse(outputHTTP_string, content_type="text/plain")

def home(request):
    
    Backend.WipeStubAttachments()
    Backend.WipeStubs()
    Backend.WipeUserMetas()
    Backend.WipeUserPasses()
    Backend.WipeUsers()
    Backend.WipeOrganizations()
    Backend.WipeLicenses()
    
    Backend.CreateTestLicenses()
    Backend.CreateTestOrganizations()
    Backend.CreateTestUsers()
    Backend.CreateTestUserPasses()
    Backend.CreateTestUserMetas()
    Backend.CreateTestStubs()
    Backend.CreateTestStubAttachments()

    all_stubs = Stub.objects.all()
    user = UserFile.objects.all()[0]
    stub_inprocess = Stub.objects.filter(InProcess=True).get(DeveloperUserFileID=user.pk)
    dict = {'all_stubs':all_stubs, 'user_stubs':all_stubs.filter(IssuerUserFileID=user.pk), 'stub_inprocess':stub_inprocess}
    return render(request, 'home.html', dict)

def signup(request):
    if request.method == 'POST' :
        username = request.POST['username']
        firstname = request.Post['firstname']
        lastname = request.Post['lastname']
        email = request.POST['email_address']
        password2 = request.POST['password2']
        password1 = request.POST['password1']
        licenseKey = request.POST['license_key']
        department = request.POST['department']
        administrator = request.Post['admin']
#Database Username is a SQL Queries to see if it has been taken
        if Check_UserName_Availability(username):
            messages.error(request, "Username already taken")
        else:
            if password1 == password2:
#All data needs to be taken and place into the Database here 
                organization = Organization.objects.filter(LicenseID=licenseKey)
                newUser = UserFile(Username=username, FirstName=firsname, LastName=lastname, Email=email, OrganizationID=organization.OrganizationID, Department=department, Administrator=administrator)           
                newUser.save()
                messages.success(request, "Your Account has been successfully created")
                return redirect('/login/')
            else:
                messages.error(request, "Your passwords do not match!")
                return redirect('/signup/')
    return render(request, 'signup.html')
     
 
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
#I don't know how to connect this username with the password.
        user = UserFile.objects.get(Username=username)
        ActiveUser = user
        userPassword = UserPass.objects.get(EncryptedPassword=password)
        if user is not None: 
            if userPassword is not None:
                return redirect('/')
            else:
                messages.error(request, "Incorrect Credentials! Please makes sure your username and password are correct!")
                return redirect ('/login/')
    else:
        return render(request, 'login.html')

def profile(request):

    return render(request, 'profile.html')

def AddOrganization(request):

    form = OrganizationForm()
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'organization.html', context)

    user = Backend.PrintUsers()
    print('USER:', user)
    context = {
        'user':user
    }
    return render(request,'profile.html', context)

def createstub(request):
     if request.method == 'POST' :
        stubtitle = request.POST['stubTitle']
        stuboverview = request.Post['stubOverview']
        stubcategory = request.Post['StubCategory']
        stuburgency = request.POST['stubUrgency']
        stubdomain = request.POST['stubDomain']
        attachments = request.POST['attachments']
        developer = request.POST['developer']
        newstub = Stub(Title=stubtitle, Overview=stuboverview, Category=stubcategory, Urgency=stuburgency, Domain=stubdomain, IssuerUserFileID=UserFile.objects.get(Username=ActiveUser), DeveloperUserFileID=UserFile.objects.get(Username=developer), StartDate=timezone.now(), EstimatedCompletionTime="1", EstimatedCompletionTimeUOM="Days", PriorityInQueue=1.0, InProcess=True, Completed=False, CreationDate=timezone.now())
     return render(request, 'createstub.html')

