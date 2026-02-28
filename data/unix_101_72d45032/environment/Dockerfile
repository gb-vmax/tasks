FROM unix101-base:latest

USER root
RUN echo 'critical log entry' > /home/user/important.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

