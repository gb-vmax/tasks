FROM unix101-base:latest

USER root
RUN echo 'This is a test file.' > /home/user/data.txt
RUN gzip /home/user/data.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

