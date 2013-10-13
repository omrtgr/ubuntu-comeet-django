from django.db import models
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename.replace(' ','.'))

# Create your models here.
class Rank(models.Model):
	title = models.CharField(max_length=20)
	desc = models.TextField()
	value = models.IntegerField(default=0)
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)
	val1 = models.TextField(default='Bare minumim')
	val2 = models.TextField(default='Minimal')
	val3 = models.TextField(default='Sufficient')
	val4 = models.TextField(default='Strong')
	val5 = models.TextField(default='Top 5%')


	def __unicode__(self):
		#returns the title when is being called
		return self.title







 
