from django.shortcuts import render

from django.views import generic

from .models import Diary

class AllView(generic.ListView):
    template_name = 'crud/all.html'
    model = Diary
    def get_queryset(self):
        return Diary.objects.order_by('-pub_date')
