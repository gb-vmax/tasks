FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/subdir
RUN echo '#!/bin/bash
echo Hello' > /home/user/subdir/script.sh
RUN chmod 754 /home/user/subdir/script.sh
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

