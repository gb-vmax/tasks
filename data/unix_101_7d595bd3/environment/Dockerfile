FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/reports
RUN echo -e 'report 1\nreport 2\nreport 3' > /home/user/reports/summary.txt
RUN cp /home/user/reports/summary.txt /home/user/reports/summary.txt.orig
RUN sed -i '2s/report 2/report two/' /home/user/reports/summary.txt
RUN gzip -c /home/user/reports/summary.txt.orig > /home/user/reports/summary.txt.gz
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

