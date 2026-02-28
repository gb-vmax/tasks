FROM unix101-base:latest

USER root
RUN echo 'Hello, Hexdump!' > /home/user/sample.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

