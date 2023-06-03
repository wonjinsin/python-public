from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from users.forms import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/posts/feeds')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # is_valid() 안부르면 cleaned_data 못씀
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/posts/feeds')

        print('로그인에 실패했습니다')
        context = {"form": form}
        return render(request, "users/login.html", context)

    form = LoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)
