FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/bin
RUN echo '#!/bin/bash
echo App' > /home/user/app.sh
RUN chmod 644 /home/user/app.sh
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

