from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from  blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def home(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'home/home.html', context)
    # return HttpResponse('This is home')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact(name=name, email=email, phone=phone, content=content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5:
            messages.error(request, "Please fill the form correctly.")
        else:
            contact.save()
            messages.success(request, "Your form has been submitted successfully.")
        print(name, email, phone, content)
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    # allPosts = Post.objects.all()
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent).union(allPostsAuthor)
    if allPosts.count() == 0:
        messages.warning(request, "No search result found, please refine your query.")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

# Authentication APIs
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        # Check for errorneous inputs
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')
        if not username.isalnum():
            messages.error(request, "Username must have letters and numbers")
            return redirect('/')
        if password != cpassword:
            messages.error(request, "password and confirm password do not match")
            return redirect('/')
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your iCodedr account has been successfully created.")
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
        else:
            messages.error(request, "Invalid Credentials, please try again")
    else:
        return HttpResponse('404 - Not Found')

    return redirect("home")  # use / or home

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("home")