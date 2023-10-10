from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name="inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases_login'


class CategoriaNew(SuccessMessageMixin ,LoginRequiredMixin, generic.CreateView):
    model=Categoria
    template_name="inv/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    login_url="bases:login"
    success_message = "Categoria creada satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class CategoriaEdit(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    model=Categoria
    template_name="inv/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    login_url="bases:login"
    success_message="Categoria editada exitosamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    

class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model=Categoria
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:categoria_list")


class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name="inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = 'bases_login'


class SubCategoriaNew(SuccessMessageMixin,LoginRequiredMixin, generic.CreateView):
    model=SubCategoria
    template_name="inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    login_url="bases:login"
    success_message= "Subcategoria creada exitosamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    model=SubCategoria
    template_name="inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    login_url="bases:login"
    success_message="Subcategoria editada Correctamente!"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model=SubCategoria
    template_name='inv/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inv:subcategoria_list")


# Todo relacionado con marca

class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name="inv/marca_list.html"
    context_object_name = "obj"
    login_url = 'bases_login'


class MarcaNew(SuccessMessageMixin,LoginRequiredMixin, generic.CreateView):
    model=Marca
    template_name="inv/marca_form.html"
    context_object_name = "obj"
    form_class=MarcaForm
    success_url=reverse_lazy("inv:marca_list")
    login_url="bases:login"
    success_message="Marca agregada correctamente!"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MarcaEdit(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    model=Marca
    template_name="inv/categoria_form.html"
    context_object_name = "obj"
    form_class=MarcaForm
    success_url=reverse_lazy("inv:marca_list")
    login_url="bases:login"
    success_message="Marca editada correctamente!"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)



def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()

    contexto={}
    template_name="inv/catalogos_del.html"

    if not marca:
        return redirect("inv:marca_list")
    
    if request.method=='GET':
        contexto={'obj':marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        messages.error(request, "Marca Inactivada")
        return redirect("inv:marca_list")
    
    return render(request, template_name, contexto)

# -------------------------------------------------------------------------------------
# Todo relacionado con las unidades de medida


class UMView(LoginRequiredMixin, generic.ListView):
    model = UnidadMedida
    template_name="inv/um_list.html"
    context_object_name = "obj"
    login_url = 'bases_login'


class UMNew(SuccessMessageMixin,LoginRequiredMixin, generic.CreateView):
    model=UnidadMedida
    template_name="inv/um_form.html"
    context_object_name = "obj"
    form_class=UMForm
    success_url=reverse_lazy("inv:um_list")
    login_url="bases:login"
    success_message="Unidad de medida creada!"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)


class UMEdit(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    model=UnidadMedida
    template_name="inv/um_form.html"
    context_object_name = "obj"
    form_class=UMForm
    success_url=reverse_lazy("inv:um_list")
    login_url="bases:login"
    success_message="Unidad de medida editada!"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)



def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()

    contexto={}
    template_name="inv/catalogos_del.html"

    if not um:
        return redirect("inv:um_list")
    
    if request.method=='GET':
        contexto={'obj':um}

    if request.method == 'POST':
        um.estado = False
        um.save()
        return redirect("inv:um_list")
    
    return render(request, template_name, contexto)

# -------------------------------------------------------------------------------------
# Todo realcionado con productos


class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name="inv/producto_list.html"
    context_object_name = "obj"
    login_url = 'bases_login'


class ProductoNew(SuccessMessageMixin,LoginRequiredMixin, generic.CreateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name = "obj"
    form_class=ProductoForm
    success_url=reverse_lazy("inv:producto_list")
    login_url="bases:login"
    success_message="Producto Creado!"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProductoEdit(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name = "obj"
    form_class=ProductoForm
    success_url=reverse_lazy("inv:producto_list")
    login_url="bases:login"
    success_message="Producto editado!"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)



def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()

    contexto={}
    template_name="inv/catalogos_del.html"

    if not prod:
        return redirect("inv:producto_list")
    
    if request.method=='GET':
        contexto={'obj':prod}

    if request.method == 'POST':
        prod.estado = False
        prod.save()
        return redirect("inv:producto_list")
    
    return render(request, template_name, contexto)