from django.shortcuts import render
from .models import Faqs


def faqs(request):
    """
    Returns all Q&A and render FAQ page.
    """

    faqs = Faqs.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'faqs/faqs.html', context)
