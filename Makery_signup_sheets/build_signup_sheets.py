# -*- coding: utf-8 -*-
"""Front end to generate signup sheets from data"""

from gen_signup_sheet import SignupSheet, Event

event_types = {
    "base": Event({"cost": 8})
}

event_types_overrides = {
    "saturday": [
        "base",
        {
            "dow": "Sat",
            "starttime": "12:00",
            "endtime": "14:00",
            "agerange": "8-13",
            "plu": "2x PLU8"
        }
    ],
    "afterschool": [
        "base",
        {
            "starttime": "15:45",
            "endtime": "17:45",
            "agerange": "8-13",
            "plu": "2x PLU8"
        }
    ],
    "adult": [
        "base",
        {
            "dow": "Tue",
            "starttime": "11:00",
            "endtime": "13:00",
            "agerange": "17+",
            "plu": ""
        }
    ],
    "summer_tuesday": [
        "base",
        {
            "starttime": "",
            "endtime": "",
            "agerange": "8-13",
            "plu": "PLU7",
        }
    ],
    "summer_weekday": [
        "base",
        {
            "starttime": "15:00",
            "endtime": "17:00",
            "agerange": "8-13",
            "plu": "PLU7",
        }
    ],
    "summer_weekend": [
        "saturday",
        {
            "plu": "PLU7",
        }
    ],
    "scratch": [
        "base",
        {
            "eventname": "Raspberry Pi Programming (Scratch)",
            "description": (
                "A chance to learn or improve your Scratch programming skills!"
            ),
            "numslots": 7,
        }
    ],
    "python": [
        "base",
        {
            "eventname": "Raspberry Pi Programming (Python)",
            "description": (
                "A chance to learn or improve your Python programming skills!"
            ),
            "numslots": 7,
        }
    ],
    "robotics": [
        "base",
        {
            "description": (
                "Use our Lego EV3 Mindstorms robots to "
                "complete a selection of challenges."
            ),
            "numslots": 4,
        }
    ],
    "3D Design": [
        "base",
        {
            "eventname": "3D Design for 3D Printing",
            "description": (
                "Learn how to create a 3D object ready for printing on our "
                "3D printer. "
                u"(Printing is optional, £2 cost of print based on print "
                "duration and materials used. "
                "Printing price NOT included in session price."
            ),
            "numslots": 5,
        }
    ]
}

retry = []
for name, override in event_types_overrides.iteritems():
    print "Overriding {} with {} -> {}\n".format(override[0], override[1], name)
    try:
        event_types[name] = Event(orig=event_types[override[0]], params=override[1])
    except KeyError:
        retry.append(name)

while len(retry):
    name = retry.pop(0)
    override = event_types_overrides[name]
    print "Overriding {} with {} -> {}\n".format(override[0], override[1], name)
    try:
        event_types[name] = Event(orig=event_types[override[0]], params=override[1])
    except AttributeError as err:
        print "\t{} : Error: {}\n".format(name, err)
        if len(retry) > 1:
            retry.append(name)

the_events = [
    {
        "name": "20180723_robotics_summer", 
        "bases": ["summer_weekday", "robotics"],
        "overrides": {
            "eventname": "Summer Session: Lego Robotics",
            "date": "23/7/2018",
            "dow": "Mon",
        }
    },
    {
        "name": "20180724_3ddesign", 
        "bases": ["summer_tuesday", "3D Design"],
        "overrides": {
            "eventname": "Summer Session: 3D Design for 3D Printing",
            "date": "24/7/2018",
            "dow": "Tue",
        }
    },
    {
        "name": "20180725_summer_scratch", 
        "bases": ["summer_weekday", "scratch"],
        "overrides": {
            "eventname": "Summer Session: Raspberry Pi Programming (Scratch)",
            "date": "25/7/2018",
            "dow": "Wed",
        }
    },
    {
        "name": "20180728_summer_python",
        "bases": ["summer_weekend", "python"],
        "overrides": {
            "eventname": "Summer Session: Raspberry Pi Programming (Python)",
            "date": "28/7/2018",
        }
    },

]


if __name__ == '__main__':
    for event in the_events:
        params = Event()
        for base in event["bases"]:
            params.override(params=event_types[base].params)
        params.override(params=event["overrides"])

        sheet = SignupSheet(params=params)
        print sheet.params.params
        sheet.generate_pdf()
