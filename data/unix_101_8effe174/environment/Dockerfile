FROM unix101-base:latest

USER root
RUN echo 'Archived report data' > /home/user/old_report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

