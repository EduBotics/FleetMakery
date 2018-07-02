# -*- coding: utf-8 -*-
"""Front end to generate signup sheets from data"""

from gen_signup_sheet import SignupSheet


class Event(object):
    def __init__(self, params=None):
        self._cost = 8
        self._eventname = None
        self._date = None
        self._dow = None
        self._starttime = None
        self._endtime = None
        self._cost = None
        self._plu = None
        self._description = None
        self._agerange = None
        self._numslots = None
        if params is not None:
            self.override(params)

    @property
    def params(self):
        params = {}
        for key in [
            "cost", "eventname", "date", "dow", "starttime", "endtime", "cost",
            "plu", "description", "agerange", "numslots"
        ]:
            params[key] = getattr(self, "_" + key, None)
        return params

    @property
    def eventname(self):
        return self._eventname

    @eventname.setter
    def eventname(self, value):
        self._eventname = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def dow(self):
        return self._dow

    @dow.setter
    def dow(self, value):
        self._dow = value

    @property
    def starttime(self):
        return self._starttime

    @starttime.setter
    def starttime(self, value):
        self._starttime = value

    @property
    def endtime(self):
        return self._endtime

    @endtime.setter
    def endtime(self, value):
        self._endtime = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def plu(self):
        return self._plu

    @plu.setter
    def plu(self, value):
        self._plu = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def agerange(self):
        return self._agerange

    @agerange.setter
    def agerange(self, value):
        self._agerange = value

    @property
    def numslots(self):
        return self._numslots

    @numslots.setter
    def numslots(self, value):
        self._numslots = value

    def override(self, params):
        for key in params:
            setattr(self, "_" + key, params[key])


event_types = {
    "base": Event({
        "cost": 8
    }),
}

event_types_overrides = {
    "saturday": [
        "base", {
            "starttime": "11:00",
            "endtime": "13:00",
            "agerange": "8-13",
            "plu": "2x PLU8"
        }
    ],
    "afterschool": [
        "base", {
            "starttime": "15:45",
            "endtime": "17:45",
            "agerange": "8-13",
            "plu": "2x PLU8"
        }
    ],
    "python": [
        "base",
        {
            "eventname": "Raspberry Pi Programming (Python)",
            "description": (
                "Use our Lego EV3 Mindstorms robots to "
                "complete a selection of challenges."
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
        "description": u''.join(
            "Learn how to create a 3D object ready for printing on our "
            "3D printer. "
            u"(Printing is optional, £2 cost of print based on print "
            "duration and materials used. "
            "Printing price NOT included in session price."
        ),
        "agerange": "8-13",
        "numslots": 8,
    },
]


if __name__ == '__main__':
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
