from django.shortcuts import render
from django.views import generic

class Home(generic.TemplateView):
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        context = super(Home, self).get_context_data()
        context.update({'my_message': 'Welcome to my site'}) # 画面に渡すデータ
        return render(request, 'home.html', context)