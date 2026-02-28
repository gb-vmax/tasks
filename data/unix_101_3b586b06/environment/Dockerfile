FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/logs
RUN echo -e 'INFO: server started\nWarning: Disk almost full\nerror: connection lost\nERROR: file not found\ninfo: user login\nError: timeout\nAll operations complete' > /home/user/logs/server.log
RUN rm -f /home/user/error_count.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

