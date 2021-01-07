from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Student, Person
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms


# Create your views here.
# Use of ListView
class StudentListView(ListView):
    model = Student
    # template_name_suffix = '_list'
    template_name = 'school/student_list.html'
    ordering = ['name']


class DefaultTemplateListView(ListView):
    model = Student  # This will fetch all data from the database
    context_object_name = 'students'
    template_name = 'school/student.html'

    # Specially we use addition method to customized the things according to our needs
    def get_queryset(self):
        return Student.objects.filter(course='Data Science')

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['fresher'] = Student.objects.all().order_by('course')
        return context

    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'Anup':
    #         template_name = 'school/anup.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]


# Use of DetailView
class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/student_detail.html'
    context_object_name = 'std'
    # It take id as pk in default but if we want to change to id then
    pk_url_kwarg = 'id'


# Below code is to display all employee name and when click to the particular name it will show detail of employee
class EmployeeListView(ListView):
    model = Student
    template_name = 'school/employee.html'
    context_object_name = 'employee'


class EmployeeDetailView(DetailView):
    model = Student
    context_object_name = 'emp'
    template_name = 'school/employee_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['all_employee'] = self.model.objects.all()
        return context


# Use of FormView
class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm
    success_url = '/thankyou/'


class ThanksTemplateView(TemplateView):
    template_name = 'school/thankyou.html'


# Use of CreateView
class PersonCreateView(CreateView):
    model = Person
    fields = ['name', 'email', 'password']
    template_name = 'school/person_form.html'
    success_url = '/success/'

    # Below method code for form class given
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class': 'name'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'email'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class': 'pass'})
        return form


class SuccessTemplateView(TemplateView):
    template_name = 'school/success.html'


# Use of UpdateView
class PersonUpdateView(UpdateView):
    model = Person
    fields = ['name', 'email', 'password']
    template_name = 'school/person_form.html'
    success_url = '/updated/'

    # Below method code for form class given
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class': 'name'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'email'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class': 'pass'}, render_value=True)
        return form


class ThanksUpdatedView(TemplateView):
    template_name = 'school/update.html'


# Use of DeleteView
class PersonDeleteView(DeleteView):
    model = Person
    success_url = '/create/'
    template_name = 'school/person_confirm_delete.html'
