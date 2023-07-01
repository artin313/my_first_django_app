#from django.http import HttpResponse

#def homePageView(request):
    #return HttpResponse('hello ekipa ja nisem djangos')

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class about(TemplateView):
    template_name = 'about.html'