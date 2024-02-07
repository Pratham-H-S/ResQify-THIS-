FROM python:3.9-alpine3.13
COPY ./PythonGuides .
RUN pip install -r /Requirements.txt
RUN /usr/local/bin/pip install --upgrade pip
ENV INSTANCE_IP_OR_DOMAIN=100.27.26.210 
EXPOSE 8001
CMD ["python","manage.py","runserver","0.0.0.0:8001"]