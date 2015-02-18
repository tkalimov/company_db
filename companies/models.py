from django.db import models

# Create your models here.
class Company(models.Model):
	domain = models.TextField()
	investors = models.TextField()
	last_funding_amount = models.BigIntegerField()
	cached_mobile_mattermark = models.IntegerField()
	employees_6_months_ago = models.IntegerField()
	keywords = models.TextField()
	uniques_wow = models.IntegerField() #May have a percentag ein the field that needs removing
	pre_money_valuation = models.IntegerField()
	last_funding_date = models.DateField(null=True)
	alert_hash = models.IntegerField()
	mobile_downloads_mom = models.IntegerField() # May have a percentage in the field that needs removing 
	continent = models.TextField()
	cached_uniques_month_ago = models.IntegerField()
	industries = models.TextField()
	city = models.TextField()
	employees_12_months_growth = models.IntegerField() # May have a percentage in the field that needs removing 	
	employees_mom = models.IntegerField() # May have a percentage in the field that needs removing 	
	employees_added_since_last_funding = models.IntegerField()	
	months_since_last_funding = models.IntegerField()
	cached_mobile_downloads = models.IntegerField()	
	state = models.TextField()
	interested = models.IntegerField()	
	company_name = models.TextField()
	is_raising = models.TextField()
	new_person_months_since_last_funding = models.IntegerField()	
	employees_month_ago = models.IntegerField()	
	est_founding_date = models.DateField(null=True)	
	employees_added_in_month = models.IntegerField()		
	mattermark_score = models.IntegerField()		
	cached_uniques = models.IntegerField()		
	cached_mobile_downloads_week_ago = models.IntegerField()
	employees_6_months_growth = models.IntegerField() # May have a percentage in the field that needs removing 		
	custom_score = models.IntegerField()	
	cached_mobile_downloads_month_ago = models.IntegerField()	
	total_funding = models.TextField()	
	employees_12_months_ago = models.IntegerField()	
	momentum_score = models.IntegerField()	
	region = models.TextField()
	new_funding_employee_growth = models.IntegerField() # May have a percentage in the field that needs removing	
	employees_added_in_6_months	= models.IntegerField()
	stage = models.TextField()
	business_models = models.TextField()
	user_tags = models.IntegerField()	
	has_mobile = models.TextField()
	mobile_downloads_wow = models.IntegerField() # May have a percentage in the field that needs removing 		
	country = models.TextField()
	raised_amount = models.IntegerField()
	cached_growth_score	= models.IntegerField()	
	location = models.TextField()
	cached_uniques_week_ago	= models.IntegerField()	
	raising_amount = models.IntegerField()	
	employees= models.IntegerField()
	uniques_mom = models.IntegerField() # May have a percentage in the field that needs removing 	

	def __unicode__(self):
		return str(self.company_name)
