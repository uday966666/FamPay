FROM python:3.8-slim-buster

WORKDIR /app

COPY requirments.txt /app


RUN pip install -r requirments.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]