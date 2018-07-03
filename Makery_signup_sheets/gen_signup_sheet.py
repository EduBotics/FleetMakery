""" Generate signup sheet """
# -*- coding: utf-8 -*-

import subprocess
import datetime
import codecs
import copy

from pylatexenc.latexencode import utf8tolatex


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
        for key, val in params.iteritems():
            setattr(self, "_" + key, val)


class SignupSheet(object):
    def __init__(self, params=None):
        self._params = None
        self._template = None
        self._signup_sheet = None
        self._tex_filename = None
        if params is not None:
            self._params = params

    @property
    def eventname(self):
        return self.params.eventname

    @eventname.setter
    def eventname(self, value):
        self.params.eventname = value

    @property
    def date(self):
        return self.params.date

    @date.setter
    def date(self, value):
        self.params.date = value

    @property
    def dow(self):
        return self.params.dow

    @dow.setter
    def dow(self, value):
        self.params.dow = value

    @property
    def starttime(self):
        return self.params.starttime

    @starttime.setter
    def starttime(self, value):
        self.params.starttime = value

    @property
    def endtime(self):
        return self.params.endtime

    @endtime.setter
    def endtime(self, value):
        self.params.endtime = value

    @property
    def cost(self):
        return self.params.cost

    @cost.setter
    def cost(self, value):
        self.params.cost = value

    @property
    def plu(self):
        return self.params.plu

    @plu.setter
    def plu(self, value):
        self.params.plu = value

    @property
    def description(self):
        return self.params.description

    @description.setter
    def description(self, value):
        self.params.description = value

    @property
    def agerange(self):
        return self.params.agerange

    @agerange.setter
    def agerange(self, value):
        self.params.agerange = value

    @property
    def numslots(self):
        return self.params.numslots

    @numslots.setter
    def numslots(self, value):
        self.params.numslots = value

    @property
    def template(self):
        if (self._template is None):
            self.read_template()
        return self._template

    @property
    def params(self):
        if self._params is None:
            self.set_test_params()
        return self._params

    @params.setter
    def params(self, new_params):
        self._params = new_params

    @property
    def signup_sheet(self):
        if self._signup_sheet is None:
            self.generate_signupsheet()
        return self._signup_sheet

    @signup_sheet.setter
    def signup_sheet(self, value):
        self._signup_sheet = value

    @property
    def tex_filename(self):
        if self._tex_filename is None:
            self._tex_filename = "{}_signup_sheet.tex".format(
                datetime.datetime.strptime(
                    self.date,
                    "%d/%m/%Y"
                ).strftime("%Y%m%d")
            )
        return self._tex_filename

    def read_template(self):
        # read in signup_sheet.tex.tmpl
        filename = "signup_sheet.tex.tmpl"
        with codecs.open(filename, encoding='utf-8') as template_file:
            self._template = template_file.read()

    def set_test_params(self):
        self._params = Event(params={
            "eventname": "Raspberry Pi (Python)",
            "date": "2/7/2018",
            "dow": "Mon",
            "starttime": "15:45",
            "endtime": "17:45",
            "cost": "8",
            "plu": "",
            "description": (
                "A chance to learn or improve your "
                "Python programming!"
            ),
            "agerange": "8-13",
            "numslots": 8,
        })

    def generate_signupsheet(self):
        latex_params = {}
        for name, param in self.params.params.iteritems():
            latex_params[name] = utf8tolatex(param)

        self.signup_sheet = self.template.format(**latex_params)

    def generate_tex(self):
        with codecs.open(
            self.tex_filename,
            encoding='utf-8',
            mode="w"
        ) as tex_f:
            tex_f.write(self.signup_sheet)

    def generate_pdf(self):
        # call pdflatex to convert it to pdf
        self.generate_tex()
        cmd = ["pdflatex", self.tex_filename]
        subprocess.call(cmd)


if __name__ == '__main__':
    the_signupsheet = SignupSheet()

    the_signupsheet.generate_pdf()
