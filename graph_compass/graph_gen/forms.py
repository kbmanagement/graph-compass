from django import forms
from graph_gen.models import Graph, User

class GraphForm(forms.ModelForm):
    
    class Meta:
        model = Graph
        fields = ['name', 'size', 'graph_type']
