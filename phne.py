import phonenumbers
from phonenumbers import carrier,geocoder,timezone
import opencage
from opencage.geocoder import OpenCageGeocode
import geopy
from geopy import Nominatim
import folium

geolocator=Nominatim(user_agent="geoapiExcercises")
mobilenum=input("enter your mobile number ")
mobilenum=phonenumbers.parse("+91"+mobilenum)
print(timezone.time_zones_for_number(mobilenum))
print(carrier.name_for_number(mobilenum,"en"))
print("valid number",phonenumbers.is_valid_number(mobilenum))
print("checking possibility",phonenumbers.is_possible_number(mobilenum))
print(geocoder.description_for_number(mobilenum,"en"))
#print(phonenumbers.PhoneNumberDesc.PhoneMetadata())
key="b6488f47a4cc4366b34a80a7e2008df1"
location=geocoder.description_for_number(mobilenum,"en")
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
# lattitude=a['lat'][8:len(a['lat'])-4]
# longitude=a['lng'][8:len(a['lng'])-4]
lattitude=results[0]['geometry']['lat']
longitude=results[0]['geometry']['lng']
print(lattitude)
locate=geolocator.geocode(str(lattitude)+","+str(longitude))
print(locate)
mymap=folium.Map(location=[lattitude,longitude],zoom_start=9)
folium.Marker([lattitude,longitude],popup=location).add_to(mymap)
mymap.save("divya'slocation.html")


