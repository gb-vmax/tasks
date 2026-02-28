FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/docs
RUN echo 'Q1 Results: 100' > /home/user/docs/report.txt
RUN bzip2 /home/user/docs/report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

