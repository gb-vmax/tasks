FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/documents
RUN echo 'Annual Report 2023' > /home/user/documents/report.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

