from django.urls import path
from . import views

urlpatterns = [
    path('std/', views.StudentListView.as_view(), name='student'),
    path('std1/', views.DefaultTemplateListView.as_view(), name='student1'),
    path('std2/<int:id>/', views.StudentDetailView.as_view(), name='student2'),
    path('emp/', views.EmployeeListView.as_view(), name='emp'),
    path('emp/data/<int:pk>/', views.EmployeeDetailView.as_view(), name='emp2'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('thankyou/', views.ThanksTemplateView.as_view(), name='thankyou'),
    path('create/', views.PersonCreateView.as_view(), name='create'),
    path('success/', views.SuccessTemplateView.as_view(), name='success'),
    path('update/<int:pk>', views.PersonUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.PersonDeleteView.as_view(), name='delete'),
    path('updated/', views.ThanksUpdatedView.as_view(), name='updated'),
]
