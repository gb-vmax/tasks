FROM unix101-base:latest

USER root
RUN rm -f /home/user/current_nice.txt
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

