from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from web.models import Website
from django.apps import apps

class WebsiteList(ListView):
    paginate_by = 25
    model = Website

    def get_ordering(self):
        ordering = self.request.GET.get('o', '-date_added')
        return ordering

    def get_context_data(self):
        context = super().get_context_data()
        context['website_categories'] = apps.get_model('web.WebsiteCategory').objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = self.request.GET.get('filter')
        if filter:
            return queryset.filter(category__id=filter)
        else:
            return queryset


class WebsiteDetail(DetailView):
    model = Website
