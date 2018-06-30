# -*- coding: utf-8 -*-
"""Front end to generate signup sheets from data"""

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
            "Use our Lego EV3 Mindstorms robots to "
            "complete a selection of challenges."
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
            u"Learn how to create a 3D object ready for printing on our "
            u"3D printer. "
            u"(Printing is optional, £2 cost of print based on print "
            u"duration and materials used. "
            u"Printing price NOT included in session price."
        ),
        "agerange": "8-13",
        "numslots": 8,
    },
]

for event in the_events:
    sheet = SignupSheet()
    sheet.eventname = event["eventname"]
    sheet.date = event["date"]
    sheet.dow = event["dow"]
    sheet.starttime = event["starttime"]
    sheet.endtime = event["endtime"]
    sheet.cost = event["cost"]
    sheet.plu = event["plu"]
    sheet.description = event["description"]
    sheet.agerange = event["agerange"]
    sheet.numslots = event["numslots"]
    sheet.generate_pdf()
