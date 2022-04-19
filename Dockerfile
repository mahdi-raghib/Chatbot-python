FROM python:3.7
RUN mkdir /app
COPY requirements.txt requirements.txt
WORKDIR /app/
ADD . /app/
RUN pip3 install -r requirements.txt
CMD ["python", "/app/app.py"]