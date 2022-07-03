from .views import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NoticeView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notice/notice.html'
    context_object_name = 'notice'
    success_url = '/notice/'
    success_message = 'Notice created'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NoticeDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Notice
    template_name = 'common/delete_confirm.html'
    success_url = '/notice/'
    success_message = 'Notice deleted'