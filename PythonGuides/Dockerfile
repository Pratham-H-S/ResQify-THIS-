

FROM python:3.10.12
WORKDIR /app
COPY Requirements.txt Requirements.txt
RUN pip3 install -r Requirements.txt
ENV INSTANCE_IP_OR_DOMAIN=13.201.50.103
COPY . .
# EXPOSE 8000
ENTRYPOINT [ "python", "manage.py","runserver","0.0.0.0:8001" ]
