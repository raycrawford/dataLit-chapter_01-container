FROM ubuntu
RUN apt-get update && apt-get install language-pack-en -y && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
RUN apt-get install python3 python3-pip wget -y
RUN pip3 -U install pandas tweepy install vaderSentiment nltk
RUN python3 -m nltk.downloader all

ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8
