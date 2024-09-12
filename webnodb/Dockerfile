FROM python:3.8-alpine
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /server
ADD ./webnodb/flaskapp /server
RUN pip install flask
EXPOSE 5000/tcp
CMD ["flask", "run"]
