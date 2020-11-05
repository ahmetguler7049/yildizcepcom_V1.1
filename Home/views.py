from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils.safestring import mark_safe


def index(request):
    form = emailFormu(request.POST or None)
    context = {
        'form': form
    }
    if "sentMessage" in request.POST:
        if form.is_valid():
            emailField = form.cleaned_data.get("emailField")
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            email = EmailMessage(
                subject=subject,
                body=message,
                reply_to=[emailField],
                to=[settings.DEFAULT_FROM_EMAIL],
            )
            email.send()
            messages.success(request, mark_safe('Mesajınız Başarıyla İletildi'))
            return redirect("Home")
        else:
            return render(request, "Home/index.html", context=context)

    return render(request, "Home/index.html", context=context)

# Create your views here.
