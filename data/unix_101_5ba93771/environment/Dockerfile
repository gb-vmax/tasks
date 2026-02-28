FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN echo -e 'INFO Start application\nERROR Failed to connect\nINFO Retrying\nERROR Out of memory\nINFO Shutdown' > /home/user/logs/app.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

