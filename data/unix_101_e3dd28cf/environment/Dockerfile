FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo 'id,value
1,100
2,200
3,300' > /home/user/data/report.csv
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

