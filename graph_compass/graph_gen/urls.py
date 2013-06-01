from django.conf.urls import patterns, include, url


urlpatterns = patterns('graph_gen.views',
    url(r'^$', 'graph_gen_home_view', name='graph_gen_home'),
    url(r'^store/', 'store_graph_view', name='store_graph'),
    url(r'^detail/(?P<graph_id>\d+)/', 'graph_detail_view', name='graph_detail'),
    url(r'^build/(?P<graph_id>\d+)/ajax/', 'ajax_build_graph_view'),
)
