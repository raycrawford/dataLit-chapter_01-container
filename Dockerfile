FROM ubuntu
RUN apt-get update && apt-get install language-pack-en -y && \
    locale-gen en_US && locale-gen en_US.UTF-8 && update-locale en_US.UTF-8 && \
    apt-get install python3 python3-pip -y
RUN pip3 install pandas && pip3 install tweepy && pip3 install vaderSentiment
