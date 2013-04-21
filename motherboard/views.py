from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from cpu.models import Cpu
from motherboard.models import Motherboard

class MotherboardsView(ListView):
    model = Motherboard
    template_name = 'motherboards.html'

class MotherboardView(DetailView):
    model = Motherboard
    template_name = 'motherboard.html'

    def get_context_data(self, **kwargs):
        context = super(MotherboardView, self).get_context_data(**kwargs)
        context['cpus'] = []
        for socket in context['motherboard'].socket.all():
            context['cpus'].append(Cpu.objects.filter(socket=socket))

        return context
