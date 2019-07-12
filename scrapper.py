import requests
from bs4 import BeautifulSoup
page=requests.get("https://karki23.github.io/Weather-Data/Albury.html")
content=page.content
soup=BeautifulSoup(content,"html.parser")
l=[]
all=soup.find("div",{"class":"locations-title weather-details-page-title"}).find("h1").text
 

table=soup.find_all("table",{"class":"twc-table"})
for items in table:
	for i in range(len(items.find_all("tr"))-1):
		d = {}
		try:
			d["date"]=items.find_all("span",{"class":"date-time"})[i].text
			d["location"]=items.find_all("span",{"class":"loc"})[i].text			
			d["Mintemp"]=items.find_all("td",{"class":"temp"})[i].text
			d["Maxtemp"]=items.find_all("td",{"class":"temp"})[i].text
			d["Rainfall"]=items.find_all("td",{"class":"rainfall"})[i].text
			d["Evaporation"]=items.find_all("td",{"class":"evap"})[i].text
			d["Sunshine"]=items.find_all("td",{"class":"sun"})[i].text
			d["WindGustDir"]=items.find_all("td",{"class":"wgd"})[i].text
			d["WindGustSpeed"]=items.find_all("td",{"class":"wgs"})[i].text
			d["WindDir9am"]=items.find_all("td",{"class":"wd9am"})[i].text
			d["WindDir3pm"]=items.find_all("td",{"class":"wd3pm"})[i].text
			d["WindSpeed9am"]=items.find_all("td",{"class":"ws9am"})[i].text
			d["WindSpeed3pm"]=items.find_all("td",{"class":"ws3pm"})[i].text
			d["Humidity9am"]=items.find_all("td",{"class":"h9am"})[i].text
			d["Humidity3pm"]=items.find_all("td",{"class":"h3pm"})[i].text
			d["Pressure9am"]=items.find_all("td",{"class":"p9am"})[i].text
			d["Pressure3pm"]=items.find_all("td",{"class":"p3pm"})[i].text
			d["Cloud9am"]=items.find_all("td",{"class":"c9am"})[i].text
			d["Cloud3pm"]=items.find_all("td",{"class":"c3pm"})[i].text
			d["Temp9am"]=items.find_all("td",{"class":"t9am"})[i].text
			d["Temp3pm"]=items.find_all("td",{"class":"t3pm"})[i].text
			d["RainToday"]=items.find_all("td",{"class":"raintoday"})[i].text
			d["RISK_MM"]=items.find_all("td",{"class":"risk"})[i].text
			d["RainTomorrow"]=items.find_all("td",{"class":"raintmrw"})[i].text
	



		except:
			d["date"]="None"
			d["location"]="None"		
			d["Mintemp"]="None"
			d["Maxtemp"]="None"
			d["Rainfall"]="None"
			d["Evaporation"]="None"
			d["Sunshine"]="None"
			d["WindGustDir"]="None"
			d["WindGustSpeed"]="None"
			d["WindDir9am"]="None"
			d["WindDir3pm"]="None"
			d["WindSpeed9am"]="None"
			d["WindSpeed3pm"]="None"
			d["Humidity9am"]="None"
			d["Humidity3pm"]="None"
			d["Pressure9am"]="None"
			d["Pressure3pm"]="None"
			d["Cloud9am"]="None"
			d["Cloud3pm"]="None"
			d["Temp9am"]="None"
			d["Temp3pm"]="None"
			d["RainToday"]="None"
			d["RISK_MM"]="None"
			d["RainTomorrow"]="None"
	
		#print("")
		l.append(d)

import pandas
df = pandas.DataFrame(l)
print(df)
df.to_csv("output.csv")	
