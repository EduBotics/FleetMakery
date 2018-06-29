FROM ubuntu

MAINTAINER Bruno Bronosky <richard@bronosky.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

RUN apt-get install -y texlive-latex-recommended
RUN apt-get install -y texlive-latex-extra

ADD latexcat /usr/local/bin/latexcat
RUN chmod a+x /usr/local/bin/latexcat

ENTRYPOINT ["/usr/local/bin/latexcat"]
