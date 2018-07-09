""" Makery Event class """
import copy
import datetime

DEBUG = False


class Event(object):
    def __init__(self, params=None, orig=None):
        if orig is not None:
            self.__dict__ = copy.deepcopy(orig.__dict__)
        else:
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
            if getattr(self, "_" + key, None) is not None:
                params[key] = getattr(self, "_" + key)
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
        self._dow = datetime.datetime.strptime(
            self.date,
            "%d/%m/%Y"
        ).strftime("%a")
        if DEBUG:
            print "Setting dow to {} from date {}".format(self.dow, self.date)

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

    @property
    def from_date(self):
        return self._from_date

    @from_date.setter
    def from_date(self, val):
        self._from_date = val

    @property
    def to_date(self):
        return self._to_date

    @to_date.setter
    def to_date(self, val):
        self._to_date = val

    def override(self, params):
        for key, val in params.iteritems():
            if DEBUG:
                print u"setting {} => {}".format(key, val)
            type(self).__dict__[key].fset(self, val)
