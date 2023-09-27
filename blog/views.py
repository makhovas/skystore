from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 100:
            send_mail(subject="Отправка письма",
                      message=f'Поздравляю! У Вас 100 просмотров по записи "{self.object.name}" в блоге!',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=['makhova-s94@mail.ru'],
                      fail_silently=False
                      )
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'description', 'image')
    success_url = reverse_lazy('blog:list')

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_blog = form.save()
    #         new_blog.slug = slugify(new_blog.name)
    #         new_blog.save()
    #
    #     return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'description', 'image')
    success_url = reverse_lazy('blog:list')

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_blog = form.save()
    #         new_blog.slug = slugify(new_blog.name)
    #         new_blog.save()
    #
    #     return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
