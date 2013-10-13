from django import forms
from models import Rank

class RankForm(forms.ModelForm):
	class Meta:
		model=Rank
		fields = ('title', 'desc', 'val1', 'val2', 'val3', 'val4', 'val5', 'pub_date')
		
