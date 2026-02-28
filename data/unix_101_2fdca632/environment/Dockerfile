FROM unix101-base:latest

USER root
RUN echo -e 'Log entry 1\nLog entry 2\nLog entry 3' > /home/user/app.log
RUN gzip -c /home/user/app.log > /home/user/app.log.gz
RUN rm /home/user/app.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

