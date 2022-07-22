# Remember when making images you start from NOTHING, which means you need to install an OS, languages and anything else you need to run your image

# Download a python 3 image and setup using it
FROM python:3-alpine

# Setup a folder called /app on the container where all the files will be stored and everything will run from
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Run `pip install -r requirements.txt`
RUN pip install -r requirements.txt 

# Copy all the files from the current directory on the host machine into the cwd of the container
COPY . ./

# Allow for port 8080 of the container to be accessible to the host machine
EXPOSE 8080

# Start using `python3 routes.py`
ENTRYPOINT ["python3", "routes.py"]
