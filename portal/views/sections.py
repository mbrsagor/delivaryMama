from .views import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SectionView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Section
    form_class = SectionForm
    template_name = 'section/section.html'
    context_object_name = 'section'
    success_url = '/section/'
    success_message = 'The section created.'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SectionDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Section
    template_name = 'common/delete_confirm.html'
    success_url = '/section/'
    success_message = 'The section updated.'