from django.views.generic.base import TemplateView


# Страница об авторе
class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'


# Страница "технологии"
class AboutTechView(TemplateView):
    template_name = 'about/tech.html'
