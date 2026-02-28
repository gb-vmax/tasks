FROM unix101-base:latest

USER root
RUN rm -rf /home/user/fifos
RUN mkdir -p /home/user/fifos
RUN chown -R user:user /home/user
RUN chown -R user:user /home/user

USER user
WORKDIR /home/user

