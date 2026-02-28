FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/text
RUN echo -n 'Hello, od!' > /home/user/text/sample.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

