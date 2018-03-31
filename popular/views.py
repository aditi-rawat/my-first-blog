from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import population,customer,Hotel,National_Park,Lake,Temple
from .models import Hotel1_annualReport_2017,Hotel1_annualReport_2016,Hotel1_annualReport_2015,Hotel1_annualReport_2014,Hotel1_annualReport_2013,Hotel1_annualReport_2012,Hotel1_annualReport_2011
from .models import National_Park1_annualReport_2017,National_Park2_annualReport_2017,National_Park3_annualReport_2017,National_Park4_annualReport_2017,National_Park5_annualReport_2017
from .models import National_Park1_annualReport_2016,National_Park2_annualReport_2016,National_Park3_annualReport_2016,National_Park4_annualReport_2016,National_Park5_annualReport_2016
from .models import National_Park1_annualReport_2015,National_Park2_annualReport_2015,National_Park3_annualReport_2015,National_Park4_annualReport_2015,National_Park5_annualReport_2015
from .models import National_Park1_annualReport_2014,National_Park2_annualReport_2014,National_Park3_annualReport_2014,National_Park4_annualReport_2014,National_Park5_annualReport_2014
from .models import National_Park1_annualReport_2013,National_Park2_annualReport_2013,National_Park3_annualReport_2013,National_Park4_annualReport_2013,National_Park5_annualReport_2013
from .models import National_Park1_annualReport_2012,National_Park2_annualReport_2012,National_Park3_annualReport_2012,National_Park4_annualReport_2012,National_Park5_annualReport_2012
from .models import National_Park1_annualReport_2011,National_Park2_annualReport_2011,National_Park3_annualReport_2011,National_Park4_annualReport_2011,National_Park5_annualReport_2011
from .models import Lake1_annualReport_2017,Lake2_annualReport_2017,Lake3_annualReport_2017,Lake4_annualReport_2017,Lake5_annualReport_2017
from .models import Lake1_annualReport_2016,Lake2_annualReport_2016,Lake3_annualReport_2016,Lake4_annualReport_2016,Lake5_annualReport_2016
from .models import Lake1_annualReport_2015,Lake2_annualReport_2015,Lake3_annualReport_2015,Lake4_annualReport_2015,Lake5_annualReport_2015
from .models import Lake1_annualReport_2014,Lake2_annualReport_2014,Lake3_annualReport_2014,Lake4_annualReport_2014,Lake5_annualReport_2014
from .models import Lake1_annualReport_2013,Lake2_annualReport_2013,Lake3_annualReport_2013,Lake4_annualReport_2013,Lake5_annualReport_2013
from .models import Lake1_annualReport_2012,Lake2_annualReport_2012,Lake3_annualReport_2012,Lake4_annualReport_2012,Lake5_annualReport_2012
from .models import Lake1_annualReport_2011,Lake2_annualReport_2011,Lake3_annualReport_2011,Lake4_annualReport_2011,Lake5_annualReport_2011
from .models import Temple1_annualReport_2017,Temple2_annualReport_2017,Temple3_annualReport_2017,Temple4_annualReport_2017,Temple5_annualReport_2017
from .models import Temple1_annualReport_2016,Temple2_annualReport_2016,Temple3_annualReport_2016,Temple4_annualReport_2016,Temple5_annualReport_2016
from .models import Temple1_annualReport_2015,Temple2_annualReport_2015,Temple3_annualReport_2015,Temple4_annualReport_2015,Temple5_annualReport_2015
from .models import Temple1_annualReport_2014,Temple2_annualReport_2014,Temple3_annualReport_2014,Temple4_annualReport_2014,Temple5_annualReport_2014
from .models import Temple1_annualReport_2013,Temple2_annualReport_2013,Temple3_annualReport_2013,Temple4_annualReport_2013,Temple5_annualReport_2013
from .models import Temple1_annualReport_2012,Temple2_annualReport_2012,Temple3_annualReport_2012,Temple4_annualReport_2012,Temple5_annualReport_2012
from .models import Temple1_annualReport_2011,Temple2_annualReport_2011,Temple3_annualReport_2011,Temple4_annualReport_2011,Temple5_annualReport_2011




from .forms import customerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from .forms import OrderForm, ProductForm
#from django.contrib import messages
#from django.contrib.auth.decorators import login_required


def index(request):
    #orders = Order.objects.all()
    return render(request, 'index23.html')

def overall(request):
    return render(request, 'hotel-footfall.html')

def hotel_list(request):
    return render(request, 'hotel-list.html')

def permit_office(request):
    return render(request, 'permit_office.html')

def destination(request):
    return render(request, 'destination.html')

def np_list(request):
    return render(request, 'np-list.html')

def museums(request):
    return render(request, 'museum.html')

#def monestry(request):
    #return render(request, 'temples.html')


def govt(request):
    #orders = Order.objects.all()
    return render(request, 'ab1.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

@login_required()
def all_hotel_name(request):
    h=Hotel.objects.all()
    x=0
    return render(request,'all_hotel_name.html',{'h': h,'x': x})

@login_required()
def all_national_park_name(request):
    h=National_Park.objects.all()
    return render(request,'all_National_park.html',{'h': h})

@login_required()
def all_lake_name(request):
    h=Lake.objects.all()
    return render(request,'all_lake.html',{'h': h})

@login_required()
def all_temple_name(request):
    h=Temple.objects.all()
    return render(request,'all_temple.html',{'h': h})


def hotel_analysis(request):
    return render()




#  Hotel1 data
def hotel1_data(request):
    h=Hotel1_annualReport_2017.objects.all()
    h1=Hotel1_annualReport_2016.objects.all()
    h2=Hotel1_annualReport_2015.objects.all()
    h3=Hotel1_annualReport_2014.objects.all()
    h4=Hotel1_annualReport_2013.objects.all()
    h5=Hotel1_annualReport_2012.objects.all()
    h6=Hotel1_annualReport_2011.objects.all()
    return render(request,'hotel1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})


#Approve-Data
def approve_data_hotel1(request):
    r=Hotel.objects.get(hotel_name="Keepsa Residency")
    r.status="Approved"
    r.save()
    r=Hotel.objects.all()
    return render(request,'ab1.html')

#Hotel-2 Data
def hotel2_data(request):
    h=Hotel2_annualReport_2017.objects.all()
    h1=Hotel2_annualReport_2016.objects.all()
    h2=Hotel2_annualReport_2015.objects.all()
    h3=Hotel2_annualReport_2014.objects.all()
    h4=Hotel2_annualReport_2013.objects.all()
    h5=Hotel2_annualReport_2012.objects.all()
    h6=Hotel2_annualReport_2011.objects.all()
    return render(request,'hotel1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})


def approve_data_hotel2(request):
    r=Hotel.objects.get(hotel_name="White Conch Residency")
    r.status="Approved"
    r.save()
    r=Hotel.objects.all()
    return render(request,'ab1.html')

#Hotel-3 Data
def hotel3_data(request):
    h=Hotel3_annualReport_2017.objects.all()
    h1=Hotel3_annualReport_2016.objects.all()
    h2=Hotel3_annualReport_2015.objects.all()
    h3=Hotel3_annualReport_2014.objects.all()
    h4=Hotel3_annualReport_2013.objects.all()
    h5=Hotel3_annualReport_2012.objects.all()
    h6=Hotel3_annualReport_2011.objects.all()
    return render(request,'hotel1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})


def approve_data_hotel3(request):
    r=Hotel.objects.get(hotel_name="The Nettle & Fern Hotel")
    r.status="Approved"
    r.save()
    r=Hotel.objects.all()
    return render(request,'ab1.html')

#Hotel-4 Data
def hotel4_data(request):
    h=Hotel4_annualReport_2017.objects.all()
    h1=Hotel4_annualReport_2016.objects.all()
    h2=Hotel4_annualReport_2015.objects.all()
    h3=Hotel4_annualReport_2014.objects.all()
    h4=Hotel4_annualReport_2013.objects.all()
    h5=Hotel4_annualReport_2012.objects.all()
    h6=Hotel4_annualReport_2011.objects.all()
    return render(request,'hotel1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})


def approve_data_hotel4(request):
    r=Hotel.objects.get(hotel_name="Keepsa Residency")
    r.status="Approved"
    r.save()
    r=Hotel.objects.all()
    return render(request,'ab1.html')


#Hotel-5 Data
def hotel5_data(request):
    h=Hotel5_annualReport_2017.objects.all()
    h1=Hotel5_annualReport_2016.objects.all()
    h2=Hotel5_annualReport_2015.objects.all()
    h3=Hotel5_annualReport_2014.objects.all()
    h4=Hotel5_annualReport_2013.objects.all()
    h5=Hotel5_annualReport_2012.objects.all()
    h6=Hotel5_annualReport_2011.objects.all()
    return render(request,'hotel1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})


def approve_data_hotel5(request):
    r=Hotel.objects.get(hotel_name="Hotel Sikkim Delight")
    r.status="Approved"
    r.save()
    r=Hotel.objects.all()
    return render(request,'ab1.html')

#National_Park-1
def National_Park1_data(request):
    h=National_Park1_annualReport_2017.objects.all()
    h1=National_Park1_annualReport_2016.objects.all()
    h2=National_Park1_annualReport_2015.objects.all()
    h3=National_Park1_annualReport_2014.objects.all()
    h4=National_Park1_annualReport_2013.objects.all()
    h5=National_Park1_annualReport_2012.objects.all()
    h6=National_Park1_annualReport_2011.objects.all()
    return render(request,'National_Park1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_National_Park1(request):
    r=National_Park1.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')


#National_Park-2
def National_Park2_data(request):
    h=National_Park2_annualReport_2017.objects.all()
    h1=National_Park2_annualReport_2016.objects.all()
    h2=National_Park2_annualReport_2015.objects.all()
    h3=National_Park2_annualReport_2014.objects.all()
    h4=National_Park2_annualReport_2013.objects.all()
    h5=National_Park2_annualReport_2012.objects.all()
    h6=National_Park2_annualReport_2011.objects.all()
    return render(request,'National_Park1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_National_Park1(request):
    r=National_Park2.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')


#National_Park-3
def National_Park3_data(request):
    h=National_Park3_annualReport_2017.objects.all()
    h1=National_Park3_annualReport_2016.objects.all()
    h2=National_Park3_annualReport_2015.objects.all()
    h3=National_Park3_annualReport_2014.objects.all()
    h4=National_Park3_annualReport_2013.objects.all()
    h5=National_Park3_annualReport_2012.objects.all()
    h6=National_Park3_annualReport_2011.objects.all()
    return render(request,'National_Park1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_National_Park3(request):
    r=National_Park3.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')



#National_Park-4
def National_Park4_data(request):
    h=National_Park4_annualReport_2017.objects.all()
    h1=National_Park4_annualReport_2016.objects.all()
    h2=National_Park4_annualReport_2015.objects.all()
    h3=National_Park4_annualReport_2014.objects.all()
    h4=National_Park4_annualReport_2013.objects.all()
    h5=National_Park4_annualReport_2012.objects.all()
    h6=National_Park4_annualReport_2011.objects.all()
    return render(request,'National_Park1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_National_Park4(request):
    r=National_Park4.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')


#National_Park-5
def National_Park5_data(request):
    h=National_Park5_annualReport_2017.objects.all()
    h1=National_Park5_annualReport_2016.objects.all()
    h2=National_Park5_annualReport_2015.objects.all()
    h3=National_Park5_annualReport_2014.objects.all()
    h4=National_Park5_annualReport_2013.objects.all()
    h5=National_Park5_annualReport_2012.objects.all()
    h6=National_Park5_annualReport_2011.objects.all()
    return render(request,'National_Park1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_National_Park5(request):
    r=National_Park5.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')


#Lake-1
def Lake1_data(request):
    h=Lake1_annualReport_2017.objects.all()
    h1=Lake1_annualReport_2016.objects.all()
    h2=Lake1_annualReport_2015.objects.all()
    h3=Lake1_annualReport_2014.objects.all()
    h4=Lake1_annualReport_2013.objects.all()
    h5=Lake1_annualReport_2012.objects.all()
    h6=Lake1_annualReport_2011.objects.all()
    return render(request,'Lake1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Lake1(request):
    r=Lake1.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')

#Lake-2
def Lake2_data(request):
    h=Lake2_annualReport_2017.objects.all()
    h1=Lake2_annualReport_2016.objects.all()
    h2=Lake2_annualReport_2015.objects.all()
    h3=Lake2_annualReport_2014.objects.all()
    h4=Lake2_annualReport_2013.objects.all()
    h5=Lake2_annualReport_2012.objects.all()
    h6=Lake2_annualReport_2011.objects.all()
    return render(request,'Lake1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Lake1(request):
    r=Lake2.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')

def Lake3_data(request):
    h=Lake3_annualReport_2017.objects.all()
    h1=Lake3_annualReport_2016.objects.all()
    h2=Lake3_annualReport_2015.objects.all()
    h3=Lake3_annualReport_2014.objects.all()
    h4=Lake3_annualReport_2013.objects.all()
    h5=Lake3_annualReport_2012.objects.all()
    h6=Lake3_annualReport_2011.objects.all()
    return render(request,'Lake1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Lake1(request):
    r=Lake3.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')

def Lake1_data(request):
    h=Lake4_annualReport_2017.objects.all()
    h1=Lake4_annualReport_2016.objects.all()
    h2=Lake4_annualReport_2015.objects.all()
    h3=Lake4_annualReport_2014.objects.all()
    h4=Lake4_annualReport_2013.objects.all()
    h5=Lake4_annualReport_2012.objects.all()
    h6=Lake4_annualReport_2011.objects.all()
    return render(request,'Lake1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Lake1(request):
    r=Lake4.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')


def Lake5_data(request):
    h=Lake5_annualReport_2017.objects.all()
    h1=Lake5_annualReport_2016.objects.all()
    h2=Lake5_annualReport_2015.objects.all()
    h3=Lake5_annualReport_2014.objects.all()
    h4=Lake5_annualReport_2013.objects.all()
    h5=Lake5_annualReport_2012.objects.all()
    h6=Lake5_annualReport_2011.objects.all()
    return render(request,'Lake1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Lake1(request):
    r=Lake5.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')


#Temple-1
def Temple1_data(request):
    h=Temple1_annualReport_2017.objects.all()
    h1=Temple1_annualReport_2016.objects.all()
    h2=Temple1_annualReport_2015.objects.all()
    h3=Temple1_annualReport_2014.objects.all()
    h4=Temple1_annualReport_2013.objects.all()
    h5=Temple1_annualReport_2012.objects.all()
    h6=Temple1_annualReport_2011.objects.all()
    return render(request,'Temple1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Temple1(request):
    r=Temple1.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')

#Temple-2
def Temple2_data(request):
    h=Temple2_annualReport_2017.objects.all()
    h1=Temple2_annualReport_2016.objects.all()
    h2=Temple2_annualReport_2015.objects.all()
    h3=Temple2_annualReport_2014.objects.all()
    h4=Temple2_annualReport_2013.objects.all()
    h5=Temple2_annualReport_2012.objects.all()
    h6=Temple2_annualReport_2011.objects.all()
    return render(request,'Temple1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Temple1(request):
    r=Temple2.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')


#Temple-3
def Temple3_data(request):
    h=Temple3_annualReport_2017.objects.all()
    h1=Temple3_annualReport_2016.objects.all()
    h2=Temple3_annualReport_2015.objects.all()
    h3=Temple3_annualReport_2014.objects.all()
    h4=Temple3_annualReport_2013.objects.all()
    h5=Temple3_annualReport_2012.objects.all()
    h6=Temple3_annualReport_2011.objects.all()
    return render(request,'Temple1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Temple1(request):
    r=Temple2.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')


#Temple-2
def Temple2_data(request):
    h=Temple2_annualReport_2017.objects.all()
    h1=Temple2_annualReport_2016.objects.all()
    h2=Temple2_annualReport_2015.objects.all()
    h3=Temple2_annualReport_2014.objects.all()
    h4=Temple2_annualReport_2013.objects.all()
    h5=Temple2_annualReport_2012.objects.all()
    h6=Temple2_annualReport_2011.objects.all()
    return render(request,'Temple1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Temple1(request):
    r=Temple2.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')


#Temple-2
def Temple2_data(request):
    h=Temple2_annualReport_2017.objects.all()
    h1=Temple2_annualReport_2016.objects.all()
    h2=Temple2_annualReport_2015.objects.all()
    h3=Temple2_annualReport_2014.objects.all()
    h4=Temple2_annualReport_2013.objects.all()
    h5=Temple2_annualReport_2012.objects.all()
    h6=Temple2_annualReport_2011.objects.all()
    return render(request,'Temple1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Temple1(request):
    r=Temple2.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')


#Temple-3
def Temple2_data(request):
    h=Temple3_annualReport_2017.objects.all()
    h1=Temple3_annualReport_2016.objects.all()
    h2=Temple3_annualReport_2015.objects.all()
    h3=Temple3_annualReport_2014.objects.all()
    h4=Temple3_annualReport_2013.objects.all()
    h5=Temple3_annualReport_2012.objects.all()
    h6=Temple3_annualReport_2011.objects.all()
    return render(request,'Temple1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Temple1(request):
    r=Temple3.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')


#Temple-4
def Temple2_data(request):
    h=Temple4_annualReport_2017.objects.all()
    h1=Temple4_annualReport_2016.objects.all()
    h2=Temple4_annualReport_2015.objects.all()
    h3=Temple4_annualReport_2014.objects.all()
    h4=Temple4_annualReport_2013.objects.all()
    h5=Temple4_annualReport_2012.objects.all()
    h6=Temple4_annualReport_2011.objects.all()
    return render(request,'Temple1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Temple1(request):
    r=Temple4.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')


#Temple-5
def Temple5_data(request):
    h=Temple5_annualReport_2017.objects.all()
    h1=Temple5_annualReport_2016.objects.all()
    h2=Temple5_annualReport_2015.objects.all()
    h3=Temple5_annualReport_2014.objects.all()
    h4=Temple5_annualReport_2013.objects.all()
    h5=Temple5_annualReport_2012.objects.all()
    h6=Temple5_annualReport_2011.objects.all()
    return render(request,'Temple1_data.html',{'h':h,'h1':h1,'h2':h2,'h3':h3,'h4':h4,'h5':h5,'h6':h6})

def approve_data_Temple1(request):
    r=Temple5.objects.get(hotel_name="A-Star")
    r.status="Approved"
    return render(request,'ab1.html')





















# The `chart` function is defined to generate Column 2D chart from database.
def chart(request):
    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
    dataSource = {}
    dataSource['chart'] = { 
        "caption": "Monthly data for last year",
            "subCaption": "Buddha-Lake",
            "xAxisName": "Month",
            "yAxisName": "Population",
            "numberPrefix": "m",
            "theme": "zune"
        }

    # The data for the chart should be in an array where each element of the array is a JSON object
    # having the `label` and `value` as key value pair.

    dataSource['data'] = []
    # Iterate through the data in `Revenue` model and insert in to the `dataSource['data']` list.
    for key in population.objects.all():
      data = {}
      data['label'] = key.year
      data['value'] = key.population
      dataSource['data'].append(data)

    # Create an object for the Column 2D chart using the FusionCharts class constructor                      
    column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource)
    return render(request, 'index.html', {'output': column2D.render()}) 


#@login_required
def new_customer(request): 
    if request.POST:
        form = customerForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/new_customer ', messages.success(request, 'Customer is  successfully created.', 'alert-success'))
            else:
                return redirect('/new_customer ', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/new_customer ', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = customerForm(instance=customer)

        return render(request, 'new_customer.html', {'form':form})   


# Year-wise overall data
def hotel_analysis_2017(request):
    #return render(request,'analysis.html')
    #c=Hotel1_annualReport_2017.objects.get(pk=1,month='January')
    #if pk==1:
        #c=hotel_analysis_2017.objects.get()
        #c="1"
    return render(request,'analysis.html',{"c":1})

def hotel_analysis_2016(request):
    return render(request,'analysis.html',{"c":2})

def hotel_analysis_2015(request):
    return render(request,'analysis.html',{"c":3})

def hotel_analysis_2014(request):
    return render(request,'analysis.html',{"c":4})

def hotel_analysis_2013(request):
    return render(request,'analysis.html',{"c":5})

def hotel_analysis_2012(request):
    return render(request,'analysis.html',{"c":6})

def hotel_analysis_2011(request):
    return render(request,'analysis.html',{"c":7})

#monthly hotel
def hotel_analysis_jan(request):
    return render(request,'analysis.html',{"c":8})

def hotel_analysis_feb(request):
    return render(request,'analysis.html',{"c":9})

def hotel_analysis_mar(request):
    return render(request,'analysis.html',{"c":10})

def hotel_analysis_apr(request):
    return render(request,'analysis.html',{"c":11})

def hotel_analysis_may(request):
    return render(request,'analysis.html',{"c":12})

def hotel_analysis_jun(request):
    return render(request,'analysis.html',{"c":13})

def hotel_analysis_july(request):
    return render(request,'analysis.html',{"c":14})

def hotel_analysis_aug(request):
    return render(request,'analysis.html',{"c":15})

def hotel_analysis_sep(request):
    return render(request,'analysis.html',{"c":16})

def hotel_analysis_oct(request):
    return render(request,'analysis.html',{"c":17})

def hotel_analysis_nov(request):
    return render(request,'analysis.html',{"c":18})

def hotel_analysis_dec(request):
    return render(request,'analysis.html',{"c":19})




