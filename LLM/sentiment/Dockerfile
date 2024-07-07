# Use an official python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /sentiment

#Install system dependencies
RUN apt-get update && apt-get install -y \ 
    gcc \
    libhdf5-dev \
    pkg-config

# gcc -> A C compiler, required to build python packages
# libhdf5-dev -> HDF5 lib, development files
#pkg-config -> helps to configure and build applications

#Copy the requirements.txt file in the root
COPY requirements.txt .

#Install pip and upgrade it
RUN python -m ensurepip && pip install --upgrade pip

#Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

#Copy the current directory contents into the container at /app as well
COPY ./app ./app

#Make port 8000 available to the world outside this container
EXPOSE 8000

#Run main.py when the container launches, as it is contained under the app folder, we definer app.main
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]