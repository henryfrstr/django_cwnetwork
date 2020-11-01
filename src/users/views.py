from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages

def profile_view(request):
    obj = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=obj)
    
    if form.is_valid():
        form.save()
        messages.success(request, "Your profile has been updated.")
    
    context = {
        'obj': obj,
        'form': form,
    }
    
    return render(request, 'users/profile.html', context)
