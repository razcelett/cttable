from django.shortcuts import render
from django.shortcuts import redirect, render
from .forms import CustomPasswordChangeForm


# Create your views here.

def change_password(request):
    context = { 'segment': 'change-password' }
    context['form'] = CustomPasswordChangeForm(user=request.user)

    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            print(f'form is valid: {form}')
            form.save()
            return redirect("/")
        else:
            print(f'form is invalid: {form}')
            context['form'] = form
            return render(request, 'change-password.html', context)

    return render(request, 'change-password.html', context)