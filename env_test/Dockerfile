# Use the official Ubuntu base image
FROM ubuntu:20.04

ENV USER developer
ENV APP_HOME /home/${USER}/tool
ENV EXECUTABLE env_test

# Set a password for the root user
RUN echo 'root:root' | chpasswd

# Create a new user
RUN useradd -m -s /bin/bash ${USER}

# Add your desired commands or configurations here
RUN apt-get -y update && \
    apt-get -y install build-essential && \
    apt install -y make && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory to the new user's home directory
WORKDIR ${APP_HOME}

COPY . ${APP_HOME}

# Change ownership of APP_HOME to the developer user
RUN chown -R ${USER}:${USER} ${APP_HOME}

# Use the new user for subsequent commands
USER ${USER}

# The ENTRYPOINT runs make and then provides a shell
ENTRYPOINT make && exec /bin/bash
