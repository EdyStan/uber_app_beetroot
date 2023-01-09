from django.shortcuts import render


def first_page(request):
    return render(request, 'main_app/main_page.html', {})
