FROM python:3.8.0

MAINTAINER Romain Boureau <romain.boureau@reseau.eseo.fr>

COPY app /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "main.py" ]

