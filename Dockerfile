FROM ubuntu
RUN apt-get update && apt-get install python3 python3-pip -y
RUN pip3 install pandas && pip3 install tweepy && pip3 install vaderSentiment
