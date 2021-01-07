from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, request
from .forms import ProductForms
from .models import Product
from django.contrib import messages
from django.views import View


# Create your views here.
# ID Pass Of Admin View: ID:anupkakri /password:12345678
# To insert data to the database
# def index(request):
#     if request.method == "POST":
#         form = ProductForms(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/django/create')
#     else:
#         form = ProductForms()
#         context = {'form': form}
#     return render(request, 'django/index.html', context)


class InsertView(View):
    def post(self, request):
        form = ProductForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/django/create')

    def get(self, request):
        form = ProductForms()
        context = {'form': form}
        return render(request, 'django/index.html', context)


# To fetch data from the database
# def view(request):
#     product = Product.objects.all()
#     return render(request, 'django/view.html', {'product': product})

class FetchDataView(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'django/view.html', {'product': product})


# To edit redirect edited page with previously inserted data
# def edit(request, id):
#     data = Product.objects.get(id=id)
#     return render(request, 'django/edit.html', {'data': data})


# To update Data To Database
# def update(request, id):
#     product = Product.objects.get(id=id)
#     form = ProductForms(request.POST, instance=product)
#     if form.is_valid():
#         form.save()
#         return redirect('/django/view')
#     else:
#         form = ProductForms()
#         context = {'form': form}
#     return render(request, 'django/index.html', context)

class EditDataView(View):
    def get(self ,request , id):
        data = Product.objects.get(id=id)
        return render(request, 'django/edit.html', {'data': data})

    def post(self,request, id):
        product = Product.objects.get(id=id)
        form = ProductForms(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/django/view')
        else:
            form = ProductForms()
            context = {'form': form}
        return render(request, 'django/index.html', context)


# To delete Data From DataBase
# def destroy(request, id):
#     d = Product.objects.get(id=id)
#     d.delete()
#     messages.success(request, "Data Has Been Deleted Successfully Done!")
#     return redirect('/django/view')

class DeleteDataView(View):
    def get(self, request ,id):
        d = Product.objects.get(id=id)
        d.delete()
        messages.success(request, "Data Has Been Deleted Successfully Done!")
        return redirect('/django/view')


