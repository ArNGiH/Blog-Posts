from django.shortcuts import render
from .models import Blog
from .forms import BlogForm, UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.views.decorators.cache import never_cache
# Create your views here.

def index(request):
    return render(request, 'index.html')

def blog_list(request):
    blogs=Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html',{'blogs':blogs})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST , request.FILES)
        if form.is_valid():
            blog =form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect('blog_list')
    
    else:
        form=BlogForm()
    return render(request,'blog_form.html',{'form':form})


@login_required
def blog_edit(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user=request.user)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect('blog_list')
    
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_form.html', {'form': form})

@login_required
def blog_delete(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id,user=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request,'blog_confirm_delete.html',{'blog':blog})
    
    



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('blog_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def about(request):
    return render(request, 'about.html')






from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.cache import never_cache

@never_cache
def contact(request):
    if request.method == 'POST':
        # Get form data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Process the form data (e.g., print it or save it)
        print(f"Name: {name}, Email: {email}, Message: {message}")

        # Add success message to the session
        messages.success(request, 'Message sent successfully!')

        # Redirect after processing to prevent form resubmission
        return redirect('contact')

    # Clear the messages manually after they've been displayed
    response = render(request, 'contact.html')
    for message in messages.get_messages(request):
        str(message)  # Access and mark the message as read
    return response
