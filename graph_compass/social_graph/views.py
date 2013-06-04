from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import (
    render_to_response, redirect, get_object_or_404, RequestContext
)




@login_required
def home_view(request):
    return render_to_response('index.html', RequestContext(request, {}))
