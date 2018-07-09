# -*- coding: utf-8 -*-
"""Front end to generate signup sheets from data"""

import sys
import json
import codecs
from gen_signup_sheet import SignupSheet
from event import Event

DEBUG = False


class EventTypes(object):

    event_types = {
        "base": Event({"cost": 8})
    }

    event_types_overrides = {
        "saturday": [
            ["base"],
            {
                "dow": "Sat",
                "starttime": "12:00",
                "endtime": "14:00",
                "agerange": "8-13",
                "plu": "2x PLU8"
            }
        ],
        "afterschool": [
            ["base"],
            {
                "starttime": "15:45",
                "endtime": "17:45",
                "agerange": "8-13",
                "plu": "2x PLU8"
            }
        ],
        "adult": [
            ["base"],
            {
                "dow": "Tue",
                "starttime": "11:00",
                "endtime": "13:00",
                "agerange": "17+",
                "plu": ""
            }
        ],
        "summer_holidays_2018": [
            ["base"],
            {
                "from_date": "23/7/2018",
                "to_date": "2/9/2018",
            }
        ],
        "summer_tuesday": [
            ["summer_holidays_2018"],
            {
                "starttime": "",
                "endtime": "",
                "agerange": "8-13",
                "plu": "PLU7",
            }
        ],
        "summer_weekday": [
            ["summer_holidays_2018"],
            {
                "starttime": "15:00",
                "endtime": "17:00",
                "agerange": "8-13",
                "plu": "PLU7",
            }
        ],
        "summer_weekend": [
            ["summer_holidays_2018", "saturday"],
            {
                "plu": "PLU7",
            }
        ],
        "scratch": [
            ["base"],
            {
                "eventname": "Raspberry Pi Programming (Scratch)",
                "description": (
                    "A chance to learn or improve your "
                    "Scratch programming skills!"
                ),
                "numslots": 7,
            }
        ],
        "python": [
            ["base"],
            {
                "eventname": "Raspberry Pi Programming (Python)",
                "description": (
                    "A chance to learn or improve your "
                    "Python programming skills!"
                ),
                "numslots": 7,
            }
        ],
        "robotics": [
            ["base"],
            {
                "description": (
                    "Use our Lego EV3 Mindstorms robots to "
                    "complete a selection of challenges."
                ),
                "numslots": 4,
            }
        ],
        "3D Design": [
            ["base"],
            {
                "eventname": "3D Design for 3D Printing",
                "description": (
                    "Learn how to create a 3D object ready for printing on "
                    "our 3D printer. "
                    u"(Printing is optional, £2 cost of print based on print "
                    "duration and materials used. "
                    "Printing price NOT included in session price."
                ),
                "numslots": 5,
            }
        ],
        "animation": [
            ["base"],
            {
                "eventname": "Stop Motion Animation",
                "description": (
                    "Work together to create a storyboard and make it "
                    "come to life creating a stop motion animation film."
                ),
                "numslots": 8,
            }
        ],
    }

    def fill_events(self):
        deps = {
            name: self.event_types_overrides[name][0]
            for name in self.event_types_overrides.keys()
        }
        depkeys = deps.keys()
        if DEBUG:
            print "depkeys: {}".format(depkeys)
        while len(depkeys):
            dep_name = depkeys.pop(0)
            item_dep = deps[dep_name]
            if DEBUG:
                print [(dep, dep in self.event_types) for dep in item_dep]
            if all([dep in self.event_types for dep in item_dep]):
                name = dep_name
                override = self.event_types_overrides[name]
                if DEBUG:
                    print "Overriding {} with {} -> {}\n".format(
                        override[0],
                        override[1],
                        name
                    )
                try:
                    self.event_types[name] = Event(
                        orig=self.event_types[override[0]],
                        params=override[1]
                    )
                except TypeError:
                    self.event_types[name] = Event()
                    for base in override[0]:
                        self.event_types[name].override(
                            params=self.event_types[base].params
                        )
                    self.event_types[name].override(override[1])
            else:
                depkeys.append(dep_name)


def generate_signup_sheets(the_events):
    the_event_types = EventTypes()
    the_event_types.fill_events()
    for event in the_events:
        params = Event()
        for base in event["bases"]:
            params.override(params=the_event_types.event_types[base].params)
        params.override(params=event["overrides"])

        sheet = SignupSheet(params=params)
        print sheet.params.params
        sheet.generate_pdf()


def gen_signup_sheets_from_json(json_file):
    with codecs.open(json_file, encoding='utf-8') as json_f:
        the_events = json.load(json_f)
    generate_signup_sheets(the_events)


if __name__ == '__main__':
    if len(sys.argv):
        gen_signup_sheets_from_json(sys.argv[1])
    else: 
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
                    "eventname": (
                        "Summer Session: Raspberry Pi Programming (Scratch)"
                    ),
                    "date": "25/7/2018",
                    "dow": "Wed",
                }
            },
            {
                "name": "20180728_summer_python",
                "bases": ["summer_weekend", "python"],
                "overrides": {
                    "eventname": (
                        "Summer Session: Raspberry Pi Programming (Python)"
                    ),
                    "date": "28/7/2018",
                }
            },

            {
                "name": "20180716",
                "bases": ["afterschool", "python"],
                "overrides": {
                    "date": "16/7/2018",
                }
            },
            {
                "name": "20180717",
                "bases": ["adult", "python"],
                "overrides": {
                    "date": "17/7/2018",
                }
            },
            {
                "name": "20180718",
                "bases": ["afterschool", "animation"],
                "overrides": {
                    "date": "18/7/2018",
                }
            },
            {
                "name": "20180719",
                "bases": ["afterschool", "scratch"],
                "overrides": {
                    "date": "19/7/2018",
                }
            },
        ]

        generate_signup_sheets(the_events)
