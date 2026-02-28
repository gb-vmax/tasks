FROM unix101-base:latest

USER root
RUN echo 'This file will be deleted.' > /home/user/remove_me.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

