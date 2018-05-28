from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible  # only if you need to support Python 2
class Questions(models.Model):
	question = models.CharField( max_length = 200 )
	pub_date = models.DateTimeField('date published',blank=True,null=True)

	def __str__(self):
       	 	return self.question

    	def was_published_recently(self):
        	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible  # only if you need to support Python 2
class Choices(models.Model):
	question = models.ForeignKey( Questions, on_delete = models.CASCADE )
	choice = models.CharField(max_length = 200)
	votes = models.IntegerField( default = 0 )

	def __str__(self):
        	return self.choice


	# foregnkey tells django that each choiceis related to single question