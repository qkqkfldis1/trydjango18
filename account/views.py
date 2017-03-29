from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def edit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)

        if  profile_form.is_valid():
            profile_form.save()
            return render(request, 'home.html', {})
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'profile_edit.html', {'profile_form': profile_form})