from django.views.generic.base import TemplateView
from projects.models import Project, ProjectCategory

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(home=1)
        return context

class ProjectsPageView(TemplateView):
    template_name = "projects.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectsPageView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['categories'] = ProjectCategory.objects.filter(projects__isnull=False)
        return context

class SingleProjectPageView(TemplateView):
    template_name = "single_project.html"
        