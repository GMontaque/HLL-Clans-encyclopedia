# profiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages

def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            return redirect('password_reset_form', user_id=user.id)
        except User.DoesNotExist:
            messages.error(request, 'Email address not found.')
            return redirect('password_reset_request')
    return render(request, 'account/password_reset.html')

def password_reset_form(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'User not found.')
        return redirect('password_reset_request')

    if request.method == "POST":
        new_password = request.POST.get('new_password')
        user.set_password(new_password)
        user.save()
        messages.success(request, 'Password updated successfully.')
        return redirect('account_login')

    return render(request, 'password_reset_form.html', {'user': user})
