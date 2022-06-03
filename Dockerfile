FROM python:3.10.4-slim

RUN apt update && apt install -y --no-install-recommends \
    default-jre git make curl wget openssh-client

RUN useradd -ms /bin/bash python

RUN pip install pdm

USER python

WORKDIR /home/python/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV MY_PYTHON_PACKAGES=/home/python/app/__pypackages__/3.10
ENV PATH $PATH:${MY_PYTHON_PACKAGES}/bin

RUN echo 'eval "$(pdm --pep582)"' >> ~/.bashrc && \
    echo 'export TERM=xterm-256color'

CMD [ "tail", "-f", "/dev/null" ]
