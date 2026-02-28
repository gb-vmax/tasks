FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN echo -e 'INFO Starting app\nERROR Failed to start\nINFO Retrying\nERROR Timeout' > /home/user/logs/app.log
RUN gzip -c /home/user/logs/app.log > /home/user/logs/app.log.gz
RUN rm /home/user/logs/app.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

