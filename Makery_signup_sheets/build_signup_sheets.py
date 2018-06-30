"""Front end to generate signup sheets from data"""
# -*- coding: latin-1 -*-

from gen_signup_sheet import SignupSheet

the_events = [
	{
	    "eventname": "Lego Robotics",
	    "date": "23/7/2018",
	    "dow": "Mon",
	    "starttime": "15:00",
	    "endtime": "17:00",
	    "cost": "8",
	    "plu": "",
	    "description": (
	        "Use our Lego EV3 Mindstorms robots to complete a selection of challenges."
	    ),
	    "agerange": "8-13",
	    "numslots": 4,
	},
	{
	    "eventname": "3D Design for 3D Printing",
	    "date": "24/7/2018",
	    "dow": "Tue",
	    "starttime": "11:00",
	    "endtime": "13:00",
	    "cost": "8",
	    "plu": "",
	    "description": (
	    	"Learn how to create a 3D object ready for printing on our 3D printer. "
	    	"(Printing is optional, £2 cost of print based on print duration and materials used. "
	    	"Printing price NOT included in session price."
	    ),
	    "agerange": "8-13",
	    "numslots" : 8,
	},
]

for event in the_events:
	sheet = SignupSheet()
	sheet.eventname = event["eventname"]
	sheet.eventname = event["date"]
	sheet.eventname = event["dow"]
	sheet.eventname = event["starttime"]
	sheet.eventname = event["endtime"]
	sheet.eventname = event["cost"]
	sheet.eventname = event["plu"]
	sheet.eventname = event["description"]
	sheet.eventname = event["agerange"]
	sheet.eventname = event["numslots"]
	sheet.generate_pdf()
