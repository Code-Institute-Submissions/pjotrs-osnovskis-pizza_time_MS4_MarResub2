from django.shortcuts import render

def user_profile(request):
    """ Display users profile. """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)    