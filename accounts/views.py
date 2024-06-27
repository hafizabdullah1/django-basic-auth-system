from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def SignUpView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("login"))
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
