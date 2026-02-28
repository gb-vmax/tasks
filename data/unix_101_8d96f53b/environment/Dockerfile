FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/reports/2020
RUN mkdir -p /home/user/archive
RUN echo 'Annual Report 2020' > /home/user/reports/2020/report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

