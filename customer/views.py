from django.shortcuts import render
from random import randint

# Create your views here.
import json
from faker import Faker
fake=Faker()
def customer(request):
    customer_data ={}
    activity_periods={}
    for i in range(1,8):
     customer_data[i]={}
     customer_data[i]['id']=randint(1,2000)
     customer_data[i]['real_name']= fake.name()
     customer_data[i]['tz']= fake.address()
     customer_data[i]['activity_periods'] = list([activity_periods])
    for j in range(1,3):
         activity_periods[j]={}
         activity_periods[j]['start_time']=fake.date()+' '+fake.time()
         activity_periods[j]['end_time']= fake.date()+' '+fake.time()


#dictionary dumped as json in a json file
    with open('Test.json','w') as fp:
     json.dump(customer_data,fp)

    with open('Test.json','r') as fp:
     context2=json.load(fp)
     return render(request,'base.html',{'context':context2})
