# profiles/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordResetRequestForm, PasswordChangeForm


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            return redirect('password_change', uidb64=uid, token=token)
    else:
        form = PasswordResetRequestForm()
    return render(request, 'account/password_reset.html', {'form': form})


def password_change(request, uidb64=None, token=None):
    if uidb64 and token:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
        if default_token_generator.check_token(user, token):
            if request.method == "POST":
                form = PasswordChangeForm(request.POST)
                if form.is_valid():
                    new_password = form.cleaned_data['new_password']
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)
                    messages.success(
                        request,
                        'Your password has been reset successfully.'
                    )
                    return redirect('index')
            else:
                form = PasswordChangeForm(initial={'username': user.username})
            return render(
                request,
                'account/password_change.html',
                {'form': form}
            )
    messages.error(
        request,
        'The password reset link is invalid or has expired.'
    )
    return redirect('password_reset_request')
