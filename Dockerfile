FROM ubuntu:16.04


EXPOSE 5007:5007
CMD python microservice_Reg_Catalogo.py

ADD . /code
WORKDIR /code

RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y --no-install-recommends python-mysqldb
RUN pip install pymysql
RUN pip install mysqlclient
RUN pip install pika
RUN pip install Flask
