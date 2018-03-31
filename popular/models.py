from django.db import models
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import RegexValidator



class population(models.Model):
    year = models.CharField(max_length=50)
    population = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % (self.Year, self.Month)


class customer(models.Model):
	name=models.CharField(max_length=50)
	contact=models.CharField(max_length=10)
	def __init__(self,name,contact,*args,**kwargs):
		return (self.name,self)

class customerForm(ModelForm):
    class Meta:
        model = customer
        fields = ['name', 'contact']
	



from django.db import models

#HOTELS

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    website = models.CharField(max_length=250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17, primary_key = True )
    emailId = models.EmailField(max_length=254, blank=True)
    status=  models.CharField(max_length=50, default='Not-Approved')


#2017

class Hotel1_annualReport_2017(models.Model):
    hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel2_annualReport_2017(models.Model):
    hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel3_annualReport_2017(models.Model):
    hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel4_annualReport_2017(models.Model):
    hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel5_annualReport_2017(models.Model):
    hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()


#2016

class Hotel1_annualReport_2016(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel2_annualReport_2016(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel3_annualReport_2016(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel4_annualReport_2016(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel5_annualReport_2016(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    
#2015

class Hotel1_annualReport_2015(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel2_annualReport_2015(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel3_annualReport_2015(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel4_annualReport_2015(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel5_annualReport_2015(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    

#2014

class Hotel1_annualReport_2014(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel2_annualReport_2014(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel3_annualReport_2014(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel4_annualReport_2014(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel5_annualReport_2014(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    

#2013

class Hotel1_annualReport_2013(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel2_annualReport_2013(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel3_annualReport_2013(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel4_annualReport_2013(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel5_annualReport_2013(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    

#2012

class Hotel1_annualReport_2012(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel2_annualReport_2012(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel3_annualReport_2012(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel4_annualReport_2012(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel5_annualReport_2012(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    
#2011

class Hotel1_annualReport_2011(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel2_annualReport_2011(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel3_annualReport_2011(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel4_annualReport_2011(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Hotel5_annualReport_2011(models.Model):
    Hotel_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()


# NATIONAL PARKS

class National_Park(models.Model):
    National_Park_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    website = models.CharField(max_length=250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17, primary_key = True )
    status=  models.CharField(max_length=50, default='Not-Approved')
    # national park k liye email Id relevant hai?
    #emailId = models.EmailField(max_length=254, blank=True ) 

#2017

class National_Park1_annualReport_2017(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park2_annualReport_2017(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park3_annualReport_2017(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park4_annualReport_2017(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park5_annualReport_2017(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

#2016

class National_Park1_annualReport_2016(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park2_annualReport_2016(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park3_annualReport_2016(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park4_annualReport_2016(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park5_annualReport_2016(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    
#2015

class National_Park1_annualReport_2015(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park2_annualReport_2015(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park3_annualReport_2015(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park4_annualReport_2015(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park5_annualReport_2015(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    

#2014

class National_Park1_annualReport_2014(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park2_annualReport_2014(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park3_annualReport_2014(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park4_annualReport_2014(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park5_annualReport_2014(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    

#2013

class National_Park1_annualReport_2013(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park2_annualReport_2013(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park3_annualReport_2013(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park4_annualReport_2013(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park5_annualReport_2013(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    

#2012

class National_Park1_annualReport_2012(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park2_annualReport_2012(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park3_annualReport_2012(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park4_annualReport_2012(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park5_annualReport_2012(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    
#2011

class National_Park1_annualReport_2011(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park2_annualReport_2011(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park3_annualReport_2011(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park4_annualReport_2011(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class National_Park5_annualReport_2011(models.Model):
    National_Park_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    
#LAKES

class Lake(models.Model):
    Lake_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    website = models.CharField(max_length=250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17, primary_key = True )
    status=  models.CharField(max_length=50, default='Not-Approved')
    #emailId = models.EmailField(max_length=254, **options)
     # lake k liye email Id website relevant hai?


#2017

class Lake1_annualReport_2017(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake2_annualReport_2017(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake3_annualReport_2017(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake4_annualReport_2017(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake5_annualReport_2017(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()


#2016

class Lake1_annualReport_2016(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake2_annualReport_2016(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake3_annualReport_2016(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake4_annualReport_2016(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake5_annualReport_2016(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    
#2015

class Lake1_annualReport_2015(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake2_annualReport_2015(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake3_annualReport_2015(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake4_annualReport_2015(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake5_annualReport_2015(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    

#2014

class Lake1_annualReport_2014(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake2_annualReport_2014(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake3_annualReport_2014(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake4_annualReport_2014(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake5_annualReport_2014(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    

#2013

class Lake1_annualReport_2013(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake2_annualReport_2013(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake3_annualReport_2013(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake4_annualReport_2013(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake5_annualReport_2013(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    

#2012

class Lake1_annualReport_2012(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake2_annualReport_2012(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake3_annualReport_2012(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake4_annualReport_2012(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake5_annualReport_2012(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    
#2011

class Lake1_annualReport_2011(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake2_annualReport_2011(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake3_annualReport_2011(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake4_annualReport_2011(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Lake5_annualReport_2011(models.Model):
    Lake_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

#TEMPLES

class Temple(models.Model):
    Temple_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    website = models.CharField(max_length=250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17, primary_key = True )
    status=  models.CharField(max_length=50, default='Not-Approved')
   # emailId = models.EmailField(max_length=254, **options)


#2017

class Temple1_annualReport_2017(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple2_annualReport_2017(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple3_annualReport_2017(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple4_annualReport_2017(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple5_annualReport_2017(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()


#2016

class Temple1_annualReport_2016(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple2_annualReport_2016(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple3_annualReport_2016(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple4_annualReport_2016(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple5_annualReport_2016(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    
#2015

class Temple1_annualReport_2015(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple2_annualReport_2015(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple3_annualReport_2015(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple4_annualReport_2015(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple5_annualReport_2015(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    

#2014

class Temple1_annualReport_2014(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple2_annualReport_2014(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple3_annualReport_2014(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple4_annualReport_2014(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple5_annualReport_2014(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    

#2013

class Temple1_annualReport_2013(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple2_annualReport_2013(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple3_annualReport_2013(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple4_annualReport_2013(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple5_annualReport_2013(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    

#2012

class Temple1_annualReport_2012(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple2_annualReport_2012(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple3_annualReport_2012(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple4_annualReport_2012(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple5_annualReport_2012(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()
    
#2011

class Temple1_annualReport_2011(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple2_annualReport_2011(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple3_annualReport_2011(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple4_annualReport_2011(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()

class Temple5_annualReport_2011(models.Model):
    Temple_name = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    total_count = models.BigIntegerField()


from django.db import models

#HOTELS
#annual
#2017

class new_popular_hotel1_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel2_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel3_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel4_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel5_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

#2016

class new_popular_hotel1_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel2_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel3_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel4_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel5_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()


#2015

class new_popular_hotel1_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel2_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel3_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel4_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel5_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

#2014

class new_popular_hotel1_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel2_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel3_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel4_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel5_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

#2013

class new_popular_hotel1_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel2_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel3_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel4_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel5_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

#2012

class new_popular_hotel1_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel2_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel3_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel4_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel5_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()


#2011

class new_popular_hotel1_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel2_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel3_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel4_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

class new_popular_hotel5_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()

#permit_officeS
#annual
#2017

class new_popular_permit_office_annualReport_2017(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()


#2016

class new_popular_permit_office_annualReport_2016(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()


#2015

class new_popular_permit_office_annualReport_2015(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()


#2014

class new_popular_permit_office_annualReport_2014(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()


#2013

class new_popular_permit_office_annualReport_2013(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()


#2012

class new_popular_permit_office_annualReport_2012(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()



#2011

class new_popular_permit_office_annualReport_2011(models.Model):
    i = models.CharField(max_length=200)
    month = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()


#HOTELS
#monthly
#2017

class new_popular_hotel1_january_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_hotel2_february_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_hotel3_march_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_hotel4_april_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)
    
class new_popular_hotel5_may_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_hotel6_june_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_hotel7_july_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_hotel8_august_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_hotel9_september_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_hotel10_october_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_hotel11_november_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_hotel12_december_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)


#permit_officeS
#monthly
#2017

class new_popular_permit_office_january_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_permit_office_february_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_permit_office_march_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_permit_office_april_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)
    

class new_popular_permit_office_may_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_permit_office_june_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_permit_office_july_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_permit_office_august_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_permit_office_september_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_permit_office_october_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_permit_office_november_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)

class new_popular_permit_office_december_2017(models.Model):
    user_id = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200)


#Overall table

class overall_sikkim_count(models.Model):
    i = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    #month = models.DateField()
    national_count = models.BigIntegerField()
    international_count = models.BigIntegerField()
    male_count = models.BigIntegerField()
    female_count = models.BigIntegerField()







    