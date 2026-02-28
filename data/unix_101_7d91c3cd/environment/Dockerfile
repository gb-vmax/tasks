FROM unix101-base:latest

USER root
RUN echo 'Hello, Unix world!' > /home/user/fileA.txt
RUN cp /home/user/fileA.txt /home/user/fileB.txt
RUN mkdir -p /logs/verifier
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

