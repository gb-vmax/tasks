FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN echo 'Quarterly financial summary' > /home/user/docs/report.txt
RUN touch -t 202212251230.00 /home/user/docs/report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

