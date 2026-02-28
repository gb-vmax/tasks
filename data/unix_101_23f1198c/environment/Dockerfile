FROM unix101-base:latest

USER root
RUN echo 'Hello, this is a plain text file.' > /home/user/test.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

