FROM unix101-base:latest

USER root
RUN echo -e 'INFO Startup complete\nINFO User login\nERROR Disk full\nINFO Retry\nERROR Network down\nINFO Shutdown' > /home/user/logs.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

