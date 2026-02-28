FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN echo 'Quarterly results' > /home/user/docs/report.txt
RUN touch -t 202305101530.00 /home/user/docs/report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

