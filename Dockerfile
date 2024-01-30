FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT ["pytest"]

CMD ["--browser=firefox"]
