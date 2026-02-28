FROM unix101-base:latest

USER root
RUN echo '#!/bin/bash' > /home/user/testsleep.sh
RUN echo 'sleep 120' >> /home/user/testsleep.sh
RUN chmod +x /home/user/testsleep.sh
RUN su user -c '/home/user/testsleep.sh &'
RUN sleep 1
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

