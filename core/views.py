from django.views.generic import View
from django.shortcuts import render
from app.models import Familiar


class FamilyView(View):
    def get(self, request, *args,**kwargs):
        familiar= Familiar.objects.all()
        context = {
            'familiar':familiar
        }
        return render(request, 'index.html', context)