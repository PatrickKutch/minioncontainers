# Use an official Python runtime as a parent image
FROM python:3.5

# Change for your own proxy
ENV http_proxy proxy.jf.intel.com:911
ENV https_proxy proxy.jf.intel.com:911

RUN git clone https://github.com/intel/Board-Instrumentation-Framework.git
WORKDIR /Board-Instrumentation-Framework
# don't need Marvin or Oscar
RUN ["rm", "-r", "-f", "Oscar"]
RUN rm -r -f Marvin

WORKDIR /Board-Instrumentation-Framework/Minion
COPY /ContainerLauncher.py .
COPY /RandomValuesConfig.xml .


# Run app.py when the container launches
#CMD ["bash"]
ENTRYPOINT  ["python", "ContainerLauncher.py"]
