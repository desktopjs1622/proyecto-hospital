from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect


##############################################################################
'''Se Listara todos los pacientes registrados en el 
hospital
'''
class ListadoPaciente(TemplateView):
    pass


##############################################################################
'''clase para registrar nuevos pacientes en
edades comprendidas que tengan cedula de identidad
laminada los candidatos estan entre los 9 años hasta
los 110 años
'''
class RegistroPacienteView(SuccessMessageMixin, CreateView):

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['form'] = self.form_class
        return contexto
    
    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        if (form.is_valid()):
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):

        form = form.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(
            form=form))

