FROM python:3.8-alpine
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /server
ADD ./flaskapp /server
RUN pip install flask
RUN  pip install Flask-PyMongo
EXPOSE 5000/tcp
CMD ["flask", "run"]
