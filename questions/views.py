from django.shortcuts import render


def frequently_asked_questions(request):
    return render(request, 'questions/faq.html')
