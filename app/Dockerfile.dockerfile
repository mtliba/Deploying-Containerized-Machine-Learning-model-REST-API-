FROM python:3.6
# make directories suited to your application 
RUN mkdir -p /home/my_project/app

WORKDIR /home/my_project/app

# copy and install packages for flask
COPY requirements.txt /home/my_project/app
RUN pip install --no-cache-dir -r requirements.txt

# copy contents from your local to your docker container
COPY ./ /home/my_project/app