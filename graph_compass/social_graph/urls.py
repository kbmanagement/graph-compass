from django.conf.urls import patterns, include, url

urlpatterns = patterns('social_graph.views',
    url(r'^$', 'home_view', name='home')

)
