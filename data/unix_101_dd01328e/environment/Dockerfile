FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo -e 'Success! Backup completed.\nFailure: Disk full.' > /home/user/data/backup1
RUN echo -e 'Partial success on backup.\nNo errors found.' > /home/user/data/backup2
RUN gzip -c /home/user/data/backup1 > /home/user/data/backup1.gz
RUN gzip -c /home/user/data/backup2 > /home/user/data/backup2.gz
RUN rm /home/user/data/backup1 /home/user/data/backup2
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

