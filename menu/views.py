from django.shortcuts import HttpResponse
from django.views.generic import View


class IndexView(View):
    def get(self, request):
        with open('menu/www/dist/index.html') as f:
            return HttpResponse(f.read())