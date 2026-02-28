FROM unix101-base:latest

USER root
RUN echo 'Quarterly report: Q1 results' > /home/user/report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

