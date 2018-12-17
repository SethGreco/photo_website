from django.shortcuts import redirect


def login_redirect(request):
    response = redirect('/hello/login')
    return response
