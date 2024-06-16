from urllib import request
from django.urls import reverse_lazy,  reverse
from pytils.translit import slugify
from catalog.models import Product, Category, Blog
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post_context_data(self, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name)
        print(phone)
        print(message)
        return render(request, "catalog/contacts.html")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        object.views_count += 1
        object.save(update_fields=['views_count'])
        return object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_active')
    success_url = reverse_lazy('catalog:blog')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'description', 'image', 'is_active')
    success_url = reverse_lazy('catalog:blog')

    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')


def toggle_activity(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.is_active:
        blog_item.is_active = False
    else:
        blog_item.is_active = True

    blog_item.save(update_fields=['is_active'])
    return redirect(reverse('catalog:blog'))
