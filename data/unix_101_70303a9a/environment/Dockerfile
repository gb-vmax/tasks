FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN echo 'sleeping' > /home/user/logs/dummy.txt
RUN chown -R user:user /home/user
RUN su - user -c 'sleep 1000 > /dev/null 2>&1 &'
RUN sleep 1
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

