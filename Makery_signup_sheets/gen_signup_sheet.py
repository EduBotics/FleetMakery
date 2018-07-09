""" Generate signup sheet """
# -*- coding: utf-8 -*-

from signupsheet import SignupSheet

if __name__ == '__main__':
    the_signupsheet = SignupSheet()

    the_signupsheet.generate_pdf()
