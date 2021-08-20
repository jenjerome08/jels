from django.db import models

class Respondent(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	email_address = models.CharField(max_length=200)
	street = models.CharField(max_length=200)
	barangay = models.CharField(max_length=200)
	gender = models.CharField(max_length=200)
	contact = models.IntegerField()
	city = models.CharField(max_length=200)
	zip_code = models.IntegerField()
	image = models.ImageField(default='default.png', blank=True)
	def __str__(self):
		return self.name

class Vaccine(models.Model):

	person = models.ForeignKey(Respondent, null=True, on_delete= models.SET_NULL)
	STATUS = (
			('Student', 'Student'),
			('Faculty', 'Faculty'),
			('Admin', 'Admin'),
			('Others', 'Others'),
			) 
	status = models.CharField(max_length=200, choices=STATUS)
	VACCINES = (
			('AstraZeneca', 'AstraZeneca'),
			('Pfizer', 'Pfizer'),
			('Moderna', 'Moderna'),
			('Sputnik V', 'Sputnik V'),
			('Covaxin', 'Covaxin'),
			('CoronaVac', 'CoronaVac'),
			('Johnson & Johnson', 'Johnson & Johnson'),
			) 
	vaccines = models.CharField(max_length=200, choices=VACCINES)
	CHOICE = (
			('One', 'One'),
			('Two', 'Two'),
			)
	how_many_times_have_you_been_injected_by_vaccine = models.CharField(max_length=200, choices=CHOICE)
	dose = models.CharField(max_length=20)
	where_did_you_get_the_vaccine = models.CharField(max_length=50)
	date_attended = models.DateTimeField()
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	comments = models.TextField(default="none", max_length=200,null=True, blank=True)
	def __str__(self):
		return self.vaccines


