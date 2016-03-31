#teste2
import urllib2
import json
import paho.mqtt.client as paho
import time
client = paho.Client()
client.connect("localhost", 1883, 60)
key = "049e10b5aaa2711f" 
f = urllib2.urlopen('http://api.wunderground.com/api/' +key +  '/geolookup/conditions/q/NY/Manhattan.json')
json_string = f.read()
parsed_json = json.loads(json_string)
#print parsed_json
location = parsed_json['location']['city']

temp_f_jason = parsed_json['current_observation']['temp_f']
relative_humidity_jason = parsed_json['current_observation']['relative_humidity']
wind_mph_jason = parsed_json['current_observation']['wind_mph']
precip_today_in_jason = parsed_json['current_observation']['precip_today_in']
time_stamp_jason = parsed_json['current_observation']['observation_epoch'] 

mylist0 = relative_humidity_jason.split("'")
mylist1 = mylist0[0].split("%")
relative_humidity = int(mylist1[0])

mylist2 = precip_today_in_jason.split("'")
precip_today_in = (mylist2[0])

mylist3 = time_stamp_jason.split("'")
time_stamp = int(mylist3[0])*1000

msg ='{\nmetric: "%s",\ndatapoints: [\n{\ntags: {"city":"Manhattan","state":"NY","latitude": "40.750.13351","longitude":"-73.99700928","neighborhood":"Chelsea","country":"US","elevation":"110","station_id":"KNYNEWYO395","rpi.datatype":"METRIC","sensor.unit":"F"},\nvalues: {"%s":"%s"}\n}]\n}' % ("Temperature",time_stamp,temp_f_jason)
print msg
client.publish("javier/board1",msg)
time.sleep(0.1)

msg ='{\nmetric: "%s",\ndatapoints: [\n{\ntags: {"city":"Manhattan","state":"NY","latitude": "40.750.13351","longitude":"-73.99700928","neighborhood":"Chelsea","country":"US","elevation":"110","station_id":"KNYNEWYO395","rpi.datatype":"METRIC","sensor.unit":"%s"},\nvalues: {"%s":"%s"}\n}]\n}' % ("relative_humidity","%",time_stamp,relative_humidity)
print msg
client.publish("javier/board1",msg)
time.sleep(0.1)

msg ='{\nmetric: "%s",\ndatapoints: [\n{\ntags: {"city":"Manhattan","state":"NY","latitude": "40.750.13351","longitude":"-73.99700928","neighborhood":"Chelsea","country":"US","elevation":"110","station_id":"KNYNEWYO395","rpi.datatype":"METRIC","sensor.unit":"mph"},\nvalues: {"%s":"%s"}\n}]\n}' % ("Wind",time_stamp,wind_mph_jason)
print msg
client.publish("javier/board1",msg)
time.sleep(0.1)

msg ='{\nmetric: "%s",\ndatapoints: [\n{\ntags: {"city":"Manhattan","state":"NY","latitude": "40.750.13351","longitude":"-73.99700928","neighborhood":"Chelsea","country":"US","elevation":"110","station_id":"KNYNEWYO395","rpi.datatype":"METRIC","sensor.unit":"in"},\nvalues: {"%s":"%s"}\n}]\n}' % ("Precipitation",time_stamp,precip_today_in)
print msg
client.publish("javier/board1",msg)

f.close()
