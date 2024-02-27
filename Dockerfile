FROM python:3.10

ENV CONTAINER_HOME=/var/www

ADD . $CONTAINER_HOME
WORKDIR $CONTAINER_HOME

RUN pwd 
# COPY requirements.txt /tmp/requirements.txt
# RUN python3 -m pip install --upgrade pip setuptools wheel                                                                                                                                                                                                
# RUN python3 -m pip install -r /tmp/requirements.txt  

RUN pip3 install -r $CONTAINER_HOME/requirements.txt

# RUN python3 $CONTAINER_HOME/src/tests/tests.py


# FROM python:3.9-slim

# WORKDIR /app
# RUN PWD 

# COPY . .

# RUN pip install -r requirements.txt