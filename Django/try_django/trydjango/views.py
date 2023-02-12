"""
To render html web pages
"""
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return response)
    """
    article_obj = Article.objects.get(id=2)

    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    HTML_STRING = render_to_string("home-view.html", context=context)

    # HTML_STRING = """
    # <h1>{title} ({id})!</h1>
    # <p>{content}!</p>
    # """.format(**context)
    return HttpResponse(HTML_STRING)
