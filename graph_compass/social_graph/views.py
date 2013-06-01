from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import (
    render_to_response, redirect, get_object_or_404, RequestContext
)



def home_view(request):
    return HttpResponse('hello')
