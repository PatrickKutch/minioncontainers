# Use an official Python runtime as a parent image
FROM python:3.5-slim

# Board-Instrumentation-Framework has been cloned into this location
# before doing the build
WORKDIR /Board-Instrumentation-Framework/Minion
COPY /ContainerLauncher.py .
COPY /systeminfo.xml .

# Run my ContainerLauncher.py when the container launches
ENTRYPOINT  ["python", "ContainerLauncher.py"]
