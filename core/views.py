from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Service, Project, TeamMember, BlogPost
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()[:6]
        context['projects'] = Project.objects.all()[:3]
        context['team_members'] = TeamMember.objects.all()[:4]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamMember.objects.all()
        return context

class ServicesView(ListView):
    model = Service
    template_name = 'core/services.html'
    context_object_name = 'services'

class ProjectsView(ListView):
    model = Project
    template_name = 'core/projects.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'core/project_detail.html'
    context_object_name = 'project'

class BlogListView(ListView):
    model = BlogPost
    template_name = 'core/blog.html'
    context_object_name = 'posts'
    paginate_by = 6

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'core/blog_detail.html'
    context_object_name = 'post'

class ContactView(TemplateView):
    template_name = 'core/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            messages.success(request, 'Your message has been sent successfully! We will contact you soon.')
            return render(request, self.template_name, {'form': ContactForm()})
        return render(request, self.template_name, {'form': form})