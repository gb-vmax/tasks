FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/bin
RUN echo -e '#!/bin/sh\necho custom_echo' > /home/user/bin/echo
RUN chmod +x /home/user/bin/echo
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

