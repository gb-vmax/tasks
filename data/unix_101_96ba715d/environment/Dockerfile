FROM unix101-base:latest

USER root
RUN useradd -m testuser
RUN groupadd projectgrp
RUN usermod -aG projectgrp testuser
RUN mkdir -p /home/user
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

