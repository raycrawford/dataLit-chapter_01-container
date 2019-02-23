FROM ubuntu
RUN apt-get update && apt-get install language-pack-en -y && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
RUN apt-get install python3 python3-pip -y
RUN pip3 install pandas && pip3 install tweepy && pip3 install vaderSentiment

ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8
