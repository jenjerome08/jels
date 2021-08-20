import django_filters
from django_filters import CharFilter

from .models import *

class VaccineFilter(django_filters.FilterSet):

	vaccines = CharFilter(field_name='vaccines', lookup_expr='icontains')
	
	class Meta:
		model = Vaccine
		fields = ['vaccines']		
