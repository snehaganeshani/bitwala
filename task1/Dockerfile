FROM ubuntu:18.04

LABEL maintainer "sneha@ganeshani"

# Copy python requirements file
COPY requirement.txt requirement.txt
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libssl-dev \    
    libpcre3 \
    libpcre3-dev \ 
    nginx \
    python3-setuptools \
    supervisor \
    uwsgi uwsgi-plugin-python3 

RUN  pip3 install -r requirement.txt

RUN useradd --no-create-home nginx

# Copy the Nginx global conf
COPY nginx.conf /etc/nginx/
# Copy the Flask Nginx site conf
COPY flask-site-nginx.conf /etc/nginx/conf.d/
# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY uwsgi.ini /etc/uwsgi/
# Custom Supervisord config
COPY supervisord.conf /etc/supervisord.conf
COPY nginx-selfsigned.crt /etc/ssl/certs/nginx-selfsigned.crt
COPY nginx-selfsigned.key /etc/ssl/private/nginx-selfsigned.key
COPY self-signed.conf /etc/nginx/snippets/self-signed.conf
COPY ssl-params.conf /etc/nginx/snippets/ssl-params.conf
COPY dhparam.pem /etc/nginx/dhparam.pem

EXPOSE 80
EXPOSE 443

COPY files/ /app/
WORKDIR /app


CMD ["/usr/bin/supervisord"]
 
