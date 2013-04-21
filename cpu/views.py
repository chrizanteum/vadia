from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from cpu.models import Cpu
from motherboard.models import Motherboard

class CpusView(ListView):
    model = Cpu
    template_name = 'cpus.html'# Create your views here.


class CpuView(DetailView):
    model = Cpu
    template_name = 'cpu.html'# Create your views here.

    def get_context_data(self, **kwargs):
        context = super(CpuView, self).get_context_data(**kwargs)
        context['motherboards'] = Motherboard.objects.filter(
            socket__socket=context['cpu'].socket
        )

        return context
