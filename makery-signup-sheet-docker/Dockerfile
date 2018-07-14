FROM ubuntu

MAINTAINER Michael Noel Jones <mnjones@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

RUN apt-get install -y texlive-latex-recommended texlive-latex-extra python python-pip subversion && \
    pip install pylatexenc

ADD latexcat /usr/local/bin/latexcat
RUN chmod a+x /usr/local/bin/latexcat

RUN svn export https://github.com/EduBotics/FleetMakery/trunk/Makery_signup_sheets
RUN cd Makery_signup_sheets

ENTRYPOINT ["python", "/Makery_signup_sheets/build_signup_sheets.py"]
