FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/data
RUN echo -n 'Report: Q1 Results\nProfit up 20%' > /home/user/data/report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

