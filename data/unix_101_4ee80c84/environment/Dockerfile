FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/project/src
RUN mkdir -p /home/user/project/tmp
RUN echo 'main code' > /home/user/project/src/main.py
RUN echo 'config info' > /home/user/project/config.yaml
RUN echo 'temporary data' > /home/user/project/tmp/temp1.txt
RUN echo 'cache' > /home/user/project/tmp/cache.dat
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

