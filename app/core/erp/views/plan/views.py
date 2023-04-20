from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import PlanForm
from core.erp.models import Plan


class PlanListView(ListView):
    model = Plan
    template_name = 'plan/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Planes'
        context['create_url'] = reverse_lazy('erp:plan_create')
        context['list_url'] = reverse_lazy('erp:plan_list')
        context['entity'] = 'Plan'
        return context


class PlanCreateView(CreateView):
    model = Plan
    form_class = PlanForm
    template_name = 'plan/create.html'
    success_url = reverse_lazy('erp:plan_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Plan'
        context['entity'] = 'Plan'
        context['list_url'] = reverse_lazy('erp:plan_list')
        context['action'] = 'add'
        return context


class PlanUpdateView(UpdateView):
    model = Plan
    form_class = PlanForm
    template_name = 'plan/create.html'
    success_url = reverse_lazy('erp:plan_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Plan'
        context['entity'] = 'Plan'
        context['list_url'] = reverse_lazy('erp:plan_list')
        context['action'] = 'edit'
        return context


class PlanDeleteView(DeleteView):
    model = Plan
    template_name = 'plan/delete.html'
    success_url = reverse_lazy('erp:plan_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Plan'
        context['entity'] = 'Plan'
        context['list_url'] = reverse_lazy('erp:plan_list')
        return context
