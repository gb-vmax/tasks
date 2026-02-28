FROM unix101-base:latest

USER root
RUN printf "Q2 sales data\nTotal: 12345\n" > /home/user/old_report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

