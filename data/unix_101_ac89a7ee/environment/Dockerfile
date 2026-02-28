FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/documents
RUN echo 'Quarterly Report' > /home/user/documents/report.txt
RUN rm -f /home/user/output.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

