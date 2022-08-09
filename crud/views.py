from turtle import update
from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic

from .models import Diary


class AllView(generic.ListView):
    template_name = 'crud/all.html'
    model = Diary
    def get_queryset(self):
        return Diary.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    template_name = 'crud/detail.html'
    model = Diary

class AddView(generic.CreateView):
    template_name = 'crud/add.html'
    model = Diary
    fields = ['title','body']
    
class UpdateView(generic.UpdateView):
    template_name = 'crud/update.html'
    model = Diary
    fields = ['title','body']

class DeleteView(generic.DeleteView):
    template_name = 'crud/delete.html'
    model = Diary
    success_url = reverse_lazy('crud:all')


    



