FROM unix101-base:latest

USER root
RUN mkdir -p /home/user/
RUN echo 'First file' > /home/user/first.txt
RUN sleep 1
RUN echo 'Second file' > /home/user/second.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

