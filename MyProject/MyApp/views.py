from django.views.generic import ListView, DetailView
from .models import Record
# Create your views here.


class RecordListView(ListView):
    model = Record
    template_name = 'record_list.html'
    context_object_name = 'records'
    paginate_by = 10
    ordering = ['-created_at']


class RecordDetailView(DetailView):
    model = Record
    template_name = 'record_detail.html'
    context_object_name = 'record'
