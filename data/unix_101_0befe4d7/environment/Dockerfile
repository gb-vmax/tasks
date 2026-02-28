FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN printf "INFO Starting app\nERROR Failed to connect\nINFO Retrying\nERROR Timeout occurred\nINFO Stopped\n" > /home/user/logs/app.log
RUN gzip -c /home/user/logs/app.log > /home/user/logs/app.log.gz
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

