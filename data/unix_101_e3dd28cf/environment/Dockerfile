FROM unix101-base:latest

USER root
RUN printf 'Error: Disk full\nWarning: Low memory\nInfo: Backup completed\n' > /home/user/report.log
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

