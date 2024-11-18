from django.views.generic import TemplateView
from django.views.generic import DetailView


from .models import *
from .serializers import *

class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['main_photo'] = MainPhoto.objects.first() or None
        context['main_text'] = MainText.objects.first() or None
        context['links'] = Links.objects.all() if Links.objects.exists() else None
        context['articles'] = Article.objects.all() if Article.objects.exists() else None
        context['certificates'] = Certificates.objects.all() if Certificates.objects.exists() else None
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'
    slug_url_kwarg = 'article_slug'

