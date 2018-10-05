# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Board-Instrumentation-Framework has been cloned into this location
# before doing the build

COPY /Board-Instrumentation-Framework Board-Instrumentation-Framework
WORKDIR /Board-Instrumentation-Framework/Oscar
# overwrite default config file
COPY /OscarConfig.xml /ContainerLauncher.py ./


ENTRYPOINT  ["python", "ContainerLauncher.py"]


