FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/documents/a /home/user/documents/b
RUN echo 'report data' > /home/user/documents/a/report.txt
RUN echo 'report data' > /home/user/documents/b/report.txt
RUN echo 'other data' > /home/user/documents/a/summary.txt
RUN echo 'other data' > /home/user/documents/b/summary2.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

