FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN mkdir -p /home/user/backup
RUN echo 'April report' > /home/user/docs/report.txt
RUN echo 'Short summary' > /home/user/docs/summary.txt
RUN echo 'Old report' > /home/user/backup/report.txt
RUN echo 'Backup summary' > /home/user/backup/summary.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

