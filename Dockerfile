FROM python:3.9-alpine3.13
WORKDIR /PythonGuides

# Copy the current directory contents into the container at /app
COPY . /PythonGuides

RUN pip install -r /Requirements.txt
RUN pip install mysqlclient
RUN /usr/local/bin/pip install --upgrade pip
RUN python manage.py migrate
ENV INSTANCE_IP_OR_DOMAIN=default_value

EXPOSE 8001
CMD ["python","manage.py","runserver","0.0.0.0:8001"]