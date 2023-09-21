import phonenumbers
from phonenumbers import timezone,geocoder,carrier
Key= '7086cfc96d5f4a7c8738fc28c71fff41'
number=input("Enter your number with +__:")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
yourlocation =geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)
print(yourlocation) 
 


##get service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)
query =str(yourlocation)
result= geocoder.geocode(query)
print(result)

