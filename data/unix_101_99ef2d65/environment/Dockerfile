FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/confidential
RUN echo 'Top secret data 12345' > /home/user/confidential/report.dat
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

