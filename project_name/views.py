from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    '''
    Defines what to display in the home page (index)
    '''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Extra context tags can be defined here
        context['author'] = 'Some Person'
        return context
