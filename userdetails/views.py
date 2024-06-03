from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm,AddRecordForm
from .models import Record

# Create your views here.
def home(request):
	records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records})
      

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out successfully!")
    return redirect('home')

def register_user(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['user_name']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have been registered successfully!")
            return redirect('home')
    else:
        form=RegisterForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def User_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You must be logged in to view the user records")
		return redirect('home')
	

def delete_record(request,pk):
	if request.user.is_authenticated:
		delete_record = Record.objects.get(id=pk)
		delete_record.delete()
		messages.success(request, "Record has been deleted successfully!")
		return redirect('home')
	else:
		messages.success(request, "You must be logged in to delete the user records")
		return redirect('home')
	
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record added successfully!")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You must be logged in to add the record.")
		return redirect('home')
		
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record has been updated successfully!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You must be logged in to update the record!")
		return redirect('home')
	
		
	