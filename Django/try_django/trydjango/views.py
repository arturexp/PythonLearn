"""
To render html web pages
"""
from django.http import HttpResponse
from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return response)
    """
    article_obj = Article.objects.get(id=2)

    H1_STRING = f"""
    <h1>{article_obj.title}</h1>
    """

    P_STRING = f"""
    <p>{article_obj.content}</p>
    """

    HTML_STRING = H1_STRING + P_STRING

    return HttpResponse(HTML_STRING)
