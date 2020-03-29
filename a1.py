"""
Name : Larika Sehgal
Section : B
Roll No. : 2018243
Group : 4
"""

# function to get weather response
# the value returned is the data from the website in string format 
def weather_response(location, API_key):
	# write your code
	import urllib.request
	json = str(urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?q=" + location + "&APPID=" + API_key).read())
	return(json)

# function to check for valid response
# this is used to know if the location entered is same as the place for which the weather is shown.
# e.g : for location = DelHI the name is delhi in the json string which clearly sre not equal. Hence the function returns the value true i.e an error exists.
def has_error(location,json):
	# write your code
	a = json.find('name')
	b = json.find(',',a,-1)
	c = json[a+7:b-1]
	if location != c:
		return(True)
	else:
		return(False)

 
# function to get attributes on nth day
# n = the number of days from current date
# t = time at which attributes are to be checked
def get_temperature (json, n = 0, t="18:00:00"):
	# write your code 
	import datetime
	d = datetime.date.today()
	ddelta = datetime.timedelta(days = n)
	e = str(d + ddelta)
	e = str(e)
	if len(t) == 4 :
		f = e + " 0" + t + ":00"	
	elif len(t) == 7 :
		f = e + " 0" + t		
	elif len(t) == 5 :
		f = e + " " +t + ":00"	
	elif len(t) == 8 :
		f = e + " " + t			#f is the date-time substring present in the JSON string				
	
	if json.find(f) == -1:
		return("not found")
	else:
		i = json.find(f)
		j = json.rfind('{"temp',0,int(i)+2)
		k = json.find(',',int(j)+2,-1)
		temperature = json[int(j)+8:int(k)]
		return(temperature)


# n = the number of days from current date
# t = time at which attributes are to be checked
def get_humidity(json, n=0, t="18:00:00"):
	# write your code 
	import datetime
	d = datetime.date.today()
	ddelta = datetime.timedelta(days = n)
	e = str(d + ddelta)
	e = str(e)
	if len(t) == 4 :
		f = e + " 0" + t + ":00"	
	elif len(t) == 7 :
		f = e + " 0" + t		
	elif len(t) == 5 :
		f = e + " " + t + ":00"	
	elif len(t) == 8 :
		f = e + " " + t
	
	if json.find(f) == -1:
		return("not found")
	else:
		i = json.find(f)
		j = json.rfind('humidity',0,int(i)+2)
		k = json.find(',',int(j)+2,-1)
		humidity = json[int(j)+10:int(k)]
		return(humidity)


# n = the number of days from current date
# t = time at which attributes are to be checked
def get_pressure(json, n=0, t="18:00:00"):
	# write your code 
	import datetime
	d = datetime.date.today()
	ddelta = datetime.timedelta(days = n)
	e = str(d + ddelta)
	e = str(e)
	if len(t) == 4 :
		f = e + " 0" + t + ":00"
	elif len(t) == 7 :
		f = e + " 0" + t	
	elif len(t) == 5 :
		f = e + " " +t + ":00"
	elif len(t) == 8 :
		f = e + " " +t
	
	if json.find(f) == -1:
		return("not found")
	else:
		i = json.find(f)
		j = json.rfind('pressure',0,int(i))
		k = json.find(',',int(j),-1)
		pressure = json[int(j)+10:int(k)]
		return(pressure)


# n = the number of days from current date
# t = time at which attributes are to be checked
def get_wind(json, n=0, t="18:00:00"):
	# write your code
	import datetime
	d = datetime.date.today()
	ddelta = datetime.timedelta(days = n)
	e = str(d + ddelta)
	e = str(e)
	if len(t) == 4 :
		f = e + " 0" + t + ":00"
	elif len(t) == 7 :
		f = e + " 0" + t	
	elif len(t) == 5 :
		f = e + " " +t + ":00"
	elif len(t) == 8 :
		f = e + " " +t
	
	if json.find(f) == -1:
		return("not found")
	else:
		i = json.find(f)
		j = json.rfind('speed',0,int(i)+2)
		k = json.find(',',int(j)+2,-1)
		wind = json[int(j)+7:int(k)]
		return(wind)


# n = the number of days from current date
# t = time at which attributes are to be checked
def get_sealevel(json, n=0, t="18:00:00"):
	# write your code
	import datetime
	
	d = datetime.date.today()
	ddelta = datetime.timedelta(days = n)
	e = str(d + ddelta)
	e = str(e)
	if len(t) == 4 :
		f = e + " 0" + t + ":00"
	elif len(t) == 7 :
		f = e + " 0" + t		
	elif len(t) == 5 :
		f = e + " " + t + ":00"
	elif len(t) == 8 :
		f = e + " " +t
	
	if json.find(f) == -1:
		return("not found")
	else:
		i = json.find(f)
		j = json.rfind('sea_level',0,int(i)+2)
		k = json.find(',',int(j)+2,-1)
		sea_level = json[int(j)+11:int(k)]
		return(sea_level)






