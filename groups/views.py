from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from groups.models import Student, Group
from groups.forms import CreateCourseForm, CreateStudentForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q, F
from django.views.generic import (
    TemplateView,
    ListView,
    FormView,
    CreateView,
    UpdateView,
)


@method_decorator(cache_page(60, key_prefix="base"),'get')
class IndexView(ListView):
    template_name = "base.html"
    model = Group
    paginate_by = 8

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        return queryset.select_related("mentor").prefetch_related("tags")


class GroupByCategory(ListView):

    template_name = "category.html"
    model = Group
    paginate_by = 5

    def get_queryset(self):
        return (
            Group.objects.filter(categories_id=self.kwargs["categories_id"])
            .select_related("mentor")
            .prefetch_related("tags")
        )


class SearchView(IndexView):
    def get_queryset(self):
        query = self.request.GET.get("search", None)
        if query:
            return self.model.objects.prefetch_related().filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return super(SearchView, self).get_queryset()


@method_decorator(cache_page(50, key_prefix="students"),'get')
class StudentList(ListView):
    template_name = "student_list.html"
    model = Student
    paginate_by = 10

    def get_queryset(self):
        queryset = super(StudentList, self).get_queryset()
        return queryset.select_related("group")


class CreateCourse(FormView):
    template_name = "create_course.html"
    form_class = CreateCourseForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        form.send_email()
        return super(CreateCourse, self).form_valid(form)


class CreateStudent(CreateView):
    template_name = "create_student.html"
    model = Student
    form_class = CreateStudentForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(CreateStudent, self).form_valid(form)


class EditCourse(UpdateView):
    template_name = "create_course.html"
    model = Group
    form_class = CreateCourseForm
    success_url = reverse_lazy("home")
    pk_url_kwarg = "group_id"


class EditUser(UpdateView):
    template_name = "create_student.html"
    model = Student
    form_class = CreateStudentForm
    success_url = reverse_lazy("students")
    pk_url_kwarg = "student_id"


@method_decorator(cache_page(1337, key_prefix="login"),'get')
class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        login(self.request, form.user)
        return super(LoginView, self).form_valid(form)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
