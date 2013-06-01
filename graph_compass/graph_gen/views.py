import json
import networkx as nx
from sonnet import build_vega_graph
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import (
    render_to_response, redirect, get_object_or_404, RequestContext
)

from forms import GraphForm
from models import User, Graph

@login_required
def graph_gen_home_view(request):
    user = request.user
    if user.is_authenticated():
        graphs = Graph.objects.filter(owner=user)
    else:
        graphs = None
    return render_to_response('graph_gen.html', RequestContext(request,{
        'graphs': graphs,
    }))
    
@login_required
def store_graph_view(request):
    graph_form = GraphForm()
    if request.POST:
        graph_form = GraphForm(request.POST)
        if graph_form.is_valid():
            graph = graph_form.save(commit=False)
            graph.owner = request.user
            graph.save()
            return redirect(graph_gen_home_view)
    return render_to_response('graph_store.html', RequestContext(request, {
        'graph_form': graph_form,
    }))

@login_required
def graph_detail_view(request, graph_id):
    graph = get_object_or_404(Graph, id=graph_id)
    return render_to_response('graph_detail.html', RequestContext(request, {
        'graph': graph,
    }))

@login_required
def ajax_build_graph_view(request, graph_id):
    graph = get_object_or_404(Graph, id=graph_id)
    size = graph.size
    graph_type = graph.graph_type
    if graph_type == 'random':
        G = nx.gnp_random_graph(size,0.1)
    else:
        G = nx.scale_free_graph(size)
    vega_graph = build_vega_graph(G)
    return HttpResponse(vega_graph, mimetype="text/javascript")


    
