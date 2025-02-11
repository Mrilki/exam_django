from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .forms import CourseForm
from .models import Course

class CourseEditMixin:
    model = Course
    template_name = 'course/course_create.html'

    def get_success_url(self):
        return reverse_lazy('course:index')


# Create your views here.
class IndexListView(ListView):
    model = Course
    template_name = 'course/course_list.html'
    context_object_name = 'course_list'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Course.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return Course.objects.all()

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/course_detail.html'
    context_object_name = 'course'


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course/course_create.html'

    def get_success_url(self):
        return reverse_lazy(
            'course:index',
        )
class CourseCreateView(CourseEditMixin, CreateView):
    form_class = CourseForm
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CourseUpdateView(CourseEditMixin, UpdateView):
    form_class = CourseForm
