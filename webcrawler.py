import urllib.parse
import requests
import json

baseOne = "https://en.wikipedia.org/w/api.php?action=parse&format=json&prop=sections&"
baseTwo = "https://en.wikipedia.org/w/api.php?action=parse&format=json&prop=links&"
baseThree= "&"

firstPage = input('Nazwa pierwszej strony:')
alreadySeen = []

def seeAlso(link):
	url = baseOne + urllib.parse.urlencode({'page': link})
	jsonData = requests.get(url).json()
	if not jsonData:
		return
	outputData = jsonData['parse']['sections']
	if not outputData:
		return
	outputData = [x for x in outputData if x['anchor']=='See_also']
	if not outputData:
		return
	outputData = outputData[0]['index']
	
	url = baseTwo + urllib.parse.urlencode({'page': link}) + baseThree + urllib.parse.urlencode({'section': outputData})
	jsonData = requests.get(url).json()
	if not jsonData:
		return
	
	outputData = jsonData['parse']['links']
	if not outputData:
		return
	print()
	for link in outputData:
		if link['*'] not in alreadySeen:	
			
			print(link['*'])
			
	print()		
	for link in outputData:
		if link ['*'] not in alreadySeen:
			alreadySeen.append(link['*'])
			seeAlso(link['*'])
		
seeAlso(firstPage)
firstPage = input('Nazwa pierwszej strony:')