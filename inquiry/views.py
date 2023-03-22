from django.shortcuts import render
from django.views import View


class Inquiry(View):
    def get(self, request):
        return render(request, 'inquiry/inquiry.html')
