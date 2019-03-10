0# Name:Tanya Sanjay Kumar, Rollno.:2018109 , Section:A , Group:5
import urllib.request
import datetime

# function to get weather response
def weather_response(location, API_key):
    # write your code
    url=urllib.request.urlopen(str("http://api.openweathermap.org/data/2.5/forecast?q="+location+"&APPID="+API_key))
    json=url.read().decode('UTF8')
    return json
	 

# function to check for valid response 
def has_error(location,json):
	# write your code
    a=json.find(location)
    if a==-1:
        return True
    else:
        return False
    
	 

# function to get attributes on nth day1
def get_temperature (json, n, t):
	# write your code
    if n>=0 and n<=4:
        t=str(t)
        if t in ["00:00:00","03:00:00","06:00:00","09:00:00","12:00:00","15:00:00","18:00:00","21:00:00"]:
            n1=datetime.date.today().day+n
            if len(str(n1))==1:
                n1="0"+str(n1)
            n2=datetime.date.today().strftime('%Y-%m-' + str(n1))
            a=int(json.find(n2+" "+t))
            part=json[a-355:a+21]
            temp1=part.find("temp")
            temp2=part.find("temp_min")
            temp=part[temp1+6:temp2-2]
            return temp
        else:
            print("Incorrect time format. Pls enter correctly . Ex:03:00:00,06:00:00")
            
    else:
        print("Enter a number between 0 to 4 only")
     
    
def get_humidity(json, n, t):
	# write your code
    if n>=0 and n<=4:
        t=str(t)
        if t in ["00:00:00","03:00:00","06:00:00","09:00:00","12:00:00","15:00:00","18:00:00","21:00:00"]:
            n1=datetime.date.today().day+n
            if len(str(n1))==1:
                n1="0"+str(n1)
            n2=datetime.date.today().strftime('%Y-%m-' + str(n1))
            a=int(json.find(n2+" "+t))
            part=json[a-355:a+21]
            hum1=part.find("humidity")
            hum2=part.find("temp_kf")
            hum=part[hum1+10:hum2-2]
            return hum  
        else:
            print("Incorrect time format. Pls enter correctly . Ex:03:00:00,06:00:00")
            
    else:
        print("Enter a number between 0 to 4 only")


def get_pressure(json, n, t):
	# write your code
    if n>=0 and n<=4:
        t=str(t)
        if t in ["00:00:00","03:00:00","06:00:00","09:00:00","12:00:00","15:00:00","18:00:00","21:00:00"]:
            n1=datetime.date.today().day+n
            if len(str(n1))==1:
                n1="0"+str(n1)
            n2=datetime.date.today().strftime('%Y-%m-' + str(n1))
            a=int(json.find(n2+" "+t))
            part=json[a-355:a+21]
            pres1=part.find("pressure")
            pres2=part.find("sea_level")
            pres=part[pres1+10:pres2-2]
            return pres
        else:
            print("Incorrect time format. Pls enter correctly . Ex:03:00:00,06:00:00")
            
    else:
        print("Enter a number between 0 to 4 only")


def get_wind(json, n, t):
	# write your code
    if n>=0 and n<=4:
        t=str(t)
        if t in ["00:00:00","03:00:00","06:00:00","09:00:00","12:00:00","15:00:00","18:00:00","21:00:00"]:
            n1=datetime.date.today().day+n
            if len(str(n1))==1:
                n1="0"+str(n1)
            n2=datetime.date.today().strftime('%Y-%m-' + str(n1))
            a=int(json.find(n2+" "+t))
            part=json[a-355:a+21]
            wind1=part.find("speed")
            wind2=part.find("deg")
            wind=part[wind1+7:wind2-2]
            return wind
        else:
            print("Incorrect time format. Pls enter correctly . Ex:03:00:00,06:00:00")
            
    else:
        print("Enter a number between 0 to 4 only")

def get_sealevel(json, n, t):
	# write your code
    if n>=0 and n<=4:
        t=str(t)
        if t in ["00:00:00","03:00:00","06:00:00","09:00:00","12:00:00","15:00:00","18:00:00","21:00:00"]:
            n1=datetime.date.today().day+n
            if len(str(n1))==1:
                n1="0"+str(n1)
            n2=datetime.date.today().strftime('%Y-%m-' + str(n1))
            a=int(json.find(n2+" "+t))
            part=json[a-355:a+21]
            sea1=part.find("sea_level")
            sea2=part.find("grnd_level")
            sea=part[sea1+11:sea2-2]
            return sea
        else:
            print("Incorrect time format. Pls enter correctly . Ex:03:00:00,06:00:00")
            
    else:
        print("Enter a number between 0 to 4 only")



