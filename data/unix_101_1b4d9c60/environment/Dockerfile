FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/testsync
RUN echo 'A test file for sync' > /home/user/testsync/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

