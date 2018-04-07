from django.shortcuts import render
from template_app.forms import UserForm, UserProfileInfoForm
# Create your views here.


def index(request):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'template_app/index.html', context_dict)


def other(request):
    return render(request, 'template_app/other.html')


def relatives(request):
    return render(request, 'template_app/relatives.html')


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'template_app/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered
                   })
