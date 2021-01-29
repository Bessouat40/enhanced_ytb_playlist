FROM python:3.7

RUN mkdir /home/dev/ && mkdir /home/dev/code/

WORKDIR /home/dev/code/


RUN pip install --upgrade pip 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python","./app/main.py"]