FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/archive
RUN printf "Backup started\nIncremental backup\nNo errors\n" > /home/user/archive/backup1.log
RUN printf "backup completed\nFull BACKUP\nNothing to do\n" > /home/user/archive/backup2.log
RUN gzip -c /home/user/archive/backup1.log > /home/user/archive/backup1.log.gz
RUN gzip -c /home/user/archive/backup2.log > /home/user/archive/backup2.log.gz
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

