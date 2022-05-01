FROM python:3.8
WORKDIR StatisticsCRUDTest
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
