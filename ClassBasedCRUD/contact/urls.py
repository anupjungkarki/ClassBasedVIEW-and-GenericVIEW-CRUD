from django.urls import path
from . import views

app_name = "DjangoFormCrud"
urlpatterns = [
    # path('create', views.index, name="create"),
    path('create', views.InsertView.as_view(), name='create'),
    # path('view', views.view, name="view"),
    path('view', views.FetchDataView.as_view(), name="view"),
    # path('delete/<int:id>', views.destroy, name="delete"),
    path('delete/<int:id>', views.DeleteDataView.as_view(), name="delete"),
    # path('edit/<int:id>', views.edit, name="edit"),
    path('edit/<int:id>', views.EditDataView.as_view(), name="edit"),
    # path('update/<int:id>', views.update, name="update"),
    path('update/<int:id>', views.EditDataView.as_view(), name="update"),

]
