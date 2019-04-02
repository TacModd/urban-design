from django.db import models

# View database in postgres
# $ sudo -u user psql (db)
# \l to view databases
# \c db if you didn't connect to db via command line
# \dt to view tables

# Create your models here.

# many to many label-image relationship needed
# but start with single gallery first

# gallery model
class Galleries(models.Model):
	title = models.CharField(max_length=50)
	gallery_desc = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.gallery_desc

# and an image model
class Images(models.Model):
	gallery = models.ForeignKey(Galleries, on_delete=models.CASCADE)
	image_text = models.CharField(max_length=200)
	add_date = models.DateTimeField('date added')
	votes = models.IntegerField(default = 0)
	def __str__(self):
		return self.image_text

