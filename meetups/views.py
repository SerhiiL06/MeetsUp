from typing import Any
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic import View
from .models import Meetup, People
from .forms import PeopleForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render


class IndexView(ListView):
    model = Meetup
    template_name = "meetups/index.html"


class DetailMeetView(View):
    template_name = "meetups/meetup-details.html"
    model = Meetup

    def get(self, request, pk):
        context = {"object": Meetup.objects.get(pk=pk), "form": PeopleForm()}
        return render(request, "meetups/meetup-details.html", context)

    def post(self, request, pk):
        form = PeopleForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            new = People.objects.create(first_name=first_name, last_name=last_name)
            meet = Meetup.objects.get(pk=pk)
            new.meet.add(meet)
            return HttpResponseRedirect(reverse("meetups:success"))

        else:
            return HttpResponseRedirect(request.META["HTTP_REFERER"])


class SuccessView(TemplateView):
    template_name = "meetups/success.html"
