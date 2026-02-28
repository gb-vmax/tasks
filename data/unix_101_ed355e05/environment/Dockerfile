FROM unix101-base:latest

USER root
RUN echo 'Primary dataset contents' > /home/user/source_data.txt
RUN mkdir -p /home/user/backup
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

