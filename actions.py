from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionLIVERail(Action):
	def name(self):
		return 'action_liverail'
		
	def run(self, dispatcher, tracker, domain):
import requests , json 

# enter your api key here 
api_key = "Your_API_Key"

# base_url variable to store url 
base_url = "https://api.railwayapi.com/v2/live/train/"

# enter train_number here 
train_number = tracker.get_slot('train no')

# enter current date in dd-mm-yyyy format 
current_date = tracker.get_slot('date')

# complete_url variable to 
# store complete url address 
complete_url = base_url + train_number + "/date/" + current_date + "/apikey/" + api_key + "/"

# get method of requests module 
# return response object 
response_ob = requests.get(complete_url) 

# json method of response object convert 
# json format data into python format data 
result = response_ob.json() 

# Now result contains list of nested dictionaries 
# Check the value of "response_code" key is equal 
# to "200" or not if equal that means record is 
# found otherwise record is not found 
if result["response_code"] == 200 : 

	# train name is extracting from 
	# the result variable data	 
	train_name = result["train"]["name"] 

	# store the value or data of 
	# "route" key in variable y 
	y = result["route"] 

	# source station name is extracting 
	# from the y variable data 
	source_station = y[0]["station"]["name"] 

	# destination station name is 
	# extracting from the y varibale data 
	destination_station = y[len(y)-1]["station"]["name"] 
	
	# store the value of "position" 
	# key in variable position 
	position = result["position"] 

	

		response = """Train name {} going from {} towards {} is currently {}""".format(train_name, source_station, destination_station, position)
						
		dispatcher.utter_message(response)
		return [SlotSet('train no',train_no),('date',current_date)]

class ActionPnr(Action):
	def name(self):
		return 'action_pnr'
		
	def run(self, dispatcher, tracker, domain):
# Python program to find PNR 
# status using RAILWAY API 

# import required modules 
import requests, json 

# Enter API key here 
api_key = "Your_API_key"

# base_url variable to store url 
base_url = "https://api.railwayapi.com/v2/pnr-status/pnr/"

# Enter valid pnr_number 
pnr_number = tracker.get_slot('pnr')

# Stores complete url address 
complete_url = base_url + pnr_number + "/apikey/" + api_key + "/"

# get method of requests module 
# return response object 
response_ob = requests.get(complete_url) 

# json method of response object convert 
# json format data into python format data 
result = response_ob.json() 

# now result contains list 
# of nested dictionaries 
if result["response_code"] == 200: 

	# train name is extracting 
	# from the result variable data 
	train_name = result["train"]["name"] 

	# train number is extracting from 
	# the result variable data 
	train_number = result["train"]["number"] 

	# from station name is extracting 
	# from the result variable data 
	from_station = result["from_station"]["name"] 

	# to_station name is extracting from 
	# the result variable data 
	to_station = result["to_station"]["name"] 

	# boarding point station name is 
	# extracting from the result variable data 
	boarding_point = result["boarding_point"]["name"] 

	# reservation upto station name is 
	# extracting from the result variable data 
	reservation_upto = result["reservation_upto"]["name"] 

	# store the value or data of "pnr" 
	# key in pnr_num variable 
	pnr_num = result["pnr"] 

	# store the value or data of "doj" key 
	# in variable date_of_journey variable 
	date_of_journey = result["doj"] 

	# store the value or data of 
	# "total_passengers" key in variable 
	total_passengers = result["total_passengers"] 

	# store the value or data of "passengers" 
	# key in variable passengers_list 
	passengers_list = result["passengers"] 

	# store the value or data of 
	# "chart_prepared" key in variable 
	chart_prepared = result["chart_prepared"] 

	# print following values 
	print(" train name : " + str(train_name) 
		+ "\n train number : " + str(train_number) 
		+ "\n from station : " + str(from_station) 
		+ "\n to station : " + str(to_station) 
		+ "\n boarding point : " + str(boarding_point) 
		+ "\n reservation upto : " + str(reservation_upto) 
		+ "\n pnr number : " + str(pnr_num) 
		+ "\n date of journey : " + str(date_of_journey) 
		+ "\n total no. of passengers: " + str(total_passengers) 
		+ "\n chart prepared : " + str(chart_prepared)) 

	# looping through passenger list 
	for passenger in passengers_list: 
		
		# store the value or data 
		# of "no" key in variable 
		passenger_num = passenger["no"] 

		# store the value or data of 
		# "current_status" key in variable 
		current_status = passenger["current_status"] 

		# store the value or data of 
		# "booking_status" key in variable 
		booking_status = passenger["booking_status"] 

		# print following values 
		print(" passenger number : " + str(passenger_num) 
			+ "\n current status : " + str(current_status) 
			+ "\n booking_status : " + str(booking_status)) 

else: 
	print("record is not found for given request") 


	

		response = """Paseenger number {} current status {} Booking status {}""".format(passenger_num, current_status, booking_status)
						
		dispatcher.utter_message(response)
		return [SlotSet('pnr',pnr_number)]
